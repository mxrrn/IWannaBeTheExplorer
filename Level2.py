import pygame

from Coin import Coin
from Level import Level
from Obstacle import Obstacle
from SavePosition import SavePosition


class Level2(Level):
    def __init__(self,game_over):
        self.coinObjects = []
        self.restart(game_over)
        self.obstacle5_moving_condition = False
        self.obstacle6_moving_condition = False

    def restart(self, game_over):

        super().__init__()


        self.obstacle5_moving_condition = False
        self.obstacle6_moving_condition = False


        wall_left1 = pygame.image.load('level2pics/wall_left1.jpg')
        wall_left1_rect = wall_left1.get_rect(topleft = (0,0))
        self.border.append((wall_left1, wall_left1_rect))

        wall_left2 = pygame.image.load('level2pics/wall_left2.jpg')
        wall_left2_rect = wall_left2.get_rect(bottomleft= (0, 825))
        self.border.append((wall_left2, wall_left2_rect))

        wall_right = pygame.image.load('level2pics/wall_right.jpg')
        wall_right_rect = wall_right.get_rect(bottomright = (1100, 825))
        self.border.append((wall_right, wall_right_rect))

        wall_up = pygame.image.load('level2pics/wall_up.jpg')
        wall_up_rect = wall_up.get_rect(topright = (1100, 0))
        self.border.append((wall_up, wall_up_rect))

        wall1 = pygame.image.load('level2pics/wall1.jpg')
        wall1_rect = wall1.get_rect(bottomright = wall_right_rect.bottomleft)
        self.border.append((wall1, wall1_rect))

        wall2 = pygame.image.load('level2pics/wall2.jpg')
        wall2_rect = wall2.get_rect(bottomright = wall1_rect.bottomleft)
        self.border.append((wall2, wall2_rect))

        wall3 = pygame.image.load('level2pics/wall3.jpg')
        wall3_rect = wall3.get_rect(bottomright=wall2_rect.bottomleft)
        self.border.append((wall3, wall3_rect))

        wall4 = pygame.image.load('level2pics/wall4_6_8_10.jpg')
        wall4_rect = wall4.get_rect(bottomright=wall3_rect.bottomleft)
        self.border.append((wall4, wall4_rect))

        wall5 = pygame.image.load('level2pics/wall5.jpg')
        wall5_rect = wall5.get_rect(bottomright=wall4_rect.bottomleft)
        self.border.append((wall5, wall5_rect))

        wall6 = wall4
        wall6_rect = wall6.get_rect(bottomright = wall5_rect.bottomleft)
        self.border.append((wall6, wall6_rect))

        wall7 = pygame.image.load('level2pics/wall7.jpg')
        wall7_rect = wall7.get_rect(bottomright=wall6_rect.bottomleft)
        self.border.append((wall7, wall7_rect))

        wall8 = wall4
        wall8_rect = wall8.get_rect(bottomright=wall7_rect.bottomleft)
        self.border.append((wall8, wall8_rect))

        wall9 = pygame.image.load('level2pics/wall9.jpg')
        wall9_rect = wall9.get_rect(bottomright=wall8_rect.bottomleft)
        self.border.append((wall9, wall9_rect))

        wall10 = wall4
        wall10_rect = wall10.get_rect(bottomright=wall9_rect.bottomleft)
        self.border.append((wall10, wall10_rect))

        wall11 = pygame.image.load('level2pics/wall11.jpg')
        wall11_rect = wall11.get_rect(bottomright=wall10_rect.bottomleft)
        self.border.append((wall11, wall11_rect))

        wall12 = pygame.image.load('level2pics/wall12.jpg')
        wall12_rect = wall12.get_rect(bottomleft = wall_left1_rect.bottomright)
        self.border.append((wall12, wall12_rect))

        wall13 = pygame.image.load('level2pics/wall13.jpg')
        wall13_rect = wall13.get_rect(bottomleft=wall12_rect.bottomright)
        self.border.append((wall13, wall13_rect))

        wall14 = pygame.image.load('level2pics/wall14.jpg')
        wall14_rect = wall14.get_rect(bottomleft=wall13_rect.bottomright)
        self.border.append((wall14, wall14_rect))

        wall15 = pygame.image.load('level2pics/wall15.jpg')
        wall15_rect = wall15.get_rect(bottomleft=wall14_rect.bottomright)
        self.border.append((wall15, wall15_rect))

        wall16 = pygame.image.load('level2pics/wall16.jpg')
        wall16_rect = wall16.get_rect(bottomleft=wall15_rect.bottomright)
        self.border.append((wall16, wall16_rect))

        wall17 = pygame.image.load('level2pics/wall17.jpg')
        wall17_rect = wall17.get_rect(bottomleft=wall16_rect.bottomright)
        self.border.append((wall17, wall17_rect))


        #obstacles:

        lv2obstacle1 = Obstacle("up", 1, "bottomleft", (44, 44), wall14_rect.topleft)
        self.obstacleObjects.append(lv2obstacle1)

        lv2obstacle2 = Obstacle("up", 1, "bottomleft", (44, 44), lv2obstacle1.rect.bottomright)
        self.obstacleObjects.append(lv2obstacle2)

        lv2obstacle3 = Obstacle("up", 1, "bottomleft", (44, 44), lv2obstacle2.rect.bottomright)
        self.obstacleObjects.append(lv2obstacle3)

        lv2obstacle4 = Obstacle("up", 1, "bottomleft", (44, 44), lv2obstacle3.rect.bottomright)
        self.obstacleObjects.append(lv2obstacle4)

        lv2obstacle5 = Obstacle("up", 1, "bottomleft", (44, 44), lv2obstacle4.rect.bottomright)
        self.obstacleObjects.append(lv2obstacle5)

        lv2obstacle6 = Obstacle("up", 1, "bottomright", (44, 44), wall15_rect.topright)
        self.obstacleObjects.append(lv2obstacle6)

        lv2obstacle7 = Obstacle("up", 1, "bottomleft", (44, 44), wall17_rect.topleft)
        self.obstacleObjects.append(lv2obstacle7)

        lv2obstacle8 = Obstacle("up", 1, "bottomright", (44, 44), wall2_rect.topright)
        self.obstacleObjects.append(lv2obstacle8)

        lv2obstacle9 = Obstacle("up", 1, "bottomleft", (44, 44), wall2_rect.topleft)
        self.obstacleObjects.append(lv2obstacle9)

        lv2obstacle10 = Obstacle("up", 1, "bottomright", (44, 44), wall4_rect.topright)
        self.obstacleObjects.append(lv2obstacle10)

        lv2obstacle11 = Obstacle("up", 1, "bottomright", (44, 44), wall5_rect.topright)
        self.obstacleObjects.append(lv2obstacle11)

        lv2obstacle12 = Obstacle("up", 1, "bottomleft", (44, 44), wall5_rect.topleft)
        self.obstacleObjects.append(lv2obstacle12)

        lv2obstacle13 = Obstacle("up", 1, "bottomleft", (44, 44), wall6_rect.topleft)
        self.obstacleObjects.append(lv2obstacle13)

        lv2obstacle14 = Obstacle("up", 1, "bottomleft", (44, 44), wall10_rect.topleft)
        self.obstacleObjects.append(lv2obstacle14)

        # Blocks:
        lv2block1 = pygame.image.load('level2pics/Block.jpg').convert_alpha()
        lv2block1 = pygame.transform.scale(lv2block1, (44,20))
        lv2block1_rect = lv2block1.get_rect(bottomleft = lv2obstacle1.rect.topleft)
        #self.border.append((lv2block1, lv2block1_rect))
        self.blocks.append((lv2block1, lv2block1_rect))

        lv2block2 = lv2block1
        lv2block2_rect = lv2block2.get_rect(bottomleft = lv2block1_rect.bottomright)
        self.blocks.append((lv2block2, lv2block2_rect))

        lv2block3 = lv2block1
        lv2block3_rect = lv2block3.get_rect(bottomleft = lv2block2_rect.bottomright)
        self.blocks.append((lv2block3, lv2block3_rect))

        lv2block4 = lv2block1
        lv2block4_rect = lv2block4.get_rect(bottomleft = lv2block3_rect.bottomright)
        self.blocks.append((lv2block4, lv2block4_rect))

        lv2block5 = lv2block1
        lv2block5_rect = lv2block5.get_rect(bottomleft=lv2block4_rect.bottomright)
        self.blocks.append((lv2block5, lv2block5_rect))

        lv2block6 = lv2block1
        lv2block6_rect = lv2block6.get_rect(topleft = (wall14_rect.x, wall14_rect.y +225))
        self.blocks.append((lv2block6, lv2block6_rect))

        save1 = SavePosition(88, 150)
        self.saveObjects.append(save1)

        save2 = SavePosition(1000, 400)
        self.saveObjects.append(save2)

        # coins:

        if game_over:

            self.coinObjects = []

            coin1 = Coin(218, 100)
            self.coinObjects.append(coin1.coin_rect)

            coin2 = Coin(448, 120)
            self.coinObjects.append(coin2.coin_rect)

            coin3 = Coin(977, 264)
            self.coinObjects.append(coin3.coin_rect)

            coin4 = Coin(832, 572)
            self.coinObjects.append(coin4.coin_rect)

            coin5 = Coin(274, 750)
            self.coinObjects.append(coin5.coin_rect)

            coin6 = Coin(154, 352)
            self.coinObjects.append(coin6.coin_rect)


    def draw(self, screen, player):

        super().draw(screen, player)

        # moving obstacles on certain conditions
        if player.alive:            # so that when the player is dead nothing will be moving on the screen
            if player.rect.x >= self.obstacleObjects[4].rect.x and player.rect.y <= self.obstacleObjects[4].rect.y:
                self.obstacle5_moving_condition = True
            if self.obstacle5_moving_condition:         # once the condition is fullfilled, the obstacle will be moved in each iteration
                self.obstacleObjects[4].rect.y -= 8

            if self.border[19][1].colliderect((player.rect.x, player.rect.y + player.dy, player.width, player.height)):
                self.obstacle6_moving_condition = True
            if self.obstacle6_moving_condition:
                self.obstacleObjects[5].rect.x += 4
