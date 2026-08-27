package net.ody.pySoup;

import net.ody.pySoup.bridge.PySoupBridge;
import org.bukkit.plugin.Plugin;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Engine;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Source;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.logging.Logger;

public class ScriptManager {
    private final Plugin plugin;
    private final Logger logger;
    private final PySoupBridge bridge;
    private final File scriptsDir;
    private final File libDir;

    private Engine engine;
    private final Map<String, ScriptInstance> scripts = new HashMap<>();

    public ScriptManager(Plugin plugin, PySoupBridge bridge) {
        this.plugin = plugin;
        this.bridge=bridge;
        this.logger = plugin.getLogger();
        this.scriptsDir = new File(plugin.getDataFolder(), "scripts");
        this.libDir = new File(plugin.getDataFolder(), "lib");
    }

    /** Copy every resource bundled under lib/ in the plugin jar out to the
     * data folder, overwriting each time. Walks the jar directly rather than
     * a hardcoded file list, so newly added lib files are picked up
     * automatically instead of silently going missing until someone
     * remembers to list them. */
    private void extractLib() {
        File jarFile;
        try {
            jarFile = new File(plugin.getClass().getProtectionDomain().getCodeSource().getLocation().toURI());
        } catch (Exception e) {
            logger.severe("Could not locate plugin jar to extract lib: " + e.getMessage());
            return;
        }

        try (java.util.jar.JarFile jar = new java.util.jar.JarFile(jarFile)) {
            java.util.Enumeration<java.util.jar.JarEntry> entries = jar.entries();
            while (entries.hasMoreElements()) {
                java.util.jar.JarEntry entry = entries.nextElement();
                String name = entry.getName();
                if (entry.isDirectory() || !name.startsWith("lib/")) {
                    continue;
                }

                File dest = new File(scriptsDir, name.substring("lib/".length()));
                try (InputStream in = jar.getInputStream(entry)) {
                    Files.createDirectories(dest.toPath().getParent());
                    Files.copy(in, dest.toPath(), java.nio.file.StandardCopyOption.REPLACE_EXISTING);
                }
            }
        } catch (IOException e) {
            logger.severe("Failed to extract bundled lib: " + e.getMessage());
        }
    }

    public void loadAll() {
        engine = Engine.newBuilder("python").build();
        extractLib();

        if (!scriptsDir.exists() && !scriptsDir.mkdirs()) {
            logger.severe("Could not create scripts directory: " + scriptsDir.getAbsolutePath());
            return;
        }

        File[] files = scriptsDir.listFiles((dir, name) -> name.endsWith(".py"));
        if (files == null) {
            return;
        }

        for (File file : files) {
            load(file);
        }
    }

    public void load(File file) {
        String name = file.getName();
        logger.info("Loading script '" + name + "'");

        // If this script is already loaded, close the old context first -
        // reload should leave no leftover state from the previous version.
        ScriptInstance existing = scripts.get(name);
        if (existing != null) {
            existing.close();
            scripts.remove(name);
        }

        Context context = Context.newBuilder("python")
               .engine(engine)
                .allowAllAccess(true)
                .option("python.PythonPath", scriptsDir.getAbsolutePath())
                .build();

        context.getPolyglotBindings().putMember("bridge", bridge);
        try {

            Source source = Source.newBuilder("python", file).build();
            context.eval(source);

            scripts.put(name, new ScriptInstance(name, file, context));
            logger.info("Loaded script: " + name);
        } catch (PolyglotException e) {
            PySoupErrors.log(logger,name,context,e);
        } catch (IOException e) {
            logger.severe("Could not read script " + name + ": " + e.getMessage());
        } catch (Exception e) {
            logger.severe("Failed to load script " + name + ": " + e.getMessage());
        }
    }


    public void unload(String name) {
        ScriptInstance instance = scripts.remove(name);
        if (instance != null) {
            instance.close();
            logger.info("Unloaded script: " + name);
        }
    }

    public void unloadAll(){
        Set<String> names=scripts.keySet();
        for (String name:names){
            unload(name);
        }
    }

    public void shutdown() {
        for (ScriptInstance instance : scripts.values()) {
            instance.close();
        }
        scripts.clear();

        if (engine != null) {
            engine.close();
            engine = null;
        }
    }

    public Map<String, ScriptInstance> getScripts() {
        return scripts;
    }
}
