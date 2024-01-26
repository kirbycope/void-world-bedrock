![void-world-bedrock](/void-world-bedrock.png)

# void-world-bedrock
A Void World for Minecraft Bedrock

## How To Install
1. Download the [.mcworld](https://github.com/kirbycope/void-world-bedrock/raw/main/void-world-bedrock.mcworld) file
1. Double-click to install

## How To Create
1. Create New World
   - World Type: Flat
1. Save and Quit after the world generates
1. Download and Install [Universal Minecraft Editor](https://www.universalminecrafteditor.com/)
1. Select "Windows 10", then your save
1. Select "World Settings"
1. Scroll down to ”FlatWorldLayers” and remove the biomes so that it looks like `{"biome_id":1,"block_layers":[],"encoding_version":6,"structure_options":null,"world_version":"version.post_1_18"}
`
1. Save and exit the editor
1. Open the save folder (in `com.mojang/minecraftWorlds`)
1. Delete the `db` folder's content and the `level.dat_old` file
1. Start the level and double-jump to fly
1. Enter the command `/tp 0 64 0`
1. Enter the command `/setblock 0 63 0 grass`
1. Exit the world
1. Select the edit icon, scroll down, and export
1. Re-Edit the save in Universal Minecraft Editor to your liking (difficulty, cheats off, etc).
1. (Back in Minecraft) Select the edit icon, scroll down, and export
