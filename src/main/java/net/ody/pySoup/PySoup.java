package net.ody.pySoup;

import org.bukkit.plugin.java.JavaPlugin;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.HostAccess;
import org.graalvm.polyglot.Source;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.logging.Logger;

public final class PySoup extends JavaPlugin {
    public final Logger logger=getLogger();
    public Context context;

    @Override
    public void onEnable() {
        context= Context.newBuilder("python")
                .allowHostAccess(HostAccess.ALL)
                .allowHostClassLookup(PySoup -> true)
                .allowAllAccess(true)
                .build();

        try {
            String pythonSourceCode = Files.readString(
                    Path.of(getDataFolder().toPath().toString(), "pysoup/pysoup.py")
            );

            context.getBindings("python").putMember("_pysoup_internal", new PySoupBridge(logger));
            context.eval(Source.newBuilder("python",pythonSourceCode,"pysoup.py").build());

        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public void onDisable() {
        if (context!=null) context.close();
    }
}
