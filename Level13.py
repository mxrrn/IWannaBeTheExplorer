import pygame

from Coin import Coin
from Level import Level
from Obstacle import Obstacle
from SavePosition import SavePosition


class Level13(Level):

    def __init__(self,game_over):
        self.coinObjects = []
        self.restart(game_over)
        self.wall12_moving_condition = False
        self.obstacle31_moving_condition = False


    def restart(self, game_over):

        super().__init__()
        self.wall12_moving_condition = False
        self.obstacle31_moving_condition = False

        wall_up = pygame.image.load('level13pics/wall_up.jpg')
        wall_up_rect = wall_up.get_rect(topright = (1100, 0))
        self.border.append((wall_up, wall_up_rect))

        wall_right = pygame.image.load('level13pics/wall_right.jpg')
        wall_right = pygame.transform.scale(wall_right, (44, 825))
        wall_right_rect = wall_right.get_rect(topright=(1100, 0))
        self.border.append((wall_right, wall_right_rect))

        wall_left = pygame.image.load('level13pics/wall_left.jpg')
        wall_left = pygame.transform.scale(wall_left, (44, 825))
        wall_left_rect = wall_left.get_rect(topleft=(0, 0))
        self.border.append((wall_left, wall_left_rect))

        total_width = 0
        for i in range(1,5):
            wall = pygame.image.load(f'level13pics/wall{i}.jpg')
            wall_rect = wall.get_rect(bottomleft = (44 + total_width, 825))
            self.border.append((wall, wall_rect))
            total_width += wall.get_width()

        wall12 = pygame.image.load('level13pics/wall12.jpg')
        wall12_rect = wall12.get_rect(topleft= self.border[6][1].topright)
        self.border.append((wall12, wall12_rect))

        for i in range(5, 12):
            wall = pygame.image.load(f'level13pics/wall{i}.jpg')
            wall_rect = wall.get_rect(bottomleft=(44 + total_width, 825))
            self.border.append((wall, wall_rect))
            total_width += wall.get_width()

        # obstacle:

        for i in range(22):
            obstacle = Obstacle("down", 1, "topleft", (44, 44), (wall_up_rect.bottomleft[0] + i*44, wall_up_rect.bottomleft[1]))
            self.obstacleObjects.append(obstacle)

        lv12obstacle22 = Obstacle("up", 1, "bottomleft", (44, 44), self.border[3][1].topleft)
        self.obstacleObjects.append(lv12obstacle22)

        lv12obstacle23 = Obstacle("up", 1, "bottomleft", (44, 44), lv12obstacle22.rect.bottomright)
        self.obstacleObjects.append(lv12obstacle23)

        lv12obstacle24 = Obstacle("up", 1, "bottomleft", (44, 44), self.border[5][1].topleft)
        self.obstacleObjects.append(lv12obstacle24)

        lv12obstacle25 = Obstacle("up", 1, "bottomleft", (44, 44), lv12obstacle24.rect.bottomright)
        self.obstacleObjects.append(lv12obstacle25)

        lv12obstacle26 = Obstacle("up", 1, "bottomleft", (44, 44), self.border[6][1].topleft)
        self.obstacleObjects.append(lv12obstacle26)

        lv12obstacle27 = Obstacle("up", 1, "bottomright", (44, 44), self.border[9][1].topright)
        self.obstacleObjects.append(lv12obstacle27)

        lv12obstacle28 = Obstacle("up", 1, "midbottom", (44, 44), self.border[10][1].midtop)
        self.obstacleObjects.append(lv12obstacle28)

        lv12obstacle29 = Obstacle("up", 1, "midbottom", (44, 44), self.border[11][1].midtop)
        self.obstacleObjects.append(lv12obstacle29)

        lv12obstacle30 = Obstacle("up", 1, "midbottom", (44, 44), self.border[12][1].midtop)
        self.obstacleObjects.append(lv12obstacle30)

        lv12obstacle31 = Obstacle("up", 2, "midtop", (33, 128), self.border[13][1].midtop)
        self.obstacleObjects.append(lv12obstacle31)

        # save positions:

        save1 = SavePosition(264, 264)
        self.saveObjects.append(save1)


        if game_over:
            self.coinObjects = []

            coin1 = Coin(350, 350)
            self.coinObjects.append(coin1.coin_rect)

            coin2 = Coin(719, 582)
            self.coinObjects.append(coin2.coin_rect)

            coin3 = Coin(459, 272)
            self.coinObjects.append(coin3.coin_rect)

            coin4 = Coin(912, 578)
            self.coinObjects.append(coin4.coin_rect)

            coin5 = Coin(205, 260)
            self.coinObjects.append(coin5.coin_rect)

            coin6 = Coin(1003, 725)
            self.coinObjects.append(coin6.coin_rect)


    def draw(self, screen, player):

        super().draw(screen, player)

        if self.border[7][1].colliderect(player.rect.x, player.rect.y + player.dy, player.width, player.height):
            self.wall12_moving_condition = True
        if self.wall12_moving_condition:
            player.rect.y -= 20
            if self.border[7][1].midbottom[1] > self.border[8][1].midtop[1]:
                self.border[7][1].y -= 11

        if player.rect.topright[0] >= self.border[13][1][0]:
            self.obstacle31_moving_condition = True
        if self.obstacle31_moving_condition:
            self.obstacleObjects[-1].rect.y -= 6


