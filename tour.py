from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x = -35
y = 3
z = 80

mc.player.setTilePos(x, y, z)

time.sleep(10)

x = -30
y =10
z = 75

mc.player.setTilePos(x, y, z)
