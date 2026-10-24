import pygame

from Coin import Coin
from Level import Level
from Obstacle import Obstacle
from SavePosition import SavePosition


class Level12(Level):

    def __init__(self,game_over):

        self.coinObjects = []
        self.restart(game_over)
        self.obstacles_21_22_moving_limit = 40
        self.obstacle_21_22_moving_direction = -2
        self.stone1_showing_condition = 0
        self.stone2_showing_condition = 0
        self.stone_3_4_showing_condition = 0
        self.hidden_path_condition = False
        self.obstacle41_moving_condition = False
        self.obstacles_4_5_moving_condition = False
        self.obstacles_42_43_moving_condition = False



    def restart(self, game_over):

        super().__init__()
        self.obstacles_21_22_moving_limit = 40
        self.obstacle_21_22_moving_direction = -2
        self.stone1_showing_condition = 0
        self.stone2_showing_condition = 0
        self.stone_3_4_showing_condition = 0
        self.hidden_path_condition = False
        self.obstacle41_moving_condition = False
        self.obstacles_4_5_moving_condition = False
        self.obstacles_42_43_moving_condition = False

        wall_right = pygame.image.load('level12pics/wall_right.jpg')
        wall_right_rect = wall_right.get_rect(bottomright=(1100, 825))
        self.border.append((wall_right, wall_right_rect))

        wall_up1 = pygame.image.load('level12pics/wall_up1.jpg')
        wall_up1_rect = wall_up1.get_rect(topright= (1100,0))
        self.border.append((wall_up1, wall_up1_rect))

        wall_up2 = pygame.image.load('level12pics/wall_up2.jpg')
        wall_up2_rect = wall_up2.get_rect(topright=wall_up1_rect.topleft)
        self.border.append((wall_up2, wall_up2_rect))

        wall_up3 = pygame.image.load('level12pics/wall_up3.jpg')
        wall_up3_rect = wall_up3.get_rect(topright=wall_up2_rect.topleft)
        self.border.append((wall_up3, wall_up3_rect))

        wall_up4 = pygame.image.load('level12pics/wall_up4.jpg')
        wall_up4_rect = wall_up4.get_rect(topleft = (0,0))
        self.border.append((wall_up4, wall_up4_rect))

        wall_left1 = pygame.image.load('level12pics/wall_left1.jpg')
        wall_left1_rect = wall_left1.get_rect(topleft=(0, 0))
        self.border.append((wall_left1, wall_left1_rect))

        wall_left2 = pygame.image.load('level12pics/wall_left2.jpg')
        wall_left2_rect = wall_left2.get_rect(bottomleft =(0, 825))
        self.border.append((wall_left2, wall_left2_rect))

        wall1 = pygame.image.load('level12pics/wall1.jpg')
        wall1 = pygame.transform.scale(wall1, (132, 118))
        wall1_rect = wall1.get_rect(bottomright=(1100, 825))
        self.border.append((wall1, wall1_rect))

        wall2 = pygame.image.load('level12pics/wall10.jpg')
        wall2 = pygame.transform.scale(wall2, (132, 174))
        wall2_rect = wall2.get_rect(topleft= wall_left2_rect.topright)
        self.border.append((wall2, wall2_rect))

        wall3 = pygame.image.load('level12pics/wall9.jpg')
        wall3_rect = wall3.get_rect(bottomleft = wall2_rect.bottomright)
        self.border.append((wall3, wall3_rect))

        wall4_1 = wall2
        wall4_1_rect = wall4_1.get_rect(topleft = (wall2_rect.topright[0] + 44, wall2_rect.topright[1]))
        self.border.append((wall4_1, wall4_1_rect))

        wall4_2 = pygame.image.load('level12pics/wall8.jpg')
        wall4_2_rect = wall4_2.get_rect(topleft= wall4_1_rect.topright)
        self.border.append((wall4_2, wall4_2_rect))

        wall5 = pygame.image.load('level12pics/wall5.jpg')
        wall5_rect = wall5.get_rect(midright = wall4_2_rect.bottomleft)
        self.border.append((wall5, wall5_rect))


        wall6 = pygame.image.load('level12pics/wall6.jpg')
        wall6_rect = wall6.get_rect(topleft=wall4_2_rect.topright)
        self.border.append((wall6, wall6_rect))

        wall7 = pygame.image.load('level12pics/wall7.jpg')
        wall7_rect = wall7.get_rect(topleft = (wall6_rect.topright[0], wall3_rect.topright[1]))
        self.border.append((wall7, wall7_rect))

        wall8 = wall4_2
        wall8_rect = wall8.get_rect(bottomleft=wall7_rect.bottomright)
        self.border.append((wall8, wall8_rect))

        wall9 = wall3
        wall9_rect = wall9.get_rect(bottomleft=wall8_rect.bottomright)
        self.border.append((wall9, wall9_rect))

        wall10 = wall2
        wall10_rect = wall10.get_rect(bottomleft=wall9_rect.bottomright)
        self.border.append((wall10, wall10_rect))

        wall11 = pygame.image.load('level12pics/wall11.jpg')
        wall11_rect = wall11.get_rect(bottomleft=wall10_rect.bottomright)
        self.border.append((wall11, wall11_rect))

        wall12 = pygame.image.load('level12pics/wall12.jpg')
        wall12_rect = wall12.get_rect(topleft=wall11_rect.topright)
        self.border.append((wall12, wall12_rect))

        wall13 = pygame.image.load('level12pics/wall13.jpg')
        wall13_rect = wall13.get_rect(topleft= (wall12_rect.topright[0], wall10_rect.topright[1]))
        self.border.append((wall13, wall13_rect))

        wall14 = pygame.image.load('level12pics/wall14.jpg')
        wall14_rect = wall14.get_rect(topleft=wall12_rect.bottomleft)
        self.border.append((wall14, wall14_rect))

        wall15 = pygame.image.load('level12pics/wall15.jpg')
        wall15 = pygame.transform.scale(wall15, (132,44))
        wall15_rect = wall15.get_rect(topright =wall14_rect.topleft)
        self.border.append((wall15, wall15_rect))

        wall16 = pygame.image.load('level12pics/wall16.jpg')
        wall16 = pygame.transform.scale(wall16, (44, 88))
        wall16_rect = wall16.get_rect(topleft=wall15_rect.bottomleft)
        self.border.append((wall16, wall16_rect))

        wall17 = pygame.image.load('level12pics/wall18.jpg')
        wall17_rect = wall17.get_rect(bottomright =wall1_rect.bottomleft)
        self.border.append((wall17, wall17_rect))

        wall18 = pygame.image.load('level12pics/wall17.jpg')
        wall18 = pygame.transform.scale(wall18, (240,32))
        wall18_rect = wall18.get_rect(bottomright=wall17_rect.bottomleft)
        self.border.append((wall18, wall18_rect))

        wall19 = pygame.image.load('level12pics/wall19.jpg')
        wall19_rect = wall19.get_rect(bottomright=wall18_rect.bottomleft)
        self.border.append((wall19, wall19_rect))

        wall20 = pygame.image.load('level12pics/wall20.jpg')
        wall20 = pygame.transform.scale(wall20, (88, 32))
        wall20_rect = wall20.get_rect(bottomright=wall19_rect.bottomleft)
        self.border.append((wall20, wall20_rect))

        wall21 = pygame.image.load('level12pics/wall21.jpg')
        wall21_rect = wall21.get_rect(bottomright=wall20_rect.bottomleft)
        self.border.append((wall21, wall21_rect))

        wall22 = pygame.image.load('level12pics/wall22_23.jpg')
        wall22_rect = wall22.get_rect(bottomright =wall21_rect.topright)
        self.border.append((wall22, wall22_rect))

        wall23 = wall22
        wall23_rect = wall23.get_rect(bottomleft=wall21_rect.topleft)
        self.border.append((wall23, wall23_rect))

        wall27 = pygame.image.load('level12pics/wall24.jpg')
        wall27 = pygame.transform.scale(wall27, (88, 44))
        wall27_rect = wall27.get_rect(topleft=wall4_1_rect.bottomleft)
        self.border.append((wall27, wall27_rect))

        wall24 = pygame.image.load('level12pics/wall25.jpg')
        wall24_rect = wall24.get_rect(topleft=wall2_rect.bottomleft)
        self.border.append((wall24, wall24_rect))
        self.border_to_be_removed.append((wall24, wall24_rect))

        wall25 = wall27
        wall25_rect = wall25.get_rect(topleft=wall24_rect.bottomleft)
        self.border.append((wall25, wall25_rect))
        self.border_to_be_removed.append((wall25, wall25_rect))

        wall26 = wall27
        wall26_rect = wall26.get_rect(midleft=wall25_rect.midright)
        self.border.append((wall26, wall26_rect))


        hidden_path1 = pygame.image.load('level12pics/hidden_path1.jpg')
        hidden_path1 = pygame.transform.scale(hidden_path1, (176, 44))
        hidden_path1_rect = hidden_path1.get_rect(topleft=wall24_rect.topleft)
        self.hidden_path.append((hidden_path1, hidden_path1_rect))

        hidden_path2 = pygame.image.load('level12pics/hidden_path2.jpg')
        hidden_path2 = pygame.transform.scale(hidden_path2, (88, 44))
        hidden_path2_rect = hidden_path2.get_rect(topleft= hidden_path1_rect.bottomleft)
        self.hidden_path.append((hidden_path2, hidden_path2_rect))

        # blocks

        block = pygame.image.load('level2pics/Block.jpg').convert_alpha()
        block = pygame.transform.scale(block, (44, 20))
        for i in range(3):
            block_rect = block.get_rect(topright=(wall3_rect.topleft[0] - i*44, wall3_rect.topleft[1]))
            self.blocks.append((block, block_rect))

        for i in range(3):
            block_rect = block.get_rect(topright=(wall15_rect.topleft[0] - i*44, wall15_rect.topleft[1]))
            self.blocks.append((block, block_rect))

        for i in range(3):
            block_rect = block.get_rect(bottomright=(wall16_rect.bottomleft[0] - i*44, wall16_rect.bottomleft[1]))
            self.blocks.append((block, block_rect))

        # obstacles

        lv12obstacle1 = Obstacle("up", 1, "bottomleft", (44, 44), wall2_rect.topleft)
        self.obstacleObjects.append(lv12obstacle1)

        lv12obstacle2 = Obstacle("up", 1, "bottomleft", (44, 44), lv12obstacle1.rect.bottomright)
        self.obstacleObjects.append(lv12obstacle2)

        lv12obstacle3 = Obstacle("up", 1, "bottomleft", (44, 44), lv12obstacle2.rect.bottomright)
        self.obstacleObjects.append(lv12obstacle3)

        lv12obstacle4 = Obstacle("down", 1, "topleft", (44, 44), wall27_rect.bottomleft)
        self.obstacleObjects.append(lv12obstacle4)

        lv12obstacle5 = Obstacle("down", 1, "topleft", (44, 44), lv12obstacle4.rect.topright)
        self.obstacleObjects.append(lv12obstacle5)

        lv12obstacle6 = Obstacle("right", 1, "bottomleft", (44, 44), wall4_2_rect.bottomright)
        self.obstacleObjects.append(lv12obstacle6)

        lv12obstacle7 = Obstacle("right", 1, "bottomleft", (44, 44), lv12obstacle6.rect.topleft)
        self.obstacleObjects.append(lv12obstacle7)

        lv12obstacle8 = Obstacle("left", 1, "bottomright", (44, 44), wall7_rect.bottomleft)
        self.obstacleObjects.append(lv12obstacle8)

        lv12obstacle9 = Obstacle("left", 1, "bottomright", (44, 44), lv12obstacle8.rect.topright)
        self.obstacleObjects.append(lv12obstacle9)

        lv12obstacle10 = Obstacle("down", 1, "midtop", (44, 44), wall_up2_rect.midbottom)
        self.obstacleObjects.append(lv12obstacle10)

        lv12obstacle11 = Obstacle("down", 1, "topleft", (44, 44), wall_up1_rect.bottomleft)
        self.obstacleObjects.append(lv12obstacle11)

        lv12obstacle12 = Obstacle("up", 1, "midbottom", (44, 44), wall8_rect.midtop)
        self.obstacleObjects.append(lv12obstacle12)

        lv12obstacle13 = Obstacle("up", 1, "midbottom", (44, 44), wall9_rect.midtop)
        self.obstacleObjects.append(lv12obstacle13)

        for i in range(4):
            obstacle = Obstacle("up", 1, "bottomleft", (44, 44), (wall11_rect.topleft[0] + i*44, wall11_rect.topleft[1]))
            self.obstacleObjects.append(obstacle)

        lv12obstacle18 = Obstacle("left", 1, "topright", (44, 44), (wall_right_rect[0], wall10_rect[1]))
        self.obstacleObjects.append(lv12obstacle18)

        lv12obstacle19 = Obstacle("down", 1, "midtop", (44, 44), wall13_rect.midbottom)
        self.obstacleObjects.append(lv12obstacle19)

        lv12obstacle20 = Obstacle("down", 1, "topright", (44, 44), wall12_rect.bottomright)
        self.obstacleObjects.append(lv12obstacle20)

        lv12obstacle21 = Obstacle("up", 1, "bottomleft", (44, 44), wall1_rect.topleft)
        self.obstacleObjects.append(lv12obstacle21)

        lv12obstacle22 = Obstacle("up", 1, "bottomleft", (44, 44), lv12obstacle21.rect.bottomright)
        self.obstacleObjects.append(lv12obstacle22)

        lv12obstacle23 = Obstacle("down", 1, "topright", (44, 44), wall14_rect.bottomright)
        self.obstacleObjects.append(lv12obstacle23)

        lv12obstacle24 = Obstacle("down", 1, "topleft", (44, 44), wall14_rect.bottomleft)
        self.obstacleObjects.append(lv12obstacle24)

        lv12obstacle25 = Obstacle("down", 1, "topright", (44, 44), wall15_rect.bottomright)
        self.obstacleObjects.append(lv12obstacle25)

        lv12obstacle26 = Obstacle("down", 1, "topright", (44, 44), lv12obstacle25.rect.topleft)
        self.obstacleObjects.append(lv12obstacle26)

        for i in range(4):
            obstacle = Obstacle("left", 1, "bottomright", (44, 44), (wall20_rect.topright[0], wall20_rect.topright[1] - i*44))
            self.obstacleObjects.append(obstacle)
            obstacle = Obstacle("right", 1, "bottomleft", (44, 44), (wall20_rect.topleft[0], wall20_rect.topleft[1] - i * 44))
            self.obstacleObjects.append(obstacle)

        lv12obstacle35 = Obstacle("up", 1, "bottomright", (44, 44), wall22_rect.bottomleft)
        self.obstacleObjects.append(lv12obstacle35)

        lv12obstacle36 = Obstacle("up", 1, "bottomleft", (44, 44), wall23_rect.bottomright)
        self.obstacleObjects.append(lv12obstacle36)

        lv12obstacle37 = Obstacle("up", 1, "midbottom", (44, 44), self.blocks[3][1].midtop)
        self.obstacleObjects.append(lv12obstacle37)

        lv12obstacle38 = Obstacle("up", 1, "midbottom", (44, 44), self.blocks[5][1].midtop)
        self.obstacleObjects.append(lv12obstacle38)

        lv12obstacle39 = Obstacle("up", 1, "midbottom", (44, 44), self.blocks[6][1].midtop)
        self.obstacleObjects.append(lv12obstacle39)

        lv12obstacle40 = Obstacle("up", 1, "midbottom", (44, 44), self.blocks[8][1].midtop)
        self.obstacleObjects.append(lv12obstacle40)

        lv12obstacle41 = Obstacle("left", 1, "midleft", (44, 44), wall1_rect.midleft)
        self.obstacleObjects.append(lv12obstacle41)

        lv12obstacle42 = Obstacle("up", 1, "bottomleft", (44, 44), (wall_left2_rect.bottomright[0], wall_left2_rect.bottomright[1] + 44))
        self.obstacleObjects.append(lv12obstacle42)

        lv12obstacle43 = Obstacle("up", 1, "bottomleft", (44, 44), lv12obstacle42.rect.bottomright)
        self.obstacleObjects.append(lv12obstacle43)


        # water blocks
        water_block = pygame.image.load('level9pics/water1.jpg')
        water_block = pygame.transform.scale(water_block, (wall7_rect.topleft[0] - wall3_rect.topright[0], wall4_2_rect.topright[1] - wall7_rect.topleft[1]))
        water_block_rect = water_block.get_rect(topright=wall7_rect.topleft)
        self.waterBlocks.append((water_block, water_block_rect))

        # stones

        stone1 = pygame.image.load('level3pics/stone.jpg')
        stone1 = pygame.transform.scale(stone1, (44, 45))
        stone1_rect = stone1.get_rect(topright= (self.obstacleObjects[13].rect.midtop[0] ,wall7_rect.topleft[1]))
        self.stones.append((stone1, stone1_rect))

        stone2 = stone1
        stone2_rect = stone2.get_rect(topleft = stone1_rect.topright)
        self.stones.append((stone2, stone2_rect))

        stone3 = stone1
        stone3_rect = stone3.get_rect(bottomright= wall23_rect.topright)
        self.stones.append((stone3, stone3_rect))

        stone4 = stone1
        stone4_rect = stone4.get_rect(bottomright=stone3_rect.topright)
        self.stones.append((stone4, stone4_rect))

        # save positions:

        save1 = SavePosition(125, 120)
        self.saveObjects.append(save1)

        save2 = SavePosition(720, 560)
        self.saveObjects.append(save2)

        # coins:

        if game_over:
            self.coinObjects = []

            coin1 = Coin(945, 733)
            self.coinObjects.append(coin1.coin_rect)

            coin2 = Coin(767, 752)
            self.coinObjects.append(coin2.coin_rect)

            coin3 = Coin(592, 677)
            self.coinObjects.append(coin3.coin_rect)

            coin4 = Coin(83, 666)
            self.coinObjects.append(coin4.coin_rect)

            coin5 = Coin(160, 583)
            self.coinObjects.append(coin5.coin_rect)

            coin6 = Coin(547, 182)
            self.coinObjects.append(coin6.coin_rect)


    def draw(self, screen, player):

        super().draw(screen, player)

        if self.obstacles_21_22_moving_limit == 40:
            self.obstacle_21_22_moving_direction *= -1
            self.obstacles_21_22_moving_limit = 0
        self.obstacles_21_22_moving_limit += 2
        self.obstacleObjects[20].rect.y += self.obstacle_21_22_moving_direction
        self.obstacleObjects[21].rect.y += self.obstacle_21_22_moving_direction

        if self.stones[0][1].colliderect(player.rect.x + player.dx, player.rect.y + player.dy, player.width, player.height):
            if self.stone1_showing_condition == 0:
                self.stone1_showing_condition += 1
        if self.stones[1][1].colliderect(player.rect.x + player.dx, player.rect.y + player.dy, player.width, player.height):
            if self.stone2_showing_condition == 0:
                self.stone2_showing_condition += 1
        if self.stones[2][1].colliderect(player.rect.x + player.dx, player.rect.y + player.dy, player.width, player.height) or self.stones[3][1].colliderect(player.rect.x + player.dx, player.rect.y + player.dy, player.width, player.height) :
            self.stone_3_4_showing_condition += 1
        if self.stone1_showing_condition == 1:
            self.border.append(self.stones[0])
            self.stone1_showing_condition += 1
        if self.stone2_showing_condition == 1:
            self.border.append(self.stones[1])
            self.stone1_showing_condition += 1
        if self.stone_3_4_showing_condition:
            self.border.append(self.stones[2])
            self.border.append(self.stones[3])
            self.stone_3_4_showing_condition += 1

        if self.hidden_path[0][1].colliderect(player.rect.x + player.dx, player.rect.y, player.width, player.height):
            self.hidden_path_condition = True
        if self.hidden_path_condition:
            for tile in self.hidden_path:
                screen.blit(tile[0], tile[1])
            for tile in self.border_to_be_removed:
                if tile in self.border:
                    self.border.remove(tile)

        if 500 < player.rect.topright[0] <= self.border[21][1].bottomleft[0] and player.rect.topright[1] >= self.border[21][1].bottomleft[1]:
            self.obstacle41_moving_condition = True
        if self.obstacle41_moving_condition:
            self.obstacleObjects[40].rect.x -= 5

        if player.rect.x <= self.border[12][1][0] and player.rect.y > self.border[8][1].midbottom[1]:
            self.obstacles_4_5_moving_condition = True
        if self.obstacles_4_5_moving_condition:
            self.obstacleObjects[3].rect.y += 4
            self.obstacleObjects[4].rect.y += 4
            self.border[31][1].y += 4

        if player.rect.x < self.border[30][1][0] and player.rect.y > self.border[30][1][1]:
            self.obstacles_42_43_moving_condition = True
        if self.obstacles_42_43_moving_condition:
            self.obstacleObjects[41].rect.y -= 4
            self.obstacleObjects[42].rect.y -= 4