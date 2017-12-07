from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

x = x + random.randint (-50, 50)
mc.player.setPos(x, y, z)
