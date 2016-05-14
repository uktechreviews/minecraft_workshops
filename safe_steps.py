import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

while True:
	p = mc.player.getTilePos()
	b = mc.getBlock(p.x, p.y-1, p.z)
	if b == block.AIR.id or b == block.WATER_FLOWING.id or b==block.WATER_STATIONARY.id:
		mc.setBlock(pos.x, pos.y-1, pos.z, block.WOOD_PLANKS.id)


