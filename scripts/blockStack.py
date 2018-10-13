from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 370
y = 72
z = 538
blockType = 103
mc.setBlock(x, y, z, blockType)

y = y + 1
mc.setBlock(x, y, z, blockType)
