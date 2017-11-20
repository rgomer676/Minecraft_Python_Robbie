from mcpi.minecraft import Minecraft
mc = Minecraft.create()
blockType = 50
pos = mc.player.getTilePos()

x = pos.x
y = pos.y
z = pos.z
mc.setBlock(x, y, z, blockType)

