from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 10
y = 11
z = 12
gift = mc.getBlock(x, y, z)

if gift == 57:
    mc.postToChat("Yay! Diamonds!")

elif gift == 6:
    mc.postToChat("Saplings? I guess thats ok...")

else:
    mc.postToChat("Bring a gift to " + str(x) + ", " + str(y) + ", " + str(z))
