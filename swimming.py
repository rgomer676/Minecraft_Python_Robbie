from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

blockType = mc.getBlock(x, y, z)
if blockType == 9 :
    mc.postToChat("ur afloat")
else :
    mc.postToChat("land ho")

