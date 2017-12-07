from mcpi.minecraft import Minecraft
mc = minecraft.create()

x = 6
y = 5
z = 28
blockType = 103
up = 1
mc.setBlock(x, y, z, blockType)
mc.setBlock(x, y + up, z, blockType)
