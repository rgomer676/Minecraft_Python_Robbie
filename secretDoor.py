from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 10
y = 11
z = 12

gift = mc.getBlock(x, y, z)
if gift != 0:
    if gift == 57:
        mc.setBlock(9, 5, 15, 0)
        mc.setBlock(10, 5, 15, 0)
        mc.setBlock(11, 5, 15, 0)
    else:
        mc.setBlock(10, 11, 12, 10)
        mc.setBlock(10, 10, 12, 10)
        mc.setBlock(10, 12, 12, 10)
else:
    mc.postToChat ("Place your offering on the pedestal.")
    
