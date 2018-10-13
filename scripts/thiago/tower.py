from mcpi.minecraft import Minecraft
from blocks import block

mc = Minecraft.create()

x = -3
y = 60
z = -3
width = 7
heigth = 5
length = 7
floors = 10
blockType = block["bedrock"]
air = block["air"]

for i in range(floors):
    mc.setBlocks(x, y, z, x + width, y + heigth, z + length, blockType)
    mc.setBlocks(x+1, y+1, z+1, x+width-1, y+heigth-1, z+length-1, air)
    y = y + heigth
