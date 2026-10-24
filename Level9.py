import pygame

from Coin import Coin
from Level import Level
from Obstacle import Obstacle
from SavePosition import SavePosition


class Level9(Level):
    def __init__(self,game_over):
        self.coinObjects = []
        self.restart(game_over)
        self.blocks_1_2_moving_direction = 2
        self.blocks_3_4_moving_direction = 3
        self.obstacles_3_4_moving_condition = False
        self.obstacle18_moving_condition = False


    def restart(self, game_over):

        super().__init__()

        self.blocks_1_2_moving_direction = 2
        self.blocks_3_4_moving_direction = 3
        self.obstacles_3_4_moving_condition = False
        self.obstacle18_moving_condition = False

        wall_up = pygame.image.load('level9pics/wall_up.jpg')
        wall_up_rect = wall_up.get_rect(topleft=(0, 0))
        self.border.append((wall_up, wall_up_rect))

        wall_left = pygame.image.load('level9pics/wall_left.jpg')
        wall_left_rect = wall_left.get_rect(bottomleft=(0, 825))
        self.border.append((wall_left, wall_left_rect))

        wall_topright = pygame.image.load('level9pics/wall_topright.jpg')
        wall_topright_rect = wall_topright.get_rect(topright=(1100, 0))
        self.border.append((wall_topright, wall_topright_rect))

        wall_bottomright = pygame.image.load('level9pics/wall_bottomright.jpg')
        wall_bottomright_rect = wall_bottomright.get_rect(topright= wall_topright_rect.bottomright)
        self.border.append((wall_bottomright, wall_bottomright_rect))

        wall1 = pygame.image.load('level9pics/wall1.jpg')
        wall1_rect = wall1.get_rect(bottomright= wall_topright_rect.bottomright)
        self.border.append((wall1, wall1_rect))

        wall2 = pygame.image.load('level9pics/wall2.jpg')
        wall2_rect = wall2.get_rect(bottomright=wall1_rect.bottomleft)
        self.border.append((wall2, wall2_rect))

        wall3 = pygame.image.load('level9pics/wall3_5_7.jpg')
        wall3_rect = wall3.get_rect(bottomright=wall2_rect.bottomleft)
        self.border.append((wall3, wall3_rect))

        wall4 = pygame.image.load('level9pics/wall4.jpg')
        wall4_rect = wall4.get_rect(bottomright=wall3_rect.bottomleft)
        self.border.append((wall4, wall4_rect))

        wall5 = pygame.image.load('level9pics/wall3_5_7.jpg')
        wall5_rect = wall5.get_rect(bottomright=wall4_rect.bottomleft)
        self.border.append((wall5, wall5_rect))

        wall6 = pygame.image.load('level9pics/wall6.jpg')
        wall6_rect = wall6.get_rect(bottomright=wall5_rect.bottomleft)
        self.border.append((wall6, wall6_rect))

        wall7 = pygame.image.load('level9pics/wall3_5_7.jpg')
        wall7_rect = wall7.get_rect(bottomright=wall6_rect.bottomleft)
        self.border.append((wall7, wall7_rect))

        wall8 = pygame.image.load('level9pics/wall8.jpg')
        wall8_rect = wall8.get_rect(bottomright=wall7_rect.bottomleft)
        self.border.append((wall8, wall8_rect))

        wall9 = pygame.image.load('level9pics/wall9.jpg')
        wall9_rect = wall9.get_rect(bottomleft = wall_left_rect.bottomright)
        self.border.append((wall9, wall9_rect))

        wall10 = pygame.image.load('level9pics/wall10.jpg')
        wall10_rect = wall10.get_rect(bottomleft= wall9_rect.bottomright)
        self.border.append((wall10, wall10_rect))

        wall11 = pygame.image.load('level9pics/wall11_15.jpg')
        wall11_rect = wall11.get_rect(bottomleft=wall10_rect.bottomright)
        self.border.append((wall11, wall11_rect))

        wall12 = pygame.image.load('level9pics/wall12.jpg')
        wall12_rect = wall12.get_rect(bottomleft=wall11_rect.bottomright)
        self.border.append((wall12, wall12_rect))

        wall13 = pygame.image.load('level9pics/wall13.jpg')
        wall13_rect = wall13.get_rect(bottomleft=wall12_rect.bottomright)
        self.border.append((wall13, wall13_rect))

        wall14 = pygame.image.load('level9pics/wall14.jpg')
        wall14_rect = wall14.get_rect(bottomleft=wall13_rect.bottomright)
        self.border.append((wall14, wall14_rect))

        wall15 = wall11
        wall15_rect = wall15.get_rect(bottomleft=wall14_rect.bottomright)
        self.border.append((wall15, wall15_rect))

        wall16 = pygame.image.load('level9pics/wall16.jpg')
        wall16_rect = wall16.get_rect(topright= wall_up_rect.topright)
        self.border.append((wall16, wall16_rect))

        wall17 = pygame.image.load('level9pics/wall17.jpg')
        wall17_rect = wall17.get_rect(midtop= wall16_rect.midbottom)
        self.border.append((wall17, wall17_rect))

        # obstacles

        lv9obstacle1 = Obstacle("down", 1, "topright", (44, 44), wall16_rect.bottomright)
        self.obstacleObjects.append(lv9obstacle1)

        lv9obstacle2 = Obstacle("down", 1, "topleft", (44, 44), wall16_rect.bottomleft)
        self.obstacleObjects.append(lv9obstacle2)

        lv9obstacle3 = Obstacle("down", 1, "midtop", (44, 44), wall17_rect.midbottom)
        self.obstacleObjects.append(lv9obstacle3)

        lv9obstacle4 = Obstacle("up", 1, "bottomleft", (44, 44), (lv9obstacle3.rect.x, lv9obstacle3.rect.y + 134))
        self.obstacleObjects.append(lv9obstacle4)

        lv9obstacle5 = Obstacle("up", 1, "midbottom", (44, 44), wall5_rect.midtop)
        self.obstacleObjects.append(lv9obstacle5)

        lv9obstacle6 = Obstacle("up", 1, "midbottom", (44, 44), wall7_rect.midtop)
        self.obstacleObjects.append(lv9obstacle6)

        lv9obstacle7 = Obstacle("up", 1, "bottomleft", (44, 44), wall8_rect.topleft)
        self.obstacleObjects.append(lv9obstacle7)

        lv9obstacle8 = Obstacle("up", 1, "bottomleft", (44, 44), lv9obstacle7.rect.bottomright)
        self.obstacleObjects.append(lv9obstacle8)

        lv9obstacle9 = Obstacle("up", 1, "bottomleft", (44, 44), lv9obstacle8.rect.bottomright)
        self.obstacleObjects.append(lv9obstacle9)

        lv9obstacle10 = Obstacle("up", 1, "bottomleft", (44, 44), wall9_rect.topleft)
        self.obstacleObjects.append(lv9obstacle10)

        lv9obstacle11 = Obstacle("up", 1, "bottomleft", (44, 44), wall12_rect.topleft)
        self.obstacleObjects.append(lv9obstacle11)

        lv9obstacle12 = Obstacle("up", 1, "bottomleft", (44, 44), lv9obstacle11.rect.bottomright)
        self.obstacleObjects.append(lv9obstacle12)

        lv9obstacle13 = Obstacle("up", 1, "bottomleft", (44, 44), lv9obstacle12.rect.bottomright)
        self.obstacleObjects.append(lv9obstacle13)

        lv9obstacle14 = Obstacle("up", 1, "bottomleft", (44, 44), lv9obstacle13.rect.bottomright)
        self.obstacleObjects.append(lv9obstacle14)

        lv9obstacle15 = Obstacle("up", 1, "bottomleft", (44, 44), lv9obstacle14.rect.bottomright)
        self.obstacleObjects.append(lv9obstacle15)

        lv9obstacle16 = Obstacle("up", 1, "bottomleft", (44, 44), lv9obstacle15.rect.bottomright)
        self.obstacleObjects.append(lv9obstacle16)

        lv9obstacle17 = Obstacle("up", 1, "bottomleft", (44, 44), lv9obstacle16.rect.bottomright)
        self.obstacleObjects.append(lv9obstacle17)

        lv9obstacle18 = Obstacle("left", 2, "topleft", (33, 128), wall7_rect.topleft)
        self.obstacleObjects.append(lv9obstacle18)

        # blocks:
        lv9block1 = pygame.image.load('level2pics/Block.jpg').convert_alpha()
        lv9block1 = pygame.transform.scale(lv9block1, (44, 20))
        lv9block1_rect = lv9block1.get_rect(topleft = (lv9obstacle12.rect.x, wall11_rect[1] + 50))
        self.blocks.append((lv9block1, lv9block1_rect))

        lv9block2 = lv9block1
        lv9block2_rect = lv9block2.get_rect(midleft =lv9block1_rect.midright)
        self.blocks.append((lv9block2, lv9block2_rect))

        lv9block3 = lv9block1
        lv9block3_rect = lv9block3.get_rect(topleft = (lv9obstacle15.rect.x, wall11_rect[1] + 10))
        self.blocks.append((lv9block3, lv9block3_rect))

        lv9block4 = lv9block1
        lv9block4_rect = lv9block4.get_rect(midleft=lv9block3_rect.midright)
        self.blocks.append((lv9block4, lv9block4_rect))

        # Trees:

        tree1 = pygame.image.load('level9pics/Tree.PNG')
        tree1_rect = tree1.get_rect(midbottom = (wall10_rect.midtop[0] + 35, wall10_rect.midtop[1] + 2))
        self.decoration.append((tree1, tree1_rect))

        tree2 = pygame.image.load('level9pics/Tree.PNG')
        tree2_rect = tree2.get_rect(midbottom=(wall10_rect.midtop[0] - 35, wall10_rect.midtop[1]+ 2))
        self.decoration.append((tree2, tree2_rect))

        # apples:
        lv9apple1 = Obstacle("up", 3, "topleft", (28, 31), (tree2_rect.midtop[0] - 25, tree2_rect.midtop[1] + 20))
        self.obstacleObjects.append(lv9apple1)
        self.apples.append(lv9apple1)

        lv9apple2 = Obstacle("up", 3, "midtop", (28, 31), (lv9apple1.rect.midtop[0] + 35, lv9apple1.rect.midtop[1] + 60))
        self.obstacleObjects.append(lv9apple2)
        self.apples.append(lv9apple2)

        lv9apple3 = Obstacle("up", 3, "midtop", (28, 31), (lv9apple1.rect.midtop[0] + 105, lv9apple1.rect.midtop[1] + 10))
        self.obstacleObjects.append(lv9apple3)
        self.apples.append(lv9apple3)


        # warter:
        water_block1 = pygame.image.load('level9pics/water1.jpg')
        water_block1 = pygame.transform.scale(water_block1, (132,130))
        water_block1_rect = water_block1.get_rect(topright = wall3_rect.topleft)
        self.waterBlocks.append((water_block1, water_block1_rect))

        water_block2 = pygame.image.load('level9pics/water2.jpg')
        water_block2 = pygame.transform.scale(water_block2, (88, 132))
        water_block2_rect = water_block2.get_rect(topright=wall5_rect.topleft)
        self.waterBlocks.append((water_block2, water_block2_rect))

        # save positions:

        save1 = SavePosition(980, 330)
        self.saveObjects.append(save1)

        save2 = SavePosition(165, 560)
        self.saveObjects.append(save2)

        # coins:

        if game_over:
            self.coinObjects = []

            coin1 = Coin(852, 324)
            self.coinObjects.append(coin1.coin_rect)

            coin2 = Coin(305, 354)
            self.coinObjects.append(coin2.coin_rect)

            coin3 = Coin(356, 590)
            self.coinObjects.append(coin3.coin_rect)

            coin4 = Coin(896, 542)
            self.coinObjects.append(coin4.coin_rect)

            coin5 = Coin(63, 531)
            self.coinObjects.append(coin5.coin_rect)

            coin6 = Coin(505, 165)
            self.coinObjects.append(coin6.coin_rect)

    def draw(self, screen, player):

        super().draw(screen, player)

        if self.blocks[0][1].colliderect(self.border[7][1]) or self.blocks[0][1].colliderect(self.border[15][1]):
            self.blocks_1_2_moving_direction *= -1
        if abs((player.rect.bottom + player.dy) - self.blocks[0][1].top) < player.col_thresh:
            if self.blocks[0][1].top - 5 <= self.border[7][1].bottom + player.height:
                self.blocks_1_2_moving_direction *= -1

        if self.blocks[3][1].colliderect(self.border[4][1]) or self.blocks[3][1].colliderect(self.border[15][1]):
            self.blocks_3_4_moving_direction *= -1
        if abs((player.rect.bottom + player.dy) - self.blocks[3][1].top) < player.col_thresh:
            if self.blocks[3][1].top - 5 <= self.border[4][1].bottom + player.height:
                self.blocks_3_4_moving_direction *= -1

        for index in range(2):
            self.blocks[index][1][1] += self.blocks_1_2_moving_direction
        for index in range(2,4):
            self.blocks[index][1][1] += self.blocks_3_4_moving_direction


        if player.rect.x <= self.obstacleObjects[2].rect.topright[0] + 15 and player.rect.y < 410:
            self.obstacles_3_4_moving_condition = True
        if self.obstacles_3_4_moving_condition:
            self.obstacleObjects[2].rect.y += 4
            self.obstacleObjects[3].rect.y -= 4

        if player.rect.x <= self.obstacleObjects[8].rect.bottomright[0]:
            self.obstacle18_moving_condition = True
        if self.obstacle18_moving_condition:
            self.obstacleObjects[17].rect.x -= 4





