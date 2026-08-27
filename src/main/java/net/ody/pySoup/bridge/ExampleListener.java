package net.ody.pySoup.bridge;

import io.papermc.paper.event.player.AsyncChatEvent;
import org.bukkit.Material;
import org.bukkit.entity.EntityType;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.block.BlockBreakEvent;

public class ExampleListener implements Listener {
    @EventHandler
    public void onEvent(BlockBreakEvent event){
        event.getBlock().getWorld();
    }
}
