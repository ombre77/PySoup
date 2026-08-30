package net.ody.pySoup.bridge;

import net.kyori.adventure.text.Component;
import net.kyori.adventure.text.serializer.plain.PlainTextComponentSerializer;
import org.bukkit.Bukkit;
import org.bukkit.Server;
import org.bukkit.plugin.Plugin;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Value;

public class PySoupBridge {
    private final Plugin plugin;
    private final PySoupEventDispatcher dispatcher;
    private final PySoupScheduler scheduler;

    public PySoupBridge(Plugin plugin) {
        this.plugin = plugin;
        this.dispatcher = new PySoupEventDispatcher(plugin);
        this.scheduler = new PySoupScheduler(plugin);
    }

    // --- events ---
    public void registerEvent(String eventClassName, Value callback) {
        dispatcher.registerEvent(eventClassName, callback);
    }

    // --- scheduler ---
    public int runTask(Value callback) {
        return scheduler.runTask(callback);
    }

    public int runTaskLater(Value callback, long delayTicks) {
        return scheduler.runTaskLater(callback, delayTicks);
    }

    public int runTaskTimer(Value callback, long delayTicks, long periodTicks) {
        return scheduler.runTaskTimer(callback, delayTicks, periodTicks);
    }

    public int runTaskAsync(Value callback) {
        return scheduler.runTaskAsync(callback);
    }

    public int runTaskTimerAsync(Value callback, long delayTicks, long periodTicks) {
        return scheduler.runTaskTimerAsync(callback, delayTicks, periodTicks);
    }

    public void cancelTask(int taskId) {
        scheduler.cancelTask(taskId);
    }

    // --- lifecycle cleanup, called from ScriptManager on unload/reload ---
    public void unregisterContext(Context context) {
        dispatcher.unregisterContext(context);
        scheduler.unregisterContext(context);
    }

    // --- method for python lib ---
    public Server getServer() {
        return plugin.getServer();
    }

    public void log(String message) {
        plugin.getLogger().info(message);
    }

    public void broadcast(String message) {
        Bukkit.broadcast(Component.text(message));
    }

    public String getStringFromComponent(Component component) {
        return PlainTextComponentSerializer.plainText().serialize(component);
    }
}