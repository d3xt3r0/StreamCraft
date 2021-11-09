package io.dexterolabs.streamcraft.commands;

import org.bukkit.Location;
import org.bukkit.World;
import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.EntityType;
import org.bukkit.entity.Player;

import io.dexterolabs.streamcraft.Main;

public class SpawnCommand implements CommandExecutor{
	private Main plugin;
	
	public SpawnCommand(Main plugin) {
		this.plugin = plugin;
		plugin.getCommand("spawno").setExecutor(this);
	}

	@Override
	public boolean onCommand(CommandSender sender, Command cmd, String arg2, String[] arg3) {
		// TODO Auto-generated method stub
		
		Player p = (Player) sender;
		Location loc = p.getLocation();
		
		World w = p.getWorld();		
		w.spawnEntity(loc, EntityType.CREEPER);
		
		return false;
	}

}
