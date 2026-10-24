import pygame

from Coin import Coin
from Level import Level
from Obstacle import Obstacle
from SavePosition import SavePosition


class Level4(Level):
    def __init__(self,game_over):
        self.coinObjects = []
        self.restart(game_over)

    def restart(self, game_over):

        super().__init__()

        wall_up = pygame.image.load('level4pics/wall_up.jpg')
        wall_up_rect = wall_up.get_rect(topleft = (0, 0))
        self.border.append((wall_up, wall_up_rect))

        wall_right = pygame.image.load('level4pics/wall_right.jpg')
        wall_right_rect = wall_right.get_rect(bottomright = (1100, 825))
        self.border.append((wall_right, wall_right_rect))

        wall_left = pygame.image.load('level4pics/wall_left.jpg')
        wall_left_rect = wall_left.get_rect(bottomleft = (0, 825))
        self.border.append((wall_left, wall_left_rect))

        wall1 = pygame.image.load('level4pics/wall1.jpg')
        wall1_rect = wall1.get_rect(bottomright = wall_right_rect.bottomleft)
        self.border.append((wall1, wall1_rect))

        wall2 = pygame.image.load('level4pics/wall2.jpg')
        wall2_rect = wall2.get_rect(bottomright = wall1_rect.bottomleft)
        self.border.append((wall2, wall2_rect))

        wall3 = pygame.image.load('level4pics/wall3.jpg')
        wall3_rect = wall3.get_rect(bottomright = wall2_rect.bottomleft)
        self.border.append((wall3, wall3_rect))

        wall4 = pygame.image.load('level4pics/wall4.jpg')
        wall4_rect = wall4.get_rect(bottomright = wall3_rect.bottomleft)
        self.border.append((wall4, wall4_rect))

        wall5 = wall1
        wall5_rect = wall5.get_rect(bottomleft = wall_left_rect.bottomright)
        self.border.append((wall5, wall5_rect))

        wall6 = wall2
        wall6_rect = wall6.get_rect(bottomleft = wall5_rect.bottomright)
        self.border.append((wall6, wall6_rect))

        wall7 = wall3
        wall7_rect = wall7.get_rect(bottomleft = wall6_rect.bottomright)
        self.border.append((wall7, wall7_rect))

        wall8 = wall4
        wall8_rect = wall8.get_rect(bottomleft = wall7_rect.bottomright)
        self.border.append((wall8, wall8_rect))

        # obstacles

        lv4obstacle1 = Obstacle("up", 1, "bottomright", (44, 44), wall3_rect.topright)
        self.obstacleObjects.append(lv4obstacle1)

        lv4obstacle2 = Obstacle("up", 1, "bottomright", (44, 44), lv4obstacle1.rect.bottomleft)
        self.obstacleObjects.append(lv4obstacle2)

        lv4obstacle3 = Obstacle("up", 1, "bottomright", (44, 44), lv4obstacle2.rect.bottomleft)
        self.obstacleObjects.append(lv4obstacle3)

        lv4obstacle4 = Obstacle("up", 1, "bottomright", (44, 44), wall4_rect.topright)
        self.obstacleObjects.append(lv4obstacle4)

        lv4obstacle5 = Obstacle("up", 1, "bottomright", (44, 44), lv4obstacle4.rect.bottomleft)
        self.obstacleObjects.append(lv4obstacle5)

        lv4obstacle6 = Obstacle("up", 1, "bottomleft", (44, 44), wall7_rect.topleft)
        self.obstacleObjects.append(lv4obstacle6)

        lv4obstacle7 = Obstacle("up", 1, "bottomleft", (44, 44), lv4obstacle6.rect.bottomright)
        self.obstacleObjects.append(lv4obstacle7)

        lv4obstacle8 = Obstacle("up", 1, "bottomleft", (44, 44), lv4obstacle7.rect.bottomright)
        self.obstacleObjects.append(lv4obstacle8)

        lv4obstacle9 = Obstacle("up", 1, "bottomleft",(44, 44),  wall8_rect.topleft)
        self.obstacleObjects.append(lv4obstacle9)

        lv4obstacle10 = Obstacle("up", 1, "bottomleft", (44, 44), lv4obstacle9.rect.bottomright)
        self.obstacleObjects.append(lv4obstacle10)

        # save positions:

        save1 = SavePosition(100, 132)
        self.saveObjects.append(save1)

        save2 = SavePosition(968, 132)
        self.saveObjects.append(save2)

        # coins:

        if game_over:

            self.coinObjects = []

            coin1 = Coin(1000, 120)
            self.coinObjects.append(coin1.coin_rect)

            coin2 = Coin(820, 150)
            self.coinObjects.append(coin2.coin_rect)

            coin3 = Coin(640, 180)
            self.coinObjects.append(coin3.coin_rect)

            coin4 = Coin(539, 396)
            self.coinObjects.append(coin4.coin_rect)

            coin5 = Coin(539, 550)
            self.coinObjects.append(coin5.coin_rect)

            coin6 = Coin(539, 700)
            self.coinObjects.append(coin6.coin_rect)

    def draw(self, screen, player):

        super().draw(screen, player)