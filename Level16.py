import pygame

from Coin import Coin
from Level import Level
from Obstacle import Obstacle
from SavePosition import SavePosition


class Level16(Level):

    def __init__(self,game_over):
        self.coinObjects = []
        self.restart(game_over)

    def restart(self, game_over):

        super().__init__()

        wall_left = pygame.image.load('level16pics/wall_left.jpg')
        wall_left = pygame.transform.scale(wall_left, (44,825))
        wall_left_rect = wall_left.get_rect(topleft=(0, 0))
        self.border.append((wall_left, wall_left_rect))

        wall_up= pygame.image.load('level16pics/wall_up.jpg')
        wall_up_rect = wall_up.get_rect(topright=(1100, 0))
        self.border.append((wall_up, wall_up_rect))

        total_height = 0
        for i in range(1,9):
            wall_right = pygame.image.load(f'level16pics/wall_right{i}.jpg')
            wall_right_rect = wall_right.get_rect(topright = (1100, total_height))
            self.border.append((wall_right, wall_right_rect))
            total_height += wall_right.get_height()

        wall1 = pygame.image.load('level16pics/wall1.jpg')
        wall1_rect = wall1.get_rect(topleft= wall_left_rect.topright)
        self.border.append((wall1, wall1_rect))

        wall2 = pygame.image.load('level16pics/wall2.jpg')
        wall2_rect = wall2.get_rect(bottomleft =wall1_rect.bottomright)
        self.border.append((wall2, wall2_rect))

        wall3 = pygame.image.load('level16pics/wall3.jpg')
        wall3_rect = wall3.get_rect(topleft= (wall_left_rect.bottomright[0], wall_left_rect.bottomright[1] - 164))
        self.border.append((wall3, wall3_rect))

        wall4 = pygame.image.load('level16pics/wall4.jpg')
        wall4_rect = wall4.get_rect(topright = (self.border[2][1].topleft[0], self.border[2][1].topleft[1] + 2))
        self.border.append((wall4, wall4_rect))

        wall5 = pygame.image.load('level16pics/wall5.jpg')
        wall5_rect = wall5.get_rect(bottomright =wall4_rect.bottomleft)
        self.border.append((wall5, wall5_rect))

        total_width = 0
        for i in range(6, 12):
            wall = pygame.image.load(f'level16pics/wall{i}.jpg')
            wall_rect = wall.get_rect(bottomleft =(wall3_rect.bottomright[0] + total_width, wall3_rect.bottomright[1]))
            self.border.append((wall, wall_rect))
            total_width += wall.get_width()

        wall12 = pygame.image.load('level16pics/wall12.jpg')
        wall12_rect = wall12.get_rect(bottomright = self.border[9][1].bottomleft)
        self.border.append((wall12, wall12_rect))

        wall13 = wall12
        wall13_rect = wall13.get_rect(bottomright= wall12_rect.bottomleft)
        self.border.append((wall13, wall13_rect))

        wall14 = wall12
        wall14_rect = wall14.get_rect(bottomright= wall13_rect.bottomleft)
        self.border.append((wall14, wall14_rect))

        wall15 = wall12
        wall15_rect = wall15.get_rect(bottomright= wall14_rect.bottomleft)
        self.border.append((wall15, wall15_rect))

        water_block1 = pygame.image.load('level9pics/water1.jpg')
        water_block1 = pygame.transform.scale(water_block1, (1100,825))
        water_block1_rect = water_block1.get_rect(topleft = (0,0))
        self.waterBlocks.append((water_block1, water_block1_rect))

        # obstacles:

        lv16obstacle1 = Obstacle("right", 1, "topleft", (44, 44), wall2_rect.topright)
        self.obstacleObjects.append(lv16obstacle1)

        lv16obstacle2 = Obstacle("right", 1, "topleft", (44, 44), lv16obstacle1.rect.bottomleft)
        self.obstacleObjects.append(lv16obstacle2)

        lv16obstacle3 = Obstacle("down", 1, "topleft", (44, 44), (self.border[3][1].bottomleft[0],self.border[3][1].bottomleft[1] - 5) )
        self.obstacleObjects.append(lv16obstacle3)

        lv16obstacle4 = Obstacle("up", 1, "midbottom", (42, 44), (self.border[17][1].midtop[0], self.border[17][1].midtop[1] + 5))
        self.obstacleObjects.append(lv16obstacle4)

        lv16obstacle5 = Obstacle("up", 1, "midbottom", (44, 44), self.border[18][1].midtop)
        self.obstacleObjects.append(lv16obstacle5)

        lv16obstacle6 = Obstacle("up", 1, "midbottom", (44, 44), self.border[19][1].midtop)
        self.obstacleObjects.append(lv16obstacle6)

        lv16obstacle7 = Obstacle("up", 1, "midbottom", (44, 44), self.border[20][1].midtop)
        self.obstacleObjects.append(lv16obstacle7)

        for i in range(1,9):
            obstacle = Obstacle("left", 1, "topright", (44, 44), (wall4_rect.x, wall4_rect.y + i*44))
            self.obstacleObjects.append(obstacle)

        for i in range(0, 9):
            obstacle = Obstacle("up", 1, "bottomleft", (44, 44), (wall5_rect.x + i * 44, wall5_rect.y))
            self.obstacleObjects.append(obstacle)

        for i in range(0, 12):
            obstacle = Obstacle("up", 1, "bottomleft", (44, 44), (wall3_rect.x + i * 44, wall3_rect.y))
            self.obstacleObjects.append(obstacle)

        for i in range(0, 25):
            obstacle = Obstacle("up", 1, "bottomleft", (22, 22), (wall15_rect.x + 200 + i*22, wall15_rect.y + 4))
            self.obstacleObjects.append(obstacle)

        for i in range(0, 8):
            obstacle = Obstacle("up", 1, "bottomleft", (22, 22), (wall15_rect.x + 233 + i*66, wall15_rect.y - 18))
            self.obstacleObjects.append(obstacle)

        # save positions:

        save1 = SavePosition(210, 176)
        self.saveObjects.append(save1)

        save2 = SavePosition(704, 616)
        self.saveObjects.append(save2)


        if game_over:
            self.coinObjects = []

            coin1 = Coin(457, 265)
            self.coinObjects.append(coin1.coin_rect)

            coin2 = Coin(85, 475)
            self.coinObjects.append(coin2.coin_rect)

            coin3 = Coin(567, 580)
            self.coinObjects.append(coin3.coin_rect)

            coin4 = Coin(763, 374)
            self.coinObjects.append(coin4.coin_rect)

            coin5 = Coin(693, 738)
            self.coinObjects.append(coin5.coin_rect)

            coin6 = Coin(427, 738)
            self.coinObjects.append(coin6.coin_rect)


    def draw(self, screen, player):
        super().draw(screen, player)
