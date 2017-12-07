from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 10
y = 11
z = 12
melon = 103
block = mc.getBlock(x, y, z)

if block == melon:
    noMelon = False
else:
    noMelon = True

mc.postToChat("U need moar food: " + str(noMelon))
