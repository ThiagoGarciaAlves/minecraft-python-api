from mcpi.minecraft import Minecraft
from blocks import block

mc = Minecraft.create()
x = -499.5
y = 65
z = 0.5
width = 10
heigth = 5
length = 6
floors = 4
blockType = block["diamond"]
air = block["air"]

for i in range(floors): 
    mc.setBlocks(x, y, z, x + width, y + heigth, z + length, blockType)
    mc.setBlocks(x+1, y+1, z+1, x+width-1, y+heigth-1, z+length-1, air)
    y = y + heigth

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -499
y = 66
z = 5
blockType = block["chest"]
mc.setBlock(x, y, z, blockType)
x = x + 1
mc.setBlock(x, y, z, blockType)

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -492
y = 66
z = 5
blockType = block["chest"]
mc.setBlock(x, y, z, blockType)
x = x + 1
mc.setBlock(x, y, z, blockType)

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -495
y = 74
z = 5
blockType = block["ladder"]
mc.setBlock(x, y, z, blockType)
x = x + 1 

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -495
y = 73
z = 5
blockType = block["ladder"]
mc.setBlock(x, y, z, blockType)
x = x + 1 

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -495
y = 72
z = 5
blockType = block["ladder"]
mc.setBlock(x, y, z, blockType)
x = x + 1 

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -495
y = 71
z = 5
blockType = block["ladder"]
mc.setBlock(x, y, z, blockType)
x = x + 1 

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -495
y = 70
z = 5
blockType = block["ladder"]
mc.setBlock(x, y, z, blockType)
x = x + 1 

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -495
y = 69
z = 5
blockType = block["ladder"]
mc.setBlock(x, y, z, blockType)
x = x + 1 

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -495
y = 68
z = 5
blockType = block["ladder"]
mc.setBlock(x, y, z, blockType)
x = x + 1 

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -495
y = 67
z = 5
blockType = block["ladder"]
mc.setBlock(x, y, z, blockType)
x = x + 1 

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -495
y = 75
z = 5
blockType = block["ladder"]
mc.setBlock(x, y, z, blockType)
x = x + 1 

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -495
y = 76
z = 5
blockType = block["ladder"]
mc.setBlock(x, y, z, blockType)
x = x + 1

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -495
y = 77
z = 5
blockType = block["ladder"]
mc.setBlock(x, y, z, blockType)
x = x + 1

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -495
y = 78
z = 5
blockType = block["ladder"]
mc.setBlock(x, y, z, blockType)
x = x + 1

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -495
y = 79
z = 5
blockType = block["ladder"]
mc.setBlock(x, y, z, blockType)
x = x + 1

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -495
y = 80
z = 5
blockType = block["ladder"]
mc.setBlock(x, y, z, blockType)
x = x + 1

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -495
y = 81
z = 5
blockType = block["ladder"]
mc.setBlock(x, y, z, blockType)
x = x + 1

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -495
y = 66
z = 5
blockType = block["ladder"]
mc.setBlock(x, y, z, blockType)
y = y + 1

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -495
y = 82
z = 5
blockType = block["ladder"]
mc.setBlock(x, y, z, blockType)
y = y + 1

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -495
y = 83
z = 5
blockType = block["ladder"]
mc.setBlock(x, y, z, blockType)
y = y + 1

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -495
y = 85
z = 5
blockType = block["ladder"]
mc.setBlock(x, y, z, blockType)
y = y + 1

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -495
y = 84
z = 5
blockType = block["ladder"]
mc.setBlock(x, y, z, blockType)
y = y + 1

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -495
y = 66
z = 0.255
blockType = block["birchDoorBlock"]
mc.setBlock(x, y, z, blockType)
y = y + 1
mc.setBlock(x, y, z, blockType)

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = -499
y = 81
z = 1
blockType = block["mobSpawner"]
mc.setBlock(x, y, z, blockType)
x = x + 8
mc.setBlock(x, y, z, blockType)