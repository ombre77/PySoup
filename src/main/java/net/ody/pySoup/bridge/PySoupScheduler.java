package net.ody.pySoup.bridge;

import net.ody.pySoup.PySoupErrors;
import org.bukkit.plugin.Plugin;
import org.bukkit.scheduler.BukkitTask;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Value;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.logging.Level;

public class PySoupScheduler {
    private final Plugin plugin;
    private final Map<Integer, Context> taskContexts = new ConcurrentHashMap<>();

    public PySoupScheduler(Plugin plugin) {
        this.plugin = plugin;
    }

    private void runCallback(Value callback, Context context) {
        try {
            callback.execute();
        } catch (org.graalvm.polyglot.PolyglotException e) {
            PySoupErrors.log(plugin.getLogger(), "scheduledTask", context, e);
        } catch (Exception e) {
            plugin.getLogger().log(Level.SEVERE, "Unexpected error running scheduled task", e);
        }
    }

    private int track(BukkitTask task) {
        taskContexts.put(task.getTaskId(), Context.getCurrent());
        return task.getTaskId();
    }

    public int runTask(Value callback) {
        if (!callback.canExecute()) throw new IllegalArgumentException("callback not callable");
        Context context = Context.getCurrent();
        return track(plugin.getServer().getScheduler()
                .runTask(plugin, () -> runCallback(callback, context)));
    }

    public int runTaskLater(Value callback, long delayTicks) {
        if (!callback.canExecute()) throw new IllegalArgumentException("callback not callable");
        Context context = Context.getCurrent();
        return track(plugin.getServer().getScheduler()
                .runTaskLater(plugin, () -> runCallback(callback, context), delayTicks));
    }

    public int runTaskTimer(Value callback, long delayTicks, long periodTicks) {
        if (!callback.canExecute()) throw new IllegalArgumentException("callback not callable");
        Context context = Context.getCurrent();
        return track(plugin.getServer().getScheduler()
                .runTaskTimer(plugin, () -> runCallback(callback, context), delayTicks, periodTicks));
    }

    public int runTaskAsync(Value callback) {
        if (!callback.canExecute()) throw new IllegalArgumentException("callback not callable");
        Context context = Context.getCurrent();
        return track(plugin.getServer().getScheduler()
                .runTaskAsynchronously(plugin, () -> runCallback(callback, context)));
    }

    public int runTaskTimerAsync(Value callback, long delayTicks, long periodTicks) {
        if (!callback.canExecute()) throw new IllegalArgumentException("callback not callable");
        Context context = Context.getCurrent();
        return track(plugin.getServer().getScheduler()
                .runTaskTimerAsynchronously(plugin, () -> runCallback(callback, context), delayTicks, periodTicks));
    }

    public void cancelTask(int taskId) {
        plugin.getServer().getScheduler().cancelTask(taskId);
        taskContexts.remove(taskId);
    }

    public void unregisterContext(Context context) {
        taskContexts.entrySet().removeIf(entry -> {
            if (entry.getValue().equals(context)) {
                plugin.getServer().getScheduler().cancelTask(entry.getKey());
                return true;
            }
            return false;
        });
    }
}