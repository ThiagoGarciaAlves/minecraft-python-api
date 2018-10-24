from mcpi.minecraft import Minecraft
import tower
from blocks import block
import melon

mc = Minecraft.create()

air = block["air"]
cobblestone = block["cobblestone"]
dirt = block["dirt"]
grass = block["grassBlock"]
water = block["water"]
melon = block["melon"]
glass = block["glass"]
grass2 = block["grassPath"]

    #Criando o terreno
mc.setBlocks(900, 72, -50, 1000, 200, 50, air)
mc.setBlocks(900, 72, -50, 1000, 77, 50, dirt)
mc.setBlocks(998, 77, 48, 902, 74, -47, water)
mc.setBlocks(905, 78, -44, 995, 78, 45, grass)
mc.setBlocks(995, 79, 45, 993, 89, -43, cobblestone)
mc.setBlocks(995, 79, -44, 905, 89, -42, cobblestone)
mc.setBlocks(905, 79, -43, 907, 89, 45, cobblestone)
mc.setBlocks(905, 79, 45, 995, 89, 43, cobblestone)
mc.setBlocks(995, 93, 45, 905, 93, -44, cobblestone)
mc.setBlocks(908, 93, -41, 992, 93, 42, air)
mc.setBlocks(946, 78, -1, 908, 78, 2, grass2)
mc.setBlocks(955, 78, 2, 992, 78, -1, grass2)

    #Criando um lago central
mc.setBlocks(943, 79, 8, 958, 79, -7, glass)
mc.setBlocks(944, 79, 7, 957, 79, -6, air)
mc.setBlocks(944, 79, 7, 957, 79, -6, water)
mc.setBlocks(942, 80, -8, 959, 80, -8, glass)
mc.setBlocks(942, 80, -8, 942, 80, 9, glass)
mc.setBlocks(942, 80, 9, 959, 80, 9, glass)
mc.setBlocks(959, 80, 9, 959, 80, -8, glass)
mc.setBlocks(943, 80, 8, 958, 80, -7, water)

    #Criando as casas
tower.buildTower(950, 79, 0, glass)
melon.buildHouse(911, 79, 38, melon)
melon.buildHouse(911, 79, -38, melon)
melon.buildHouse(988, 79, -38, melon)
melon.buildHouse(988, 79, 38, melon)