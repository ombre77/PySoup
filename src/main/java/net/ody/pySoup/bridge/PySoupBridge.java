package net.ody.pySoup.bridge;

import org.bukkit.Server;
import org.bukkit.event.Event;
import org.bukkit.event.EventPriority;
import org.bukkit.event.Listener;
import org.bukkit.plugin.EventExecutor;
import org.bukkit.plugin.Plugin;
import org.graalvm.polyglot.Value;

import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.logging.Level;

public class PySoupBridge {
    private final Plugin plugin;
    private final Listener dispatchListener = new Listener() {};

    private final Map<Class<? extends Event>, List<Value>> handlers = new ConcurrentHashMap<>();

    public PySoupBridge(Plugin plugin) {
        this.plugin = plugin;
    }

    @SuppressWarnings("unchecked")
    public void registerEvent(String eventClassName, Value callback) {
        if (!callback.canExecute()) {
            throw new IllegalArgumentException("Callback for " + eventClassName + " is not callable");
        }

        Class<? extends Event> eventClass;
        try {
            eventClass = (Class<? extends Event>) Class.forName(eventClassName);
        } catch (ClassNotFoundException e) {
            throw new IllegalArgumentException("Unknown event class: " + eventClassName, e);
        }

        boolean firstHandlerForThisEvent = !handlers.containsKey(eventClass);
        handlers.computeIfAbsent(eventClass, c -> new CopyOnWriteArrayList<>()).add(callback);

        if (firstHandlerForThisEvent) {
            EventExecutor executor = (listener, event) -> dispatch(eventClass, event);
            plugin.getServer().getPluginManager()
                    .registerEvent(eventClass, dispatchListener, EventPriority.NORMAL, executor, plugin);
        }
    }

    private void dispatch(Class<? extends Event> eventClass, Event event) {
        List<Value> callbacks = handlers.get(eventClass);
        if (callbacks == null) {
            return;
        }
        for (Value callback : callbacks) {
            try {
                callback.execute(event);
            } catch (Exception e) {
                plugin.getLogger().log(Level.SEVERE,
                        "Error in python handler for " + eventClass.getSimpleName(), e);
            }
        }
    }

    public Server getServer() {
        return plugin.getServer();
    }

    public void log(String message) {
        plugin.getLogger().info(message);
    }
}
