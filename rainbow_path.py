import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
import random
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

while True:
	p = mc.player.getTilePos()
	c=random.choice(list)
	mc.setBlock(p.x,p.y-1,p.z,block.WOOL.id,c)
