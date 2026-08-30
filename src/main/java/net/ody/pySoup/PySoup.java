package net.ody.pySoup;

import com.mojang.brigadier.Command;
import io.papermc.paper.command.brigadier.Commands;
import io.papermc.paper.plugin.lifecycle.event.types.LifecycleEvents;
import net.kyori.adventure.text.Component;
import net.kyori.adventure.text.format.NamedTextColor;
import net.ody.pySoup.bridge.PySoupBridge;
import org.bukkit.Bukkit;
import org.bukkit.plugin.java.JavaPlugin;

import java.util.List;

public final class PySoup extends JavaPlugin {

    private PySoupBridge bridge;
    private ScriptManager scriptManager;

    @Override
    public void onEnable() {
        bridge=new PySoupBridge(this);
        scriptManager = new ScriptManager(this,bridge);
        scriptManager.loadAll();

        getLifecycleManager().registerEventHandler(LifecycleEvents.COMMANDS,event -> {
            event.registrar().register(
                    Commands.literal("pysoup")
                            .then(
                                    Commands.literal("reload")
                                            .executes( context -> {
                                                scriptManager.unloadAll();

                                                List<ScriptManager.LoadResult> results=scriptManager.loadAll();
                                                long successCount=results.stream().filter(ScriptManager.LoadResult::success).count();

                                                Bukkit.broadcast(Component.text(
                                                        "(PySoup) Reloaded "+successCount +"/" +results.size()+" scripts"
                                                ));

                                                for (ScriptManager.LoadResult result : results) {
                                                    if (result.success()) {
                                                        Bukkit.broadcast(Component.text("  ✓ " + result.name())
                                                                .color(NamedTextColor.GREEN));
                                                    } else {
                                                        Bukkit.broadcast(Component.text("  ✗ " + result.name() + ": " + result.error())
                                                                .color(NamedTextColor.RED));
                                                    }
                                                }

                                                return Command.SINGLE_SUCCESS;
                                            })
                            )
                            .build()
            );
        });
    }

    @Override
    public void onDisable() {
        if (scriptManager != null) {
            scriptManager.shutdown();
        }
    }

    public ScriptManager getScriptManager() {
        return scriptManager;
    }

    public PySoupBridge getBridge() {
        return bridge;
    }
}