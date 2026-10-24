import pygame

from Coin import Coin
from Level import Level
from Obstacle import Obstacle
from SavePosition import SavePosition


class Level11(Level):

    def __init__(self,game_over):
        self.coinObjects = []
        self.restart(game_over)
        self.obstacle28_moving_condition = False
        self.obstacle29_moving_condition = False


    def restart(self, game_over):

        super().__init__()

        self.obstacle28_moving_condition = False
        self.obstacle29_moving_condition = False

        wall_left = pygame.image.load('level11pics/wall_left.jpg')
        wall_left_rect = wall_left.get_rect(bottomleft=(0, 825))
        self.border.append((wall_left, wall_left_rect))

        wall_up1 = pygame.image.load('level11pics/wall_up1.jpg')
        wall_up1_rect = wall_up1.get_rect(topleft=(0, 0))
        self.border.append((wall_up1, wall_up1_rect))

        wall1 = pygame.image.load('level11pics/wall1.jpg')
        wall1_rect = wall1.get_rect(topright= wall_up1_rect.topright)
        self.border.append((wall1, wall1_rect))

        wall2 = pygame.image.load('level11pics/wall2.jpg')
        wall2_rect = wall2.get_rect(bottomleft=wall1_rect.bottomright)
        self.border.append((wall2, wall2_rect))

        wall3 = pygame.image.load('level11pics/wall3.jpg')
        wall3_rect = wall3.get_rect(topleft =(wall2_rect.topright[0],wall2_rect.topright[1] - 44))
        self.border.append((wall3, wall3_rect))

        wall_right1 = pygame.image.load('level11pics/wall_right1.jpg')
        wall_right1_rect = wall_right1.get_rect(bottomright = (1100, 825))
        self.border.append((wall_right1, wall_right1_rect))

        wall_right2 = pygame.image.load('level11pics/wall_right2.jpg')
        wall_right2_rect = wall_right2.get_rect(bottomright=wall_right1_rect.topright)
        self.border.append((wall_right2, wall_right2_rect))

        wall_right3 = pygame.image.load('level11pics/wall_right3.jpg')
        wall_right3_rect = wall_right3.get_rect(bottomright=wall_right2_rect.topright)
        self.border.append((wall_right3, wall_right3_rect))

        wall_right4 = pygame.image.load('level11pics/wall_right4.jpg')
        wall_right4_rect = wall_right4.get_rect(bottomright=wall_right3_rect.topright)
        self.border.append((wall_right4, wall_right4_rect))

        wall_right5 = pygame.image.load('level11pics/wall_right5.jpg')
        wall_right5_rect = wall_right5.get_rect(bottomright=wall_right4_rect.topright)
        self.border.append((wall_right5, wall_right5_rect))

        wall_right6 = pygame.image.load('level11pics/wall_right6.jpg')
        wall_right6 = pygame.transform.scale(wall_right6, (350, 47))
        wall_right6_rect = wall_right6.get_rect(bottomright=wall_right5_rect.topright)
        self.border.append((wall_right6, wall_right6_rect))

        wall4 = pygame.image.load('level11pics/wall4.jpg')
        wall4_rect = wall4.get_rect(bottomright = wall_right1_rect.bottomleft)
        self.border.append((wall4, wall4_rect))

        wall5 = pygame.image.load('level11pics/wall5.jpg')
        wall5_rect = wall5.get_rect(bottomright=wall4_rect.bottomleft)
        self.border.append((wall5, wall5_rect))

        wall6 = pygame.image.load('level11pics/wall6.jpg')
        wall6_rect = wall6.get_rect(bottomright=wall5_rect.bottomleft)
        self.border.append((wall6, wall6_rect))

        wall7 = pygame.image.load('level11pics/wall7.jpg')
        wall7_rect = wall7.get_rect(bottomright=wall6_rect.bottomleft)
        self.border.append((wall7, wall7_rect))

        wall8 = wall5
        wall8_rect = wall8.get_rect(bottomright=wall7_rect.bottomleft)
        self.border.append((wall8, wall8_rect))

        wall9 = pygame.image.load('level11pics/wall9.jpg')
        wall9_rect = wall9.get_rect(bottomright=wall8_rect.bottomleft)
        self.border.append((wall9, wall9_rect))

        wall10 = pygame.image.load('level11pics/wall10.jpg')
        wall10_rect = wall10.get_rect(bottomright=wall9_rect.topright)
        self.border.append((wall10, wall10_rect))

        wall11 = pygame.image.load('level11pics/wall11.jpg')
        wall11_rect = wall11.get_rect(bottomright=wall10_rect.topright)
        self.border.append((wall11, wall11_rect))

        wall12 = pygame.image.load('level11pics/wall12.jpg')
        wall12_rect = wall12.get_rect(bottomleft=wall10_rect.topleft)
        self.border.append((wall12, wall12_rect))

        wall13 = pygame.image.load('level11pics/wall13.jpg')
        wall13_rect = wall13.get_rect(bottomleft=wall_left_rect.bottomright)
        self.border.append((wall13, wall13_rect))

        # obstacles:

        lv11obstacle1 = Obstacle("up", 1, "midbottom", (44, 44), wall3_rect.midtop)
        self.obstacleObjects.append(lv11obstacle1)

        lv11obstacle2 = Obstacle("right", 1, "topleft", (44, 44), wall3_rect.topright)
        self.obstacleObjects.append(lv11obstacle2)

        lv11obstacle3 = Obstacle("right", 1, "topleft", (44, 44), lv11obstacle2.rect.bottomleft)
        self.obstacleObjects.append(lv11obstacle3)

        lv11obstacle4 = Obstacle("left", 1, "topright", (44, 44), wall_right2_rect.topleft)
        self.obstacleObjects.append(lv11obstacle4)

        lv11obstacle5 = Obstacle("left", 1, "bottomright", (44, 44), wall_right2_rect.bottomleft)
        self.obstacleObjects.append(lv11obstacle5)

        lv11obstacle6 = Obstacle("left", 1, "bottomright", (44, 44), wall3_rect.bottomleft)
        self.obstacleObjects.append(lv11obstacle6)

        lv11obstacle7 = Obstacle("left", 1, "topright", (44, 44), wall2_rect.bottomright)
        self.obstacleObjects.append(lv11obstacle7)

        lv11obstacle8 = Obstacle("up", 1, "bottomleft", (44, 44), wall4_rect.topleft)
        self.obstacleObjects.append(lv11obstacle8)

        lv11obstacle9 = Obstacle("up", 1, "bottomleft", (44, 44), lv11obstacle8.rect.bottomright)
        self.obstacleObjects.append(lv11obstacle9)

        lv11obstacle10 = Obstacle("up", 1, "midbottom", (44, 44), wall8_rect.midtop)
        self.obstacleObjects.append(lv11obstacle10)

        lv11obstacle11 = Obstacle("up", 1, "bottomleft", (44, 44), wall12_rect.bottomright)
        self.obstacleObjects.append(lv11obstacle11)

        lv11obstacle12 = Obstacle("up", 1, "bottomright",(44, 44),  wall11_rect.bottomleft)
        self.obstacleObjects.append(lv11obstacle12)

        lv11obstacle13 = Obstacle("up", 1, "bottomleft", (44, 44), (wall12_rect.x, wall13_rect.y))
        self.obstacleObjects.append(lv11obstacle13)

        lv11obstacle14 = Obstacle("up", 1, "bottomleft", (44, 44), lv11obstacle13.rect.bottomright)
        self.obstacleObjects.append(lv11obstacle14)

        for i in range(1,14):
            obstacle = Obstacle("down", 1, "topleft", (44, 44), (i * 44, 44))
            self.obstacleObjects.append(obstacle)

        lv11obstacle28 = Obstacle("left", 2, "topleft", (33, 128), (wall_right1_rect.x,wall_right1_rect.y + 6) )
        self.obstacleObjects.append(lv11obstacle28)

        lv11obstacle29 = Obstacle("left", 2, "topleft", (33, 128), (wall9_rect.x, wall9_rect.y + 6))
        self.obstacleObjects.append(lv11obstacle29)

        # save position:

        save1 = SavePosition(704, 220)
        self.saveObjects.append(save1)

        # coins:

        if game_over:
            self.coinObjects = []

            coin1 = Coin(898, 264)
            self.coinObjects.append(coin1.coin_rect)

            coin2 = Coin(240, 200)
            self.coinObjects.append(coin2.coin_rect)

            coin3 = Coin(460, 200)
            self.coinObjects.append(coin3.coin_rect)

            coin4 = Coin(130, 474)
            self.coinObjects.append(coin4.coin_rect)

            coin5 = Coin(55, 540)
            self.coinObjects.append(coin5.coin_rect)

            coin6 = Coin(850, 414)
            self.coinObjects.append(coin6.coin_rect)


    def draw(self, screen, player):

        super().draw(screen, player)

        if self.border[11][1].colliderect((player.rect.x, player.rect.y + player.dy, player.width, player.height)):
            self.obstacle28_moving_condition = True
        if self.obstacle28_moving_condition:
            self.obstacleObjects[27].rect.x -= 4

        if self.border[-1][1].colliderect((player.rect.x, player.rect.y + player.dy, player.width, player.height)):
            self.obstacle29_moving_condition = True
        if self.obstacle29_moving_condition:
            if self.obstacleObjects[-1].rect.x > self.obstacleObjects[12].rect.bottomright[0]:
                self.obstacleObjects[-1].rect.x -= 2
            else:
                self.obstacleObjects[-1].rect.x -= 6