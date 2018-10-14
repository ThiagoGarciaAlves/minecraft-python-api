from mcpi.minecraft import Minecraft
from blocks import block

mc = Minecraft.create()
pos = mc.player.getTilePos()

x = 460
y = 88
z = 0
width = 10
heigth = 5
length = 6

ironBlock = block["ironBlock"]
air = block["air"]
slab = block["spruceWoodSlab"]
plank = block["birchWoodPlank"]
door = block["oakDoorBlock"]
glass = block["glass"]
stairs = block["oakWoodStairs"]

mc.setBlocks(459, 94, 6, 459 - width, 94 - heigth, 6 - length, stairs)
mc.setBlocks(470, 94, 0, 470 + width, 94 - heigth, 0 + length, stairs)
mc.setBlocks(460, 95, 0, 460 + width, 95 + heigth, 0 + length, stairs)
mc.setBlocks(449, 95, 0, 449 + width, 95 + heigth + 1, 0 + length, stairs)
mc.setBlocks(471, 95, 0, 471 + width, 95 + heigth + 1, 0 + length, stairs)

mc.setBlocks(x, y, z, x + width, y + heigth + 1, z + length, plank)

mc.setBlocks(x, y, z, x + width, y + heigth, z + length, ironBlock)

mc.setBlocks(x+1, y+1, z+1, x+width-1, y+heigth, z+length-1, air)


mc.setBlock(465, 90, 0, air)    
mc.setBlock(465, 89, 0, air)

mc.setBlock(467, 90, 0, glass)   
mc.setBlock(468, 90, 0, glass)    
mc.setBlock(469, 90, 0, glass)    
mc.setBlock(467, 91, 0, glass)    
mc.setBlock(468, 91, 0, glass)    
mc.setBlock(469, 91, 0, glass)

mc.setBlock(463, 90, 0, glass)    
mc.setBlock(462, 90, 0, glass)    
mc.setBlock(461, 90, 0, glass)
mc.setBlock(463, 91, 0, glass)    
mc.setBlock(462, 91, 0, glass)    
mc.setBlock(461, 91, 0, glass)

mc.setBlock(460, 91, 3, glass)    
mc.setBlock(460, 92, 3, glass)    
mc.setBlock(460, 90, 3, glass)
mc.setBlock(460, 91, 4, glass)    
mc.setBlock(460, 91, 2, glass)

mc.setBlock(470, 91, 3, glass)    
mc.setBlock(470, 92, 3, glass)    
mc.setBlock(470, 90, 3, glass)
mc.setBlock(470, 91, 4, glass)    
mc.setBlock(470, 91, 2, glass)