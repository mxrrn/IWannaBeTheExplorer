import pygame

from Coin import Coin
from Level import Level
from Obstacle import Obstacle
from SavePosition import SavePosition


class Level6(Level):
    def __init__(self, game_over):
        self.coinObjects = []

        self.restart(game_over)
        self.stone_showing_condition = 0
        self.hidden_path_condition = False
        self.obstacle6_moving_condition = False
        self.obstacle8_moving_condition = False
        self.obstacle_9_10_moving_condition = False
        self.obstacle_15_16_moving_condition = False
        self.obstacle20_moving_condition = False
        self.obstacle21_moving_condition = False

    def restart(self, game_over):

        super().__init__()

        self.stone_showing_condition = 0
        self.hidden_path_condition = False
        self.obstacle6_moving_condition = False
        self.obstacle8_moving_condition = False
        self.obstacle_9_10_moving_condition = False
        self.obstacle_15_16_moving_condition = False
        self.obstacle20_moving_condition = False
        self.obstacle21_moving_condition = False

        wall_up1 = pygame.image.load('level6pics/wall_up.jpg')
        wall_up1_rect = wall_up1.get_rect(topright = (1100, 0))
        self.border.append((wall_up1, wall_up1_rect))

        wall_up2 = wall_up1
        wall_up2_rect = wall_up2.get_rect(topleft = (0, 0))
        self.border.append((wall_up2, wall_up2_rect))

        wall_right = pygame.image.load('level6pics/wall_right.jpg')
        wall_right_rect = wall_right.get_rect(bottomright = (1100, 825))
        self.border.append((wall_right, wall_right_rect))

        wall_left1 = pygame.image.load('level6pics/wall_left1.jpg')
        wall_left1_rect = wall_left1.get_rect(bottomleft=(0, 825))
        self.border.append((wall_left1, wall_left1_rect))

        wall_left2 = pygame.image.load('level6pics/wall_left2.jpg')
        wall_left2_rect = wall_left2.get_rect(topleft = (0,0))
        self.border.append((wall_left2, wall_left2_rect))

        wall1 = pygame.image.load('level6pics/wall1.jpg')
        wall1_rect = wall1.get_rect(topright = (1100, 44))
        self.border.append((wall1, wall1_rect))

        wall2 = pygame.image.load('level6pics/wall2.jpg')
        wall2_rect = wall2.get_rect(bottomright=wall_right_rect.bottomleft)
        self.border.append((wall2, wall2_rect))

        wall3 = pygame.image.load('level6pics/wall3.jpg')
        wall3_rect = wall3.get_rect(bottomright= wall2_rect.bottomleft)
        self.border.append((wall3, wall3_rect))

        wall4 = pygame.image.load('level6pics/wall4.jpg')
        wall4_rect = wall4.get_rect(bottomright=wall3_rect.bottomleft)
        self.border.append((wall4, wall4_rect))

        wall5 = pygame.image.load('level6pics/wall5.jpg')
        wall5_rect = wall5.get_rect(bottomright=wall4_rect.bottomleft)
        self.border.append((wall5, wall5_rect))

        wall6 = pygame.image.load('level6pics/wall6_8.jpg')
        wall6_rect = wall6.get_rect(bottomright=wall5_rect.bottomleft)
        self.border.append((wall6, wall6_rect))

        wall7 = pygame.image.load('level6pics/wall7.jpg')
        wall7_rect = wall7.get_rect(bottomright=wall6_rect.bottomleft)
        self.border.append((wall7, wall7_rect))

        wall8 = wall6
        wall8_rect = wall8.get_rect(bottomright=wall7_rect.bottomleft)
        self.border.append((wall8, wall8_rect))

        wall9 = pygame.image.load('level6pics/wall9.jpg')
        wall9_rect = wall9.get_rect(topleft = (44, 221))
        self.border.append((wall9, wall9_rect))

        wall10 = pygame.image.load('level6pics/wall10.jpg')
        wall10_rect = wall10.get_rect(topleft= wall9_rect.topright)
        self.border.append((wall10, wall10_rect))

        wall10_1 = wall10
        wall10_1_rect = wall10_1.get_rect(topleft= (wall10_rect.x, wall10_rect.y + 85))
        self.border.append((wall10_1, wall10_1_rect))

        wall11 = pygame.image.load('level6pics/wall11.jpg')
        wall11_rect = wall11.get_rect(bottomleft = wall9_rect.bottomright)
        self.border.append((wall11, wall11_rect))

        wall12 = pygame.image.load('level6pics/wall12.jpg')
        wall12_rect = wall12.get_rect(bottomleft=wall11_rect.bottomright)
        self.border.append((wall12, wall12_rect))

        wall13 = pygame.image.load('level6pics/wall13.jpg')
        wall13_rect = wall13.get_rect(bottomright=wall1_rect.bottomleft)
        self.border.append((wall13, wall13_rect))

        wall14 = pygame.image.load('level6pics/wall14.jpg')
        wall14_rect = wall14.get_rect(topright = wall13_rect.topleft)
        self.border.append((wall14, wall14_rect))

        wall15 = pygame.image.load('level6pics/wall15.jpg')
        wall15_rect = wall15.get_rect(bottomright=wall13_rect.bottomleft)
        self.border.append((wall15, wall15_rect))
        self.border_to_be_removed.append((wall15, wall15_rect))

        wall16 = pygame.image.load('level6pics/wall16.jpg')
        wall16_rect = wall16.get_rect(topright =wall15_rect.topright)
        self.border.append((wall16, wall16_rect))
        self.border_to_be_removed.append((wall16, wall16_rect))

        wall17 = pygame.image.load('level6pics/wall17.jpg')
        wall17_rect = wall17.get_rect(bottomright = wall15_rect.bottomleft)
        self.border.append((wall17, wall17_rect))

        wall10_2 = wall10
        wall10_2_rect = wall10_2.get_rect(topright = wall14_rect.topleft)
        self.border.append((wall10_2, wall10_2_rect))

        wall10_3 = wall10
        wall10_3_rect = wall10_3.get_rect(topright=wall17_rect.topleft)
        self.border.append((wall10_3, wall10_3_rect))

        # hidden paths

        hidden_path1 = pygame.image.load('level6pics/hidden_path1.jpg')
        hidden_path1_rect = hidden_path1.get_rect(bottomleft =wall17_rect.topleft)
        self.hidden_path.append((hidden_path1, hidden_path1_rect))

        hidden_path2 = pygame.image.load('level6pics/hidden_path2.jpg')
        hidden_path2_rect = hidden_path2.get_rect(topleft = wall15_rect.topleft)
        self.hidden_path.append((hidden_path2, hidden_path2_rect))

        # obstacles

        lv6obstacle1 = Obstacle("up", 1, "bottomleft", (44, 44), wall9_rect.topleft)
        self.obstacleObjects.append(lv6obstacle1)

        lv6obstacle2 = Obstacle("up", 1, "bottomleft", (44, 44), lv6obstacle1.rect.bottomright)
        self.obstacleObjects.append(lv6obstacle2)

        lv6obstacle3 = Obstacle("up", 1, "bottomleft", (44, 44), lv6obstacle2.rect.bottomright)
        self.obstacleObjects.append(lv6obstacle3)

        lv6obstacle4 = Obstacle("up", 1, "bottomleft", (44, 44), lv6obstacle3.rect.bottomright)
        self.obstacleObjects.append(lv6obstacle4)

        lv6obstacle5 = Obstacle("up", 1, "bottomleft", (44, 44), lv6obstacle4.rect.bottomright)
        self.obstacleObjects.append(lv6obstacle5)

        lv6obstacle6 = Obstacle("up", 1, "bottomleft", (44, 44), lv6obstacle5.rect.bottomright)
        self.obstacleObjects.append(lv6obstacle6)

        lv6obstacle7 = Obstacle("right", 1, "bottomleft", (44, 44), wall10_1_rect.topleft)
        self.obstacleObjects.append(lv6obstacle7)

        lv6obstacle8 = Obstacle("left", 1, "midright", (44, 44), wall16_rect.midleft)
        self.obstacleObjects.append(lv6obstacle8)

        lv6obstacle9 = Obstacle("down", 1, "topright", (44, 44), wall10_1_rect.bottomright)
        self.obstacleObjects.append(lv6obstacle9)

        lv6obstacle10 = Obstacle("up", 1, "bottomleft", (44, 44), wall11_rect.topleft)
        self.obstacleObjects.append(lv6obstacle10)

        lv6obstacle11 = Obstacle("up", 1, "bottomright", (44, 44), wall11_rect.topright)
        self.obstacleObjects.append(lv6obstacle11)

        lv6obstacle12 = Obstacle("up", 1, "bottomright", (44, 44), lv6obstacle11.rect.bottomleft)
        self.obstacleObjects.append(lv6obstacle12)

        lv6obstacle13 = Obstacle("up", 1, "bottomright", (44, 44), wall3_rect.topright)
        self.obstacleObjects.append(lv6obstacle13)

        lv6obstacle14 = Obstacle("up", 1, "bottomright", (44, 44), lv6obstacle13.rect.bottomleft)
        self.obstacleObjects.append(lv6obstacle14)

        lv6obstacle15 = Obstacle("up", 1, "bottomright", (44, 44), lv6obstacle14.rect.bottomleft)
        self.obstacleObjects.append(lv6obstacle15)

        lv6obstacle16 = Obstacle("up", 1, "bottomright", (44, 44), lv6obstacle15.rect.bottomleft)
        self.obstacleObjects.append(lv6obstacle16)

        lv6obstacle17 = Obstacle("down", 1, "topleft", (44, 44), wall12_rect.bottomleft)
        self.obstacleObjects.append(lv6obstacle17)

        lv6obstacle18 = Obstacle("up", 1, "midbottom", (44, 44), wall8_rect.midtop)
        self.obstacleObjects.append(lv6obstacle18)

        lv6obstacle19 = Obstacle("up", 1, "midbottom", (44, 44), (550, 221))
        self.obstacleObjects.append(lv6obstacle19)

        lv6obstacle20 = Obstacle("left", 2, "topleft", (33, 128), wall4_rect.topleft)
        self.obstacleObjects.append(lv6obstacle20)

        lv6obstacle21 = Obstacle("up", 2, "midtop", (33, 128), (wall7_rect.midtop[0], wall7_rect.midtop[1] + 20))
        self.obstacleObjects.append(lv6obstacle21)


        # blocks

        lv6block1 = pygame.image.load('level6pics/Block.jpg').convert_alpha()
        lv6block1 = pygame.transform.scale(lv6block1, (44, 20))
        lv6block1_rect = lv6block1.get_rect(topleft = wall4_rect.topright)
        self.blocks.append((lv6block1, lv6block1_rect))

        lv6block2 = lv6block1
        lv6block2_rect = lv6block2.get_rect(topleft= lv6block1_rect.topright)
        self.blocks.append((lv6block2, lv6block2_rect))

        lv6block3 = lv6block1
        lv6block3_rect = lv6block3.get_rect(topleft=lv6block2_rect.topright)
        self.blocks.append((lv6block3, lv6block3_rect))

        lv6block4 = lv6block1
        lv6block4_rect = lv6block4.get_rect(topleft=lv6block3_rect.topright)
        self.blocks.append((lv6block4, lv6block4_rect))

        # stones

        stone1 = pygame.image.load('level3pics/stone.jpg')
        stone1 = pygame.transform.scale(stone1, (44, 46))
        stone1_rect = stone1.get_rect(bottomright= lv6obstacle12.rect.bottomleft)
        self.stones.append((stone1, stone1_rect))

        stone2 = stone1
        stone2_rect = stone2.get_rect(midbottom = stone1_rect.midtop)
        self.stones.append((stone2, stone2_rect))

        # save positions:

        save1 = SavePosition(690, 150)
        self.saveObjects.append(save1)

        save2 = SavePosition(950, 420)
        self.saveObjects.append(save2)

        # coins:

        if game_over:

            self.coinObjects = []

            coin1 = Coin(539, 100)
            self.coinObjects.append(coin1.coin_rect)

            coin2 = Coin(320, 240)
            self.coinObjects.append(coin2.coin_rect)

            coin3 = Coin(500, 400)
            self.coinObjects.append(coin3.coin_rect)

            coin4 = Coin(680, 640)
            self.coinObjects.append(coin4.coin_rect)

            coin5 = Coin(1000, 415)
            self.coinObjects.append(coin5.coin_rect)

            coin6 = Coin(280, 650)
            self.coinObjects.append(coin6.coin_rect)


    def draw(self, screen, player):

        super().draw(screen, player)

        for tile in self.stones:
            if tile[1].colliderect(player.rect.x + player.dx, player.rect.y, player.width, player.height):
                self.stone_showing_condition += 1  # wenn they collide for the first time the cond will be 1
                self.obstacle_9_10_moving_condition = True
        if self.stone_showing_condition == 1:       # when its 1
            for tile in self.stones:
                self.border.append(tile)
                self.stone_showing_condition += 1   # so that the cond will never be 1 again and stone will be aded only one time to border

        if self.hidden_path[0][1].colliderect(player.rect.x + player.dx, player.rect.y, player.width, player.height):
            self.hidden_path_condition = True
        if self.hidden_path_condition:
            for tile in self.hidden_path:
                screen.blit(tile[0], tile[1])
            for tile in self.border_to_be_removed:
                if tile in self.border:
                    self.border.remove(tile)        # if we don't remove them, we won't be able to walk throght the hidden paths, because the player will be colliding with the border in the background

        # moving obstacles on certain conditions only when the player is alive
        if player.alive:
            if self.border[19][1].colliderect(player.rect.x, player.rect.y + player.dy, player.width, player.height) and \
                    player.rect.x <= self.obstacleObjects[18].rect.x :
               self.obstacle6_moving_condition = True
            if self.obstacle6_moving_condition:
                self.obstacleObjects[5].rect.x += 6

            if 600 >= player.rect.x >= self.obstacleObjects[7].rect.x and 310 <= player.rect.y <= 510:
                self.obstacle8_moving_condition = True
            if self.obstacle8_moving_condition:
                self.obstacleObjects[7].rect.y += 6

            if self.obstacle_9_10_moving_condition:
                self.obstacleObjects[8].rect.x += 6
                self.obstacleObjects[9].rect.x += 6

            for i in range (0,2):
                if self.blocks[i][1].colliderect(player.rect.x, player.rect.y + player.dy, player.width, player.height):
                    self.obstacle_15_16_moving_condition = True
            if self.obstacle_15_16_moving_condition:
                self.obstacleObjects[14].rect.y -= 6
                self.obstacleObjects[15].rect.y -= 6

            if player.rect.y > self.border[8][1].y :
                self.obstacle20_moving_condition = True
            if self.obstacle20_moving_condition:
                self.obstacleObjects[19].rect.x -= 5

            if self.border[11][1].colliderect(player.rect.x, player.rect.y + player.dy, player.width, player.height):
                self.obstacle21_moving_condition = True
            if self.obstacle21_moving_condition:
                self.obstacleObjects[20].rect.y -= 3

