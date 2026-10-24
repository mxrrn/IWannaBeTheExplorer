import pygame

from Coin import Coin
from Level import Level
from Obstacle import Obstacle
from SavePosition import SavePosition


class Level10(Level):
    def __init__(self,game_over):
        self.coinObjects = []
        self.restart(game_over)
        self.obstacle7_moving_condition = False
        self.obstacle_31_32_33_moving_condition = False

    def restart(self, game_over):

        super().__init__()

        self.obstacle7_moving_condition = False
        self.obstacle_31_32_33_moving_condition = False

        wall_right = pygame.image.load('level10pics/wall_right.jpg')
        wall_right_rect = wall_right.get_rect(bottomright=(1100, 825))
        self.border.append((wall_right, wall_right_rect))

        wall_left = pygame.image.load('level10pics/wall_left.jpg')
        wall_left_rect = wall_left.get_rect(bottomleft=(0, 825))
        self.border.append((wall_left, wall_left_rect))

        wall1 = pygame.image.load('level10pics/wall1.jpg')
        wall1_rect = wall1.get_rect(bottomright = wall_right_rect.bottomleft)
        self.border.append((wall1, wall1_rect))

        wall2 = pygame.image.load('level10pics/wall2.jpg')
        wall2_rect = wall2.get_rect(bottomright=wall1_rect.bottomleft)
        self.border.append((wall2, wall2_rect))

        wall3 = pygame.image.load('level10pics/wall3.jpg')
        wall3_rect = wall3.get_rect(bottomright=wall2_rect.bottomleft)
        self.border.append((wall3, wall3_rect))

        wall4 = pygame.image.load('level10pics/wall4.jpg')
        wall4_rect = wall4.get_rect(topright=wall1_rect.topleft)
        self.border.append((wall4, wall4_rect))

        wall5 = pygame.image.load('level10pics/wall5.jpg')
        wall5_rect = wall5.get_rect(bottomright=wall4_rect.bottomleft)
        self.border.append((wall5, wall5_rect))

        wall6 = pygame.image.load('level10pics/wall6.jpg')
        wall6_rect = wall6.get_rect(bottomright=wall5_rect.bottomleft)
        self.border.append((wall6, wall6_rect))

        wall7 = pygame.image.load('level10pics/wall7.jpg')
        wall7_rect = wall7.get_rect(bottomright=wall6_rect.bottomleft)
        self.border.append((wall7, wall7_rect))

        wall8 = pygame.image.load('level10pics/wall8.jpg')
        wall8_rect = wall8.get_rect(bottomright=wall7_rect.bottomleft)
        self.border.append((wall8, wall8_rect))

        wall9 = pygame.image.load('level10pics/wall9.jpg')
        wall9_rect = wall9.get_rect(bottomleft =wall_left_rect.bottomright)
        self.border.append((wall9, wall9_rect))

        wall10 = pygame.image.load('level10pics/wall_10_16.jpg')
        wall10_rect = wall10.get_rect(bottomleft=wall9_rect.bottomright)
        self.border.append((wall10, wall10_rect))

        wall11 = pygame.image.load('level10pics/wall_11_13_15.jpg')
        wall11_rect = wall11.get_rect(bottomleft=wall10_rect.bottomright)
        self.border.append((wall11, wall11_rect))

        wall12 = pygame.image.load('level10pics/wall_12_14.jpg')
        wall12_rect = wall12.get_rect(bottomleft=wall11_rect.bottomright)
        self.border.append((wall12, wall12_rect))

        wall13 = wall11
        wall13_rect = wall13.get_rect(bottomleft=wall12_rect.bottomright)
        self.border.append((wall13, wall13_rect))

        wall14 = wall12
        wall14_rect = wall14.get_rect(bottomleft=wall13_rect.bottomright)
        self.border.append((wall14, wall14_rect))

        wall15 = wall11
        wall15_rect = wall15.get_rect(bottomleft=wall14_rect.bottomright)
        self.border.append((wall15, wall15_rect))

        wall16 = wall10
        wall16_rect = wall16.get_rect(bottomleft=wall15_rect.bottomright)
        self.border.append((wall16, wall16_rect))

        wall_up1 = pygame.image.load('level10pics/wall_up1.jpg')
        wall_up1_rect = wall_up1.get_rect(topleft=(0, 0))
        self.border.append((wall_up1, wall_up1_rect))

        wall_up2 = pygame.image.load('level10pics/wall_up2.jpg')
        wall_up2_rect = wall_up2.get_rect(topleft= wall_up1_rect.topright)
        self.border.append((wall_up2, wall_up2_rect))

        wall_up3 = pygame.image.load('level10pics/wall_up3.jpg')
        wall_up3_rect = wall_up3.get_rect(topleft= wall_up2_rect.topright)
        self.border.append((wall_up3, wall_up3_rect))

        wall_up4 = pygame.image.load('level10pics/wall_up4.jpg')
        wall_up4_rect = wall_up4.get_rect(topleft= wall_up3_rect.topright)
        self.border.append((wall_up4, wall_up4_rect))

        wall_up5 = pygame.image.load('level10pics/wall_up5.jpg')
        wall_up5_rect = wall_up5.get_rect(topleft= wall_up4_rect.topright)
        self.border.append((wall_up5, wall_up5_rect))

        wall_up6 = pygame.image.load('level10pics/wall_up6.jpg')
        wall_up6_rect = wall_up6.get_rect(topleft= wall_up5_rect.topright)
        self.border.append((wall_up6, wall_up6_rect))

        wall17 = pygame.image.load('level10pics/wall17.jpg')
        wall17_rect = wall17.get_rect(bottomleft=wall_up5_rect.bottomright)
        self.border.append((wall17, wall17_rect))

        wall18 = pygame.image.load('level10pics/wall18.jpg')
        wall18_rect = wall18.get_rect(bottomleft=wall_up3_rect.bottomright)
        self.border.append((wall18, wall18_rect))

        wall19 = wall18
        wall19_rect = wall19.get_rect(topleft = (wall18_rect.x + 396, wall18_rect.y))
        self.border.append((wall19, wall19_rect))

        # blocks:

        for i in range (1,9):
            block = pygame.image.load('level2pics/Block.jpg').convert_alpha()
            block = pygame.transform.scale(block, (44, 20))
            block_rect = block.get_rect(topleft= (wall18_rect.x + i*44, wall18_rect.y))
            self.blocks.append((block, block_rect))

        # obstacles

        lv10obstacle1 = Obstacle("up", 1, "bottomleft", (44, 44), wall4_rect.topleft)
        self.obstacleObjects.append(lv10obstacle1)

        lv10obstacle2 = Obstacle("up", 1, "bottomleft", (44, 44), lv10obstacle1.rect.bottomright)
        self.obstacleObjects.append(lv10obstacle2)

        lv10obstacle3 = Obstacle("up", 1, "bottomright", (44, 44), (wall6_rect.topright[0] - 44, wall6_rect.topright[1]))
        self.obstacleObjects.append(lv10obstacle3)

        lv10obstacle4 = Obstacle("up", 1, "bottomright", (44, 44), (wall6_rect.topright[0] - 184, wall6_rect.topright[1]))
        self.obstacleObjects.append(lv10obstacle4)

        lv10obstacle5 = Obstacle("up", 1, "bottomleft", (44, 44), (wall6_rect.topleft[0] + 88, wall6_rect.topleft[1]))
        self.obstacleObjects.append(lv10obstacle5)

        lv10obstacle6 = Obstacle("up", 1, "bottomleft", (44, 44), (wall6_rect.topleft[0] + 132, wall6_rect.topleft[1]))
        self.obstacleObjects.append(lv10obstacle6)

        lv10obstacle7 = Obstacle("up", 1, "bottomleft", (44, 44), wall7_rect.topleft)
        self.obstacleObjects.append(lv10obstacle7)

        lv10obstacle8 = Obstacle("up", 1, "bottomleft", (44, 44), lv10obstacle7.rect.bottomright)
        self.obstacleObjects.append(lv10obstacle8)

        lv10obstacle9 = Obstacle("up", 1, "bottomleft", (44, 44), lv10obstacle8.rect.bottomright)
        self.obstacleObjects.append(lv10obstacle9)

        lv10obstacle10 = Obstacle("down", 1, "topleft", (44, 44), wall_up2_rect.bottomleft)
        self.obstacleObjects.append(lv10obstacle10)

        lv10obstacle11 = Obstacle("down", 1, "topleft", (44, 44), lv10obstacle10.rect.topright)
        self.obstacleObjects.append(lv10obstacle11)

        lv10obstacle12 = Obstacle("down", 1, "topleft", (44, 44), lv10obstacle11.rect.topright)
        self.obstacleObjects.append(lv10obstacle12)

        lv10obstacle13 = Obstacle("up", 1, "bottomleft", (44, 44), wall9_rect.topleft)
        self.obstacleObjects.append(lv10obstacle13)

        lv10obstacle14 = Obstacle("up", 1, "bottomleft", (44, 44), wall11_rect.topleft)
        self.obstacleObjects.append(lv10obstacle14)

        lv10obstacle15 = Obstacle("up", 1, "bottomleft", (44, 44), lv10obstacle14.rect.bottomright)
        self.obstacleObjects.append(lv10obstacle15)

        lv10obstacle16 = Obstacle("up", 1, "bottomleft", (44, 44), lv10obstacle15.rect.bottomright)
        self.obstacleObjects.append(lv10obstacle16)

        lv10obstacle17 = Obstacle("up", 1, "bottomleft", (44, 44), wall13_rect.topleft)
        self.obstacleObjects.append(lv10obstacle17)

        lv10obstacle18 = Obstacle("up", 1, "bottomleft", (44, 44), lv10obstacle17.rect.bottomright)
        self.obstacleObjects.append(lv10obstacle18)

        lv10obstacle19 = Obstacle("up", 1, "bottomleft", (44, 44), lv10obstacle18.rect.bottomright)
        self.obstacleObjects.append(lv10obstacle19)

        lv10obstacle20 = Obstacle("up", 1, "bottomleft", (44, 44), wall15_rect.topleft)
        self.obstacleObjects.append(lv10obstacle20)

        lv10obstacle21 = Obstacle("up", 1, "bottomleft", (44, 44), lv10obstacle20.rect.bottomright)
        self.obstacleObjects.append(lv10obstacle21)

        lv10obstacle22 = Obstacle("up", 1, "bottomleft", (44, 44), lv10obstacle21.rect.bottomright)
        self.obstacleObjects.append(lv10obstacle22)

        for i in range(11):
            obstacle = Obstacle("down", 1, "topleft", (44, 44), (wall7_rect.bottomleft[0] + i*44, wall7_rect.bottomleft[1]))
            self.obstacleObjects.append(obstacle)


        # save positions:

        save1 = SavePosition(893, 162)
        self.saveObjects.append(save1)

        save2 = SavePosition(850, 515)
        self.saveObjects.append(save2)

        # coins:

        if game_over:
            self.coinObjects = []

            coin1 = Coin(366, 95)
            self.coinObjects.append(coin1.coin_rect)

            coin2 = Coin(62, 282)
            self.coinObjects.append(coin2.coin_rect)

            coin3 = Coin(62, 565)
            self.coinObjects.append(coin3.coin_rect)

            coin4 = Coin(192, 620)
            self.coinObjects.append(coin4.coin_rect)

            coin5 = Coin(365, 643)
            self.coinObjects.append(coin5.coin_rect)

            coin6 = Coin(546, 620)
            self.coinObjects.append(coin6.coin_rect)


    def draw(self, screen, player):

        super().draw(screen, player)

        if player.rect.topright[0] <= self.border[9][1][0]:
            self.obstacle7_moving_condition = True
        if self.obstacle7_moving_condition:
            self.obstacleObjects[6].rect.x -= 5

        if 620 > player.rect.x >= self.border[15][1].midtop[0] and player.rect.y >= self.obstacleObjects[-1].rect.y:
            self.obstacle_31_32_33_moving_condition = True
        if self.obstacle_31_32_33_moving_condition:
            self.obstacleObjects[30].rect.y += 8
            self.obstacleObjects[31].rect.y += 8
            self.obstacleObjects[32].rect.y += 8



