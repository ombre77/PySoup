package net.ody.pySoup;

import org.bukkit.Bukkit;
import org.bukkit.Material;
import org.bukkit.World;
import org.bukkit.block.Block;

import java.util.logging.Logger;

public class PySoupBridge {
    /*
    When writing new handlers!!!
    - Create the Java handler
    - Make sure that it is connected
    - Create python placeholder
    - Create API method
    :)
     */


    private final Logger logger;

    public PySoupBridge(Logger logger){
        this.logger=logger;
    }

    public final WorldActions world= new WorldActions();
    public final PluginActions plugin=new PluginActions();
    public final Resolver resolver= new Resolver();

    public static class WorldActions{
        public Block getBlock(String worldName, int x, int y, int z) {
            World w = Bukkit.getWorld(worldName);
            if (w==null) return null;
            return w.getBlockAt(x, y, z);
        }

        public void setBlock(String worldName, int x, int y, int z, Object materialData) {
            World w =Bukkit.getWorld(worldName);
            Material material=(Material) materialData;
            if (w==null) return;
            w.getBlockAt(x,y,z).setType(material);
        }
    }

    public class PluginActions {
        public void log(int level, String content) {
            switch (level){
                case 1->logger.info(content);
                case 2->logger.warning(content);
            }
        }
    }

    public static class Resolver{
        public Object resolverMaterial(String materialName){
            return Material.valueOf(materialName);
        }
    }
}

