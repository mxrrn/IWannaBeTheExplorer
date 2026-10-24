import pygame

from Coin import Coin
from Level import Level
from Obstacle import Obstacle
from SavePosition import SavePosition


class Level3(Level):
    def __init__(self, game_over):
        self.coinObjects = []
        self.hidden_path_condition = False
        self.stone_showing_condition = 0
        self.blocks_moving_direction = 3
        self.blocks_moving_limit = []
        self.restart(game_over)


    def restart(self, game_over):


        super().__init__()
        self.hidden_path_condition = False
        self.stone_showing_condition = 0
        self.blocks_moving_direction = 3
        self.blocks_moving_limit = []

        wall_up = pygame.image.load('level3pics/wall_up.jpg')
        wall_up_rect = wall_up.get_rect(topright=(1100, 0))
        self.border.append((wall_up, wall_up_rect))

        wall_right = pygame.image.load('level3pics/wall_right.jpg')
        wall_right_rect = wall_right.get_rect(bottomright=(1100, 825))
        self.border.append((wall_right, wall_right_rect))

        wall_left = pygame.image.load('level3pics/wall_left.jpg')
        wall_left_rect = wall_left.get_rect(topleft=(0, 0))
        self.border.append((wall_left, wall_left_rect))

        wall_left = pygame.image.load('level3pics/wall_left.jpg')
        wall_left_rect = wall_left.get_rect(bottomleft =(0, 825))
        self.border.append((wall_left, wall_left_rect))

        wall1 = pygame.image.load('level3pics/wall1.jpg')
        wall1_rect = wall1.get_rect(topleft= wall_up_rect.topleft)
        self.border.append((wall1, wall1_rect))

        wall2 = pygame.image.load('level3pics/wall2.jpg')
        wall2_rect = wall2.get_rect(bottomleft= wall_left_rect.bottomright)
        self.border.append((wall2, wall2_rect))

        wall3 = pygame.image.load('level3pics/wall3.4.jpg')
        wall3_rect = wall3.get_rect(bottomleft= wall2_rect.bottomright)
        self.border.append((wall3, wall3_rect))

        wall3_1 = pygame.image.load('level3pics/wall3.2.jpg')
        wall3_1_rect = wall3_1.get_rect(bottomright= wall3_rect.topright)
        self.border.append((wall3_1, wall3_1_rect))
        self.blocks_moving_limit.append(wall3_1_rect)

        wall3_2 = pygame.image.load('level3pics/wall3.2.jpg')
        wall3_2_rect = wall3_2.get_rect(bottomright= wall3_1_rect.bottomleft)
        self.border.append((wall3_2, wall3_2_rect))
        self.border_to_be_removed.append((wall3_2, wall3_2_rect))

        wall3_3 = pygame.image.load('level3pics/wall3.1.jpg')
        wall3_3_rect = wall3_3.get_rect(bottomleft= wall3_rect.topleft)
        self.border.append((wall3_3, wall3_3_rect))
        self.border_to_be_removed.append((wall3_3, wall3_3_rect))

        wall3_4 = pygame.image.load('level3pics/wall3.3.jpg')
        wall3_4_rect = wall3_4.get_rect(bottomleft= wall3_3_rect.topleft)
        self.border.append((wall3_4, wall3_4_rect))

        wall4 = pygame.image.load('level3pics/wall4.jpg')
        wall4_rect = wall4.get_rect(bottomleft= wall3_rect.bottomright)
        self.border.append((wall4, wall4_rect))

        wall5 = pygame.image.load('level3pics/wall5.jpg')
        wall5_rect = wall5.get_rect(bottomleft= wall4_rect.bottomright)
        self.border.append((wall5, wall5_rect))
        self.blocks_moving_limit.append(wall5_rect)

        # obstacles

        lv3obstacle1 = Obstacle("up", 1, "bottomleft", (44, 44), wall2_rect.topleft)
        self.obstacleObjects.append(lv3obstacle1)

        lv3obstacle2 = Obstacle("up", 1, "bottomleft", (44, 44), lv3obstacle1.rect.bottomright)
        self.obstacleObjects.append(lv3obstacle2)

        lv3obstacle3 = Obstacle("up", 1, "bottomleft", (44, 44), wall4_rect.topleft)
        self.obstacleObjects.append(lv3obstacle3)

        lv3obstacle4 = Obstacle("up", 1, "bottomleft", (44, 44), lv3obstacle3.rect.bottomright)
        self.obstacleObjects.append(lv3obstacle4)

        lv3obstacle5 = Obstacle("up", 1, "bottomleft", (44, 44), lv3obstacle4.rect.bottomright)
        self.obstacleObjects.append(lv3obstacle5)

        lv3obstacle6 = Obstacle("up", 1, "bottomleft", (44, 44), lv3obstacle5.rect.bottomright)
        self.obstacleObjects.append(lv3obstacle6)

        lv3obstacle7 = Obstacle("up", 1, "bottomleft", (44, 44), lv3obstacle6.rect.bottomright)
        self.obstacleObjects.append(lv3obstacle7)

        lv3obstacle8 = Obstacle("up", 1, "bottomleft", (44, 44), lv3obstacle7.rect.bottomright)
        self.obstacleObjects.append(lv3obstacle8)

        lv3obstacle9 = Obstacle("up", 1, "bottomleft", (44, 44), lv3obstacle8.rect.bottomright)
        self.obstacleObjects.append(lv3obstacle9)

        lv3obstacle10 = Obstacle("up", 1, "bottomleft", (44, 44), lv3obstacle9.rect.bottomright)
        self.obstacleObjects.append(lv3obstacle10)

        lv3obstacle11 = Obstacle("up", 1, "bottomleft", (44, 44), lv3obstacle10.rect.bottomright)
        self.obstacleObjects.append(lv3obstacle11)

        lv3obstacle12 = Obstacle("up", 1, "bottomleft", (44, 44), lv3obstacle11.rect.bottomright)
        self.obstacleObjects.append(lv3obstacle12)

        # Stones

        stone1 = pygame.image.load('level3pics/stone.jpg')
        stone1 = pygame.transform.scale(stone1, (44,45))
        stone1_rect = stone1.get_rect(bottomleft = wall3_4_rect.topleft)
        self.stones.append((stone1, stone1_rect))

        stone2 = stone1
        stone2_rect = stone2.get_rect(bottomleft = stone1_rect.topleft)
        self.stones.append((stone2, stone2_rect))

        stone3 = stone1
        stone3_rect = stone2.get_rect(bottomleft = stone2_rect.topleft)
        self.stones.append((stone3, stone3_rect))

        # Hidden path

        path_part1 = pygame.image.load('level3pics/hidden_path1.jpg')
        path_part1_rect = path_part1.get_rect(bottomleft = wall3_rect.topleft)
        self.hidden_path.append((path_part1, path_part1_rect))

        path_part2 = pygame.image.load('level3pics/hidden_path2.jpg')
        path_part2_rect = path_part2.get_rect(bottomleft = path_part1_rect.bottomright)
        self.hidden_path.append((path_part2, path_part2_rect))

        #blocks
        lv3block1 = pygame.image.load('level2pics/Block.jpg').convert_alpha()
        lv3block1 = pygame.transform.scale(lv3block1, (44,20))
        lv3block1_rect = lv3block1.get_rect(midtop = (500, 485))
        self.blocks.append((lv3block1, lv3block1_rect))

        lv3block2 = lv3block1
        lv3block2_rect = lv3block2.get_rect(midleft = lv3block1_rect.midright)
        self.blocks.append((lv3block2, lv3block2_rect))

        # save positions:

        save1 = SavePosition(230, 380)
        self.saveObjects.append(save1)

        # coins:

        if game_over:

            self.coinObjects = []

            coin1 = Coin(50, 100)
            self.coinObjects.append(coin1.coin_rect)

            coin2 = Coin(110, 250)
            self.coinObjects.append(coin2.coin_rect)

            coin3 = Coin(50, 400)
            self.coinObjects.append(coin3.coin_rect)

            coin4 = Coin(488, 396)
            self.coinObjects.append(coin4.coin_rect)

            coin5 = Coin(660, 396)
            self.coinObjects.append(coin5.coin_rect)

            coin6 = Coin(980, 700)
            self.coinObjects.append(coin6.coin_rect)


    def draw(self, screen, player):

        super().draw(screen, player)

        for tile in self.stones:
            if tile[1].colliderect(player.rect.x + player.dx, player.rect.y, player.width, player.height):
                if self.stone_showing_condition ==0:
                    self.stone_showing_condition += 1  # wenn they collide for the first time the cond will be 1
        if self.stone_showing_condition == 1:  # when its 1
            for tile in self.stones:
                self.border.append(tile)        # added to border so that the player can't walk through it. by adding it it will be always shown
                self.stone_showing_condition += 1   # so that we don't come into this for loop again, if we do, we will add the stones multiple time (memory effort)

        if self.hidden_path[0][1].colliderect(player.rect.x + player.dx, player.rect.y, player.width, player.height):
            self.hidden_path_condition = True
        if self.hidden_path_condition:
            for tile in self.hidden_path:
                screen.blit(tile[0], tile[1])
            for tile in self.border_to_be_removed:
                if tile in self.border:
                    self.border.remove(tile)        # if we don't remove them, we won't be able to walk throght the hidden paths, because the player will be colliding with the border in the background

        if self.blocks[0][1].colliderect(self.blocks_moving_limit[0]) or self.blocks[1][1].colliderect(self.blocks_moving_limit[1]):
            self.blocks_moving_direction *= -1      # moving in the other direction
        for tile in self.blocks:
            if player.alive:        # so that when the player is dead nothing will be moving on the screen
                tile[1].x += self.blocks_moving_direction



