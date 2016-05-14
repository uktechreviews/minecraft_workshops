import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()
mc.postToChat(“Is that a melon on your head?”)

while True:
	tile = mc.player.getTilePos()
	mc.setBlock (tile.x, tile.y+2, tile.z,block.MELON.id)
