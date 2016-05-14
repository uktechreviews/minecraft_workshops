import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()
mc.postToChat("Hello World, Steve here!")
mc.postToChat("Is that a creeper behind you?")
p = mc.player.getPos()
mc.player.setPos (p.x, p.y+10, p.z)
tile = mc.player.getTilePos()
mc.setBlock (tile.x, tile.y, tile.z,block.SNOW.id)
