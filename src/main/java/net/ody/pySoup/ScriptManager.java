package net.ody.pySoup;

import net.ody.pySoup.bridge.PySoupBridge;
import org.bukkit.plugin.Plugin;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Engine;
import org.graalvm.polyglot.Source;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
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

    private static final List<String> LIB_RESOURCES = List.of(
            "lib/pysoup/__init__.py"
    );

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

    private void extractLib() {
        for (String resourcePath : LIB_RESOURCES) {
            // resourcePath is "lib/pysoup/__init__.py" - strip the leading
            // "lib/" so it lands at <dataFolder>/lib/pysoup/__init__.py
            File dest = new File(plugin.getDataFolder(), resourcePath);

            try (InputStream in = plugin.getClass().getClassLoader().getResourceAsStream(resourcePath)) {
                if (in == null) {
                    logger.warning("Bundled lib resource missing from jar: " + resourcePath);
                    continue;
                }
                Path destPath = dest.toPath();
                Files.createDirectories(destPath.getParent());
                Files.copy(in, destPath, java.nio.file.StandardCopyOption.REPLACE_EXISTING);
            } catch (IOException e) {
                logger.severe("Failed to extract lib resource " + resourcePath + ": " + e.getMessage());
            }
        }
    }

    public void load(File file) {
        String name = file.getName();
        logger.info("Loading script '"+name+"'");

        // If this script is already loaded, close the old context first -
        // reload should leave no leftover state from the previous version.
        ScriptInstance existing = scripts.get(name);
        if (existing != null) {
            existing.close();
            scripts.remove(name);
        }

        try {
            Context context = Context.newBuilder("python")
                    .engine(engine)
                    .allowAllAccess(true)
                    .option("python.PythonPath", libDir.getAbsolutePath())
                    .build();

            context.getPolyglotBindings().putMember("bridge", bridge);

            Source source = Source.newBuilder("python", file).build();
            context.eval(source);

            scripts.put(name, new ScriptInstance(name, file, context));
            logger.info("Loaded script: " + name);
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
