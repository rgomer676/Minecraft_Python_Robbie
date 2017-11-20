from mcpi.minecraft import Minecraft
mc = Minecraft.create()

username = input("Enter your username: ")

mc.postToChat(username + ": " + message)
