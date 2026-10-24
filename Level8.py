import pygame

from Coin import Coin
from Level import Level
from Obstacle import Obstacle
from SavePosition import SavePosition


class Level8(Level):
    def __init__(self,game_over):
        self.coinObjects = []
        self.restart(game_over)
        self.obstacle7_moving_condition = False
        self.obstacle12_moving_condition = False
        self.obstacle14_moving_condition = False
        self.obstacle_15_16_moving_direction = 1
        self.obstacle_15_16_moving_limit = 0
        self.obstacle17_moving_condition = False

    def restart(self, game_over):

        super().__init__()

        self.obstacle7_moving_condition = False
        self.obstacle12_moving_condition = False
        self.obstacle14_moving_condition = False
        self.obstacle_15_16_moving_direction = 1
        self.obstacle_15_16_moving_limit = 0
        self.obstacle17_moving_condition = False

        wall_topright = pygame.image.load('level8pics/wall_topright.jpg')
        wall_topright_rect = wall_topright.get_rect(topright=(1100, 0))
        self.border.append((wall_topright, wall_topright_rect))

        wall_topleft = pygame.image.load('level8pics/wall_topleft.jpg')
        wall_topleft_rect = wall_topleft.get_rect(topleft=(0, 0))
        self.border.append((wall_topleft, wall_topleft_rect))

        wall_right = pygame.image.load('level8pics/wall_right.jpg')
        wall_right_rect = wall_right.get_rect(bottomright=(1100, 825))
        self.border.append((wall_right, wall_right_rect))

        wall_bottomleft = pygame.image.load('level8pics/wall_left.jpg')
        wall_bottomleft_rect = wall_bottomleft.get_rect(bottomleft = (0, 825))
        self.border.append((wall_bottomleft, wall_bottomleft_rect))

        wall1 = pygame.image.load('level8pics/wall1.jpg')
        wall1_rect = wall1.get_rect(bottomleft= wall_bottomleft_rect.bottomright)
        self.border.append((wall1, wall1_rect))

        wall2 = pygame.image.load('level8pics/wall2.jpg')
        wall2_rect = wall2.get_rect(bottomleft=wall1_rect.bottomright)
        self.border.append((wall2, wall2_rect))

        wall3 = pygame.image.load('level8pics/wall3.jpg')
        wall3_rect = wall3.get_rect(bottomleft=wall2_rect.bottomright)
        self.border.append((wall3, wall3_rect))

        wall4 = pygame.image.load('level8pics/wall4.jpg')
        wall4_rect = wall4.get_rect(bottomleft=wall3_rect.bottomright)
        self.border.append((wall4, wall4_rect))

        wall5 = pygame.image.load('level8pics/wall5.jpg')
        wall5_rect = wall5.get_rect(bottomleft=wall4_rect.bottomright)
        self.border.append((wall5, wall5_rect))

        wall6 = pygame.image.load('level8pics/wall6.jpg')
        wall6_rect = wall6.get_rect(bottomleft=wall5_rect.bottomright)
        self.border.append((wall6, wall6_rect))

        wall7 = pygame.image.load('level8pics/wall7.jpg')
        wall7_rect = wall7.get_rect(bottomright =wall6_rect.topright)
        self.border.append((wall7, wall7_rect))

        wall8 = pygame.image.load('level8pics/wall8.jpg')
        wall8_rect = wall8.get_rect(bottomleft=wall6_rect.bottomright)
        self.border.append((wall8, wall8_rect))

        wall9 = pygame.image.load('level8pics/wall9.jpg')
        wall9_rect = wall9.get_rect(bottomleft=wall8_rect.bottomright)
        self.border.append((wall9, wall9_rect))

        wall10 = pygame.image.load('level8pics/wall10.jpg')
        wall10_rect = wall10.get_rect(topleft = (575, 565))
        self.border.append((wall10, wall10_rect))

        wall11 = pygame.image.load('level8pics/wall11.jpg')
        wall11_rect = wall11.get_rect(bottomright=wall_topright_rect.bottomleft)
        self.border.append((wall11, wall11_rect))

        wall12 = pygame.image.load('level8pics/wall12.jpg')
        wall12_rect = wall12.get_rect(bottomright=wall11_rect.bottomleft)
        self.border.append((wall12, wall12_rect))

        wall13 = pygame.image.load('level8pics/wall13.jpg')
        wall13_rect = wall13.get_rect(bottomright=wall12_rect.bottomleft)
        self.border.append((wall13, wall13_rect))

        wall14 = pygame.image.load('level8pics/wall14.jpg')
        wall14_rect = wall14.get_rect(bottomright=wall13_rect.bottomleft)
        self.border.append((wall14, wall14_rect))

        wall15 = pygame.image.load('level8pics/wall15.jpg')
        wall15_rect = wall15.get_rect(topright=wall14_rect.bottomright)
        self.border.append((wall15, wall15_rect))

        wall16 = pygame.image.load('level8pics/wall16.jpg')
        wall16_rect = wall16.get_rect(bottomright=wall14_rect.bottomleft)
        self.border.append((wall16, wall16_rect))

        wall17 = pygame.image.load('level8pics/wall17.jpg')
        wall17_rect = wall17.get_rect(topright=wall15_rect.topleft)
        self.border.append((wall17, wall17_rect))

        wall18 = pygame.image.load('level8pics/wall18.jpg')
        wall18_rect = wall18.get_rect(topright=wall17_rect.topleft)
        self.border.append((wall18, wall18_rect))

        wall19 = pygame.image.load('level8pics/wall19.jpg')
        wall19_rect = wall19.get_rect(topright=wall18_rect.topleft)
        self.border.append((wall19, wall19_rect))

        wall20 = pygame.image.load('level8pics/wall20.jpg')
        wall20_rect = wall20.get_rect(bottomright=wall16_rect.bottomleft)
        self.border.append((wall20, wall20_rect))

        # obstacles

        lv8obstacle1 = Obstacle("up", 1, "bottomright", (44, 44), wall13_rect.topright)
        self.obstacleObjects.append(lv8obstacle1)

        lv8obstacle2 = Obstacle("up", 1, "bottomright", (44, 44), lv8obstacle1.rect.bottomleft)
        self.obstacleObjects.append(lv8obstacle2)

        lv8obstacle3 = Obstacle("up", 1, "bottomright", (44, 44), lv8obstacle2.rect.bottomleft)
        self.obstacleObjects.append(lv8obstacle3)

        lv8obstacle4 = Obstacle("up", 1, "bottomright", (44, 44), wall16_rect.topright)
        self.obstacleObjects.append(lv8obstacle4)

        lv8obstacle5 = Obstacle("up", 1, "bottomright", (44, 44), lv8obstacle4.rect.bottomleft)
        self.obstacleObjects.append(lv8obstacle5)

        lv8obstacle6 = Obstacle("up", 1, "bottomright", (44, 44), lv8obstacle5.rect.bottomleft)
        self.obstacleObjects.append(lv8obstacle6)

        lv8obstacle7 = Obstacle("up", 1, "bottomright", (44, 44), wall16_rect.bottomleft)
        self.obstacleObjects.append(lv8obstacle7)

        lv8obstacle8 = Obstacle("down", 1, "topright", (44, 44), wall20_rect.bottomright)
        self.obstacleObjects.append(lv8obstacle8)

        lv8obstacle9 = Obstacle("down", 1, "topright", (44, 44), wall19_rect.bottomright)
        self.obstacleObjects.append(lv8obstacle9)

        lv8obstacle10 = Obstacle("down", 1, "topright", (44, 44), wall18_rect.bottomright)
        self.obstacleObjects.append(lv8obstacle10)

        lv8obstacle11 = Obstacle("down", 1, "topright", (44, 44), wall17_rect.bottomright)
        self.obstacleObjects.append(lv8obstacle11)

        lv8obstacle12 = Obstacle("down", 1, "topright", (44, 44), wall15_rect.bottomright)
        self.obstacleObjects.append(lv8obstacle12)

        lv8obstacle13 = Obstacle("left", 1, "topright", (44, 44), wall6_rect.topleft)
        self.obstacleObjects.append(lv8obstacle13)

        lv8obstacle14 = Obstacle("up", 2, "midtop", (33, 128), (wall10_rect.midtop[0], wall10_rect.midtop[1] + 44))
        self.obstacleObjects.append(lv8obstacle14)

        lv8obstacle15 = Obstacle("up", 1, "bottomleft", (44, 44), (wall9_rect.midtop[0] + 4, wall9_rect.midtop[1]))
        self.obstacleObjects.append(lv8obstacle15)

        lv8obstacle16 = Obstacle("up", 1, "bottomright", (44, 44), (wall9_rect.midtop[0] - 4, wall9_rect.midtop[1]))
        self.obstacleObjects.append(lv8obstacle16)

        lv8obstacle17 = Obstacle("up", 2, "topright", (33, 128), (1090,830))
        self.obstacleObjects.append(lv8obstacle17)

        # save positions:

        save1 = SavePosition(540, 205)
        self.saveObjects.append(save1)

        save2 = SavePosition(455, 635)
        self.saveObjects.append(save2)

        # coins:

        if game_over:
            self.coinObjects = []

            coin1 = Coin(153, 624)
            self.coinObjects.append(coin1.coin_rect)

            coin2 = Coin(637, 767)
            self.coinObjects.append(coin2.coin_rect)

            coin3 = Coin(1006, 531)
            self.coinObjects.append(coin3.coin_rect)

            coin4 = Coin(635, 500)
            self.coinObjects.append(coin4.coin_rect)

            coin5 = Coin(284, 769)
            self.coinObjects.append(coin5.coin_rect)

            coin6 = Coin(284, 188)
            self.coinObjects.append(coin6.coin_rect)


    def draw(self, screen, player):

        super().draw(screen, player)

        if player.rect.x <= self.obstacleObjects[4].rect.x:
            self.obstacle7_moving_condition = True
        if self.obstacle7_moving_condition:
            if self.obstacleObjects[6].rect.midbottom[1] > self.border[-1][1].midtop[1]:
                self.obstacleObjects[6].rect.y -= 4

        if self.border[18][1].bottomleft[0] + 20 >= player.rect.x >= self.border[18][1].bottomleft[0] - 10 and player.rect.y > 750:
            self.obstacle12_moving_condition = True
        if self.obstacle12_moving_condition:
            self.obstacleObjects[11].rect.y += 4

        if player.rect.x > self.border[13][1][0] - 5 and self.border[13][1][1] > player.rect.y > self.border[14][1].midbottom[1]:
            self.obstacle14_moving_condition = True
        if self.obstacle14_moving_condition:
            self.obstacleObjects[13].rect.y -= 4

        if self.obstacle_15_16_moving_limit == 40:
            self.obstacle_15_16_moving_direction *= -1
            self.obstacle_15_16_moving_limit = 0
        self.obstacle_15_16_moving_limit += 1
        self.obstacleObjects[14].rect.y += self.obstacle_15_16_moving_direction
        self.obstacleObjects[15].rect.y += self.obstacle_15_16_moving_direction

        if player.rect.x >= self.border[12][1].topright[0] and player.rect.y >= self.border[12][1][1] + 5:
            self.obstacle17_moving_condition = True
        if self.obstacle17_moving_condition:
            self.obstacleObjects[16].rect.y -= 10


