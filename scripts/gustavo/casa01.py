from mcpi.minecraft import Minecraft
from blocks import block

mc = Minecraft.create()
pos = mc.player.getTilePos()

x = pos.x
y = pos.y
z = pos.z
width = 10
heigth = 5
length = 6
blockType = block["ironBlock"]
air = block["air"]

mc.setBlocks(x, y, z, x + width, y + heigth, z + length, blockType)
mc.setBlocks(x+1, y+1, z+1, x+width-1, y+heigth-1, z+length-1, air)