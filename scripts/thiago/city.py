from mcpi.minecraft import Minecraft
import tower
from blocks import block
import house

mc = Minecraft.create()

air = block["air"]
bedrock = block["bedrock"]
bricks = block["bricks"]
cobblestone = block["cobblestone"]
dirt = block["dirt"]
water = block["water"]

#Criando o terreno
# mc.setBlocks(-110, 60, -110, 110, 200, 110, air)
# mc.setBlocks(-110, 60, -110, 110, 65, 110, dirt)
# mc.setBlocks(-60, 50, -60, 60, 65, 60, air)
# mc.setBlocks(-60, 50, -60, 60, 63, 60, water)
# mc.setBlocks(-55, 70, -55, 55, 70, 55, cobblestone)
# mc.setBlocks(-53, 59, -53, 53, 70, 53, cobblestone)
# mc.setBlocks(-50, 60, -50, 50, 70, 50, air)

tower.buildTower(0, 60, 0, bedrock)
house.buildHouse(20, 60, 0, bricks)
house.buildHouse(0, 60, 20, bricks)
house.buildHouse(-20, 60, 0, bricks)
house.buildHouse(0, 60, -20, bricks)
