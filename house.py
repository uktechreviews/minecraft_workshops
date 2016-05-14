import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
x, y, z = mc.player.getPos()
x+=2
mc.setBlocks(x, y, z, x+4, y+4, z+4, block.COBBLESTONE.id)
mc.setBlocks(x+1, y-1, z+1, x+3, y+3, z+3, block.AIR.id)
mc.setBlocks(x+1, y-1, z+1, x+3, y-1, z+3, block.WOOL.id,14)
mc.setBlocks(x, y, z+2, x, y+1, z+2, block.AIR.id)
