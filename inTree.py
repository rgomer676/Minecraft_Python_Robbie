from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

blockType = mc.getBlock(x, y - 1, z)
if blockType == 11 or blockType == 18 :
    mc.postToChat("birdwatchin")
else :
    mc.postToChat("on the ground")

