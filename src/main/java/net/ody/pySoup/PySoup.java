package net.ody.pySoup;

import net.ody.pySoup.bridge.PySoupBridge;
import org.bukkit.plugin.java.JavaPlugin;
import org.graalvm.polyglot.Context;


public final class PySoup extends JavaPlugin {

    private PySoupBridge bridge;
    private ScriptManager scriptManager;

    @Override
    public void onEnable() {
        bridge=new PySoupBridge(this);
        scriptManager = new ScriptManager(this,bridge);
        scriptManager.loadAll();
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