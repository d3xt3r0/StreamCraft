package io.dexterolabs.streamcraft;

import org.bukkit.plugin.java.JavaPlugin;

import io.dexterolabs.streamcraft.commands.SpawnCommand;

public class Main extends JavaPlugin{
	
	@Override
	public void onEnable() {
		new SpawnCommand(this);
	}
}
