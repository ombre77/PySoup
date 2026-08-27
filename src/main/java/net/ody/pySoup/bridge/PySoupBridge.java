package net.ody.pySoup.bridge;

import net.kyori.adventure.text.Component;
import net.kyori.adventure.text.TextComponent;
import net.ody.pySoup.PySoupErrors;
import org.bukkit.Bukkit;
import org.bukkit.Server;
import org.bukkit.event.Event;
import org.bukkit.event.EventPriority;
import org.bukkit.event.Listener;
import org.bukkit.plugin.EventExecutor;
import org.bukkit.plugin.Plugin;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Value;

import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.logging.Level;

public class PySoupBridge {
    private final Plugin plugin;
    private final Listener dispatchListener = new Listener() {};

    private record RegisteredHandler(Value callback, Context context){}
    private final Map<Class<? extends Event>, List<RegisteredHandler>> handlers = new ConcurrentHashMap<>();

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
        Context context=Context.getCurrent();
        handlers.computeIfAbsent(eventClass,c->new CopyOnWriteArrayList<>())
                .add(new RegisteredHandler(callback,context));

        if (firstHandlerForThisEvent) {
            EventExecutor executor = (listener, event) -> dispatch(eventClass, event);
            plugin.getServer().getPluginManager()
                    .registerEvent(eventClass, dispatchListener, EventPriority.NORMAL, executor, plugin);
        }
    }

    private void dispatch(Class<? extends Event> eventClass, Event event) {
        List<RegisteredHandler> callbacks = handlers.get(eventClass);
        if (callbacks == null) {
            return;
        }
        for (RegisteredHandler h: callbacks) {
            try {
                h.callback.execute(event);
            } catch (org.graalvm.polyglot.PolyglotException e) {
                PySoupErrors.log(plugin.getLogger(),
                        "handler:" + eventClass.getSimpleName(), h.context,e);
            } catch (Exception e) {
                // non-polyglot Java-side failure (shouldn't normally happen here,
                // but keep a fallback so a bad handler can't kill the dispatch loop)
                plugin.getLogger().log(Level.SEVERE,
                        "Unexpected error dispatching " + eventClass.getSimpleName(), e);
            }
        }
    }

    public Server getServer() {
        return plugin.getServer();
    }

    public void log(String message) {
        plugin.getLogger().info(message);
    }

    public void broadcast(String message) {
        Bukkit.broadcast(Component.text(message));
    }

    public String getStringFromComponent(Component component){
        TextComponent textComponent=(TextComponent) component;
        return textComponent.content();
    }

}
