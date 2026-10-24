import pygame

from Coin import Coin
from Level import Level
from Obstacle import Obstacle
from SavePosition import SavePosition


class Level15(Level):

    def __init__(self,game_over):
        self.coinObjects = []
        self.restart(game_over)
        self.blocks_moving_direction = 2
        self.applesObstacles_moving_direction = 8
        self.obstacle17_moving_condition = False
        self.obstacle31_moving_condition = False



    def restart(self, game_over):

        super().__init__()
        self.blocks_moving_direction = 2
        self.applesObstacles_moving_direction = 8
        self.obstacle17_moving_condition = False
        self.obstacle31_moving_condition = False

        wall_up = pygame.image.load('level15pics/wall_up.jpg')
        wall_up_rect = wall_up.get_rect(topright=(1100, 0))
        self.border.append((wall_up, wall_up_rect))

        wall_right = pygame.image.load('level15pics/wall_right.jpg')
        wall_right = pygame.transform.scale(wall_right, (132, 825))
        wall_right_rect = wall_right.get_rect(topright=(1100, 0))
        self.border.append((wall_right, wall_right_rect))

        wall_left1 = pygame.image.load('level15pics/wall_left1.jpg')
        wall_left1 = pygame.transform.scale(wall_left1, (44, 355))
        wall_left1_rect = wall_left1.get_rect(topleft=(0, 0))
        self.border.append((wall_left1, wall_left1_rect))

        wall_left2 = pygame.image.load('level15pics/wall_left2.jpg')
        wall_left2_rect = wall_left2.get_rect(bottomleft=(0, 825))
        self.border.append((wall_left2, wall_left2_rect))

        wall1 = pygame.image.load('level15pics/wall1.jpg')
        wall1_rect = wall1.get_rect(bottomright= wall_right_rect.bottomleft)
        self.border.append((wall1, wall1_rect))

        wall2 = pygame.image.load('level15pics/wall2.jpg')
        wall2_rect = wall2.get_rect(bottomright=wall1_rect.bottomleft)
        self.border.append((wall2, wall2_rect))

        wall3 = pygame.image.load('level15pics/wall3.jpg')
        wall3_rect = wall3.get_rect(bottomright=wall2_rect.bottomleft)
        self.border.append((wall3, wall3_rect))

        wall4 = pygame.image.load('level15pics/wall4.jpg')
        wall4_rect = wall4.get_rect(bottomright=wall3_rect.bottomleft)
        self.border.append((wall4, wall4_rect))

        wall5 = pygame.image.load('level15pics/wall7.jpg')
        wall5_rect = wall5.get_rect(bottomright=wall4_rect.bottomleft)
        self.border.append((wall5, wall5_rect))

        wall6 = pygame.image.load('level15pics/wall6.jpg')
        wall6_rect = wall6.get_rect(bottomright=wall5_rect.topright)
        self.border.append((wall6, wall6_rect))

        wall7 = pygame.image.load('level15pics/wall5.jpg')
        wall7_rect = wall7.get_rect(bottomright=wall6_rect.topright)
        self.border.append((wall7, wall7_rect))

        wall8 = pygame.image.load('level15pics/wall8.jpg')
        wall8_rect = wall8.get_rect(bottomright = (wall7_rect.bottomleft[0], wall7_rect.bottomleft[1] - 44))
        self.border.append((wall8, wall8_rect))

        wall9 = pygame.image.load('level15pics/wall9.jpg')
        wall9_rect = wall9.get_rect(bottomleft=wall_left1_rect.bottomright)
        self.border.append((wall9, wall9_rect))

        wall10 = pygame.image.load('level15pics/wall10.jpg')
        wall10_rect = wall10.get_rect(bottomleft=wall9_rect.bottomright)
        self.border.append((wall10, wall10_rect))

        wall11 = pygame.image.load('level15pics/wall11.jpg')
        wall11_rect = wall11.get_rect(bottomleft=wall10_rect.bottomright)
        self.border.append((wall11, wall11_rect))

        wall12 = wall8
        wall12_rect = wall12.get_rect(bottomleft=wall11_rect.bottomright)
        self.border.append((wall12, wall12_rect))

        wall13 = pygame.image.load('level15pics/wall13.jpg')
        wall13_rect = wall13.get_rect(topleft=(wall12_rect.topright[0], wall12_rect.topright[1] + 44))
        self.border.append((wall13, wall13_rect))

        wall14 = pygame.image.load('level15pics/wall14.jpg')
        wall14_rect = wall14.get_rect(topleft=wall10_rect.bottomleft)
        self.border.append((wall14, wall14_rect))

        wall15 = pygame.image.load('level15pics/wall15.jpg')
        wall15_rect = wall15.get_rect(bottomleft=wall_left2_rect.bottomright)
        self.border.append((wall15, wall15_rect))

        wall16 = pygame.image.load('level15pics/wall16.jpg')
        wall16_rect = wall16.get_rect(bottomleft=wall15_rect.bottomright)
        self.border.append((wall16, wall16_rect))

        wall17 = pygame.image.load('level15pics/wall17.jpg')
        wall17_rect = wall17.get_rect(bottomleft=wall16_rect.bottomright)
        self.border.append((wall17, wall17_rect))

        # obstacles

        lv15obstacle1 = Obstacle("up", 1, "bottomleft", (44, 44), wall9_rect.topleft)
        self.obstacleObjects.append(lv15obstacle1)

        lv15obstacle2 = Obstacle("up", 1, "bottomleft", (44, 44), lv15obstacle1.rect.bottomright)
        self.obstacleObjects.append(lv15obstacle2)

        lv15obstacle3 = Obstacle("down", 1, "topleft", (44, 44), wall9_rect.bottomleft)
        self.obstacleObjects.append(lv15obstacle3)

        lv15obstacle4 = Obstacle("down", 1, "topleft", (44, 44), lv15obstacle3.rect.topright)
        self.obstacleObjects.append(lv15obstacle4)

        lv15obstacle5 = Obstacle("up", 1, "midbottom", (44, 44), wall1_rect.midtop)
        self.obstacleObjects.append(lv15obstacle5)

        lv15obstacle6 = Obstacle("up", 1, "midbottom", (44, 44), wall2_rect.midtop)
        self.obstacleObjects.append(lv15obstacle6)

        lv15obstacle7 = Obstacle("up", 1, "bottomright", (44, 44), wall3_rect.topright)
        self.obstacleObjects.append(lv15obstacle7)

        lv15obstacle8 = Obstacle("up", 1, "bottomleft", (44, 44), wall3_rect.topleft)
        self.obstacleObjects.append(lv15obstacle8)

        for i in range(10):
            obstacle = Obstacle("up", 1, "bottomleft", (44, 44), (wall11_rect.topleft[0] + i * 44, wall11_rect.topleft[1]))
            self.obstacleObjects.append(obstacle)

        for i in range(10):
            obstacle = Obstacle("down", 1, "topleft", (44, 44), (wall10_rect.topright[0] + i * 44, wall_up_rect.bottomleft[1]))
            self.obstacleObjects.append(obstacle)

        lv15obstacle29 = Obstacle("up", 3, "topright", (28, 31), (wall12_rect.bottomright[0], wall12_rect.bottomright[1] + 5))
        self.obstacleObjects.append(lv15obstacle29)

        lv15obstacle30 = Obstacle("up", 3, "bottomright", (28, 31), (wall7_rect.topright[0], wall7_rect.topright[1] - 5))
        self.obstacleObjects.append(lv15obstacle30)

        lv15obstacle31 = Obstacle("up", 1, "midtop", (44, 44), (wall12_rect.midtop[0], wall12_rect.midtop[1] + 15))
        self.obstacleObjects.append(lv15obstacle31)

        # blocks:

        lv15block1 = pygame.image.load('level2pics/Block.jpg').convert_alpha()
        lv15block1 = pygame.transform.scale(lv15block1, (44, 20))
        lv15block1_rect = lv15block1.get_rect(topleft= wall10_rect.topright)
        self.blocks.append((lv15block1, lv15block1_rect))

        lv15block2 = lv15block1
        lv15block2_rect = lv15block1.get_rect(midleft=lv15block1_rect.midright)
        self.blocks.append((lv15block2, lv15block2_rect))

        # save positions:

        save1 = SavePosition(176, 176)
        self.saveObjects.append(save1)

        if game_over:
            self.coinObjects = []

            coin1 = Coin(107, 470)
            self.coinObjects.append(coin1.coin_rect)

            coin2 = Coin(765, 460)
            self.coinObjects.append(coin2.coin_rect)

            coin3 = Coin(863, 344)
            self.coinObjects.append(coin3.coin_rect)

            coin4 = Coin(115, 25)
            self.coinObjects.append(coin4.coin_rect)

            coin5 = Coin(325, 158)
            self.coinObjects.append(coin5.coin_rect)

            coin6 = Coin(585, 158)
            self.coinObjects.append(coin6.coin_rect)

    def draw(self, screen, player):

        super().draw(screen, player)

        if self.blocks[0][1].colliderect(self.border[13][1]) or self.blocks[1][1].colliderect(self.border[15][1]):
            self.blocks_moving_direction *= -1      # moving in the other direction
        for tile in self.blocks:
            if player.alive:        # so that when the player is dead nothing will be moving on the screen
                tile[1].x += self.blocks_moving_direction

        if self.obstacleObjects[29].rect.colliderect(self.border[7][1]) or self.obstacleObjects[29].rect.colliderect(self.border[11][1]):
            self.applesObstacles_moving_direction *= -1
        if player.alive:
            self.obstacleObjects[28].rect.x += self.applesObstacles_moving_direction
            self.obstacleObjects[29].rect.x += self.applesObstacles_moving_direction

        if player.rect.topright[0] >= self.obstacleObjects[15].rect.midtop[0]:
            self.obstacle17_moving_condition = True
        if self.obstacle17_moving_condition:
            self.obstacleObjects[16].rect.y -= 5

        if player.rect.topright[0] >= self.obstacleObjects[17].rect.midtop[0]:
            self.obstacle31_moving_condition = True
        if self.obstacle31_moving_condition:
            self.obstacleObjects[30].rect.y -= 5