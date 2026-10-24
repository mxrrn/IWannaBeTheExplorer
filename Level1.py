import pygame

from Coin import Coin
from Level import Level
from Obstacle import Obstacle
from SavePosition import SavePosition


class Level1(Level):
    def __init__(self, game_over):
        '''we dont want to define the coins in the Parent class, because if we do..'''
        self.coinObjects = []
        self.restart(game_over)

    def restart(self, game_over):
        '''then the list of coins will be emptied every time we restart the level, but when we come back to this level
        due to a save, we will call this restart method and we want to show the coins who werent collected, so it muss
        not be empty then'''

        super().__init__()

        # Einzelteile des Levels

        wall_up = pygame.image.load('level1pics\wall_up.jpg')
        wall_up_rect = wall_up.get_rect(topleft = (0,0))
        self.border.append((wall_up, wall_up_rect))

        wall_right1 = pygame.image.load('level1pics/wall_right1.jpg')
        wall_right1_rect = wall_right1.get_rect(topright = wall_up_rect.bottomright)
        self.border.append((wall_right1,wall_right1_rect))

        wall_right2 = pygame.image.load('level1pics/wall_right2.jpg')
        wall_right2_rect = wall_right2.get_rect(topright=wall_right1_rect.bottomright)
        self.border.append((wall_right2, wall_right2_rect))

        wall_right3 = pygame.image.load('level1pics/wall_right3.jpg')
        wall_right3_rect = wall_right3.get_rect(topright=wall_right2_rect.bottomright)
        self.border.append((wall_right3, wall_right3_rect))

        wall_left1 = pygame.image.load('level1pics\wall_left1.jpg')
        wall_left1_rect = wall_left1.get_rect(topleft = (0,0))
        self.border.append((wall_left1, wall_left1_rect))

        wall_left2 = pygame.image.load('level1pics\wall_left2.jpg')
        wall_left2_rect = wall_left2.get_rect(topleft=wall_left1_rect.bottomleft)
        self.border.append((wall_left2, wall_left2_rect))

        wall_bottom1 = pygame.image.load('level1pics\wallBottom1.jpg')
        wall_bottom1_rect = wall_bottom1.get_rect(bottomright = (1100, 825))
        self.border.append((wall_bottom1, wall_bottom1_rect))

        wall_bottom2 = pygame.image.load('level1pics\wallBottom2_4_6.jpg')
        wall_bottom2_rect = wall_bottom2.get_rect(bottomright = wall_bottom1_rect.bottomleft)
        self.border.append((wall_bottom2, wall_bottom2_rect))

        wall_bottom3 = pygame.image.load('level1pics\wallBottom3_5.jpg')
        wall_bottom3_rect = wall_bottom3.get_rect(bottomright = wall_bottom2_rect.bottomleft)
        self.border.append((wall_bottom3, wall_bottom3_rect))

        wall_bottom4 = wall_bottom2
        wall_bottom4_rect = wall_bottom4.get_rect(bottomright = wall_bottom3_rect.bottomleft)
        self.border.append((wall_bottom4, wall_bottom4_rect))

        wall_bottom5 = wall_bottom3
        wall_bottom5_rect = wall_bottom5.get_rect(bottomright = wall_bottom4_rect.bottomleft)
        self.border.append((wall_bottom5, wall_bottom5_rect))

        wall_bottom6 = wall_bottom2
        wall_bottom6_rect = wall_bottom6.get_rect(bottomright = wall_bottom5_rect.bottomleft)
        self.border.append((wall_bottom6, wall_bottom6_rect))

        wall_bottom7 = pygame.image.load('level1pics\wallBottom7.jpg')
        wall_bottom7_rect = wall_bottom7.get_rect(bottomright = wall_bottom6_rect.bottomleft)
        self.border.append((wall_bottom7, wall_bottom7_rect))

        wall_bottom8 = pygame.image.load('level1pics\wallBottom8.jpg')
        wall_bottom8_rect = wall_bottom8.get_rect(bottomright = wall_bottom7_rect.bottomleft)
        self.border.append((wall_bottom8, wall_bottom8_rect))

        floor_midtop1 = pygame.image.load('level1pics\wall_midtop1.jpg')
        floor_midtop1_rect = floor_midtop1.get_rect(bottomright = wall_right1_rect.bottomleft)
        self.border.append((floor_midtop1, floor_midtop1_rect))

        floor_midtop2 = pygame.image.load('level1pics\wall_midtop2.jpg')
        floor_midtop2_rect = floor_midtop2.get_rect(bottomright = floor_midtop1_rect.bottomleft)
        self.border.append((floor_midtop2, floor_midtop2_rect))

        floor_midtop3 = pygame.image.load('level1pics\wall_midtop3.jpg')
        floor_midtop3_rect = floor_midtop3.get_rect(bottomright = floor_midtop2_rect.bottomleft)
        self.border.append((floor_midtop3, floor_midtop3_rect))

        floor_midbottom1 = pygame.image.load('level1pics\wall_midbottom1.jpg')
        floor_midbottom1_rect = floor_midbottom1.get_rect(bottomleft = wall_left1_rect.bottomright)
        self.border.append((floor_midbottom1, floor_midbottom1_rect))

        floor_midbottom2 = floor_midtop2
        floor_midbottom2_rect = floor_midbottom2.get_rect(bottomleft = floor_midbottom1_rect.bottomright)
        self.border.append((floor_midbottom2, floor_midbottom2_rect))

        floor_midbottom3 = floor_midtop1
        floor_midbottom3_rect = floor_midbottom3.get_rect(bottomright = wall_right2_rect.bottomleft)
        self.border.append((floor_midbottom3, floor_midbottom3_rect))

        floor_midbottom4 = floor_midtop2
        floor_midbottom4_rect = floor_midbottom4.get_rect(bottomright = floor_midbottom3_rect.bottomleft)
        self.border.append((floor_midbottom4, floor_midbottom4_rect))


        # obstacles:
        lv1obstacle1 = Obstacle("up", 1, "bottomleft", (44, 44), floor_midtop3_rect.topleft)
        self.obstacleObjects.append(lv1obstacle1)

        lv1obstacle2 = Obstacle("up", 1, "topleft", (44, 44), (lv1obstacle1.rect.x + 220, lv1obstacle1.rect.y))
        self.obstacleObjects.append(lv1obstacle2)

        lv1obstacle3 = Obstacle("up", 1, "topleft", (44, 44), (lv1obstacle2.rect.x + 220, lv1obstacle1.rect.y))
        self.obstacleObjects.append(lv1obstacle3)

        lv1obstacle4 = Obstacle("up", 1, "bottomleft", (44, 44), floor_midbottom1_rect.topleft)
        self.obstacleObjects.append(lv1obstacle4)

        lv1obstacle5 = Obstacle("up", 1, "topleft", (44, 44), (lv1obstacle4.rect.x + 190, lv1obstacle4.rect.y))
        self.obstacleObjects.append(lv1obstacle5)

        lv1obstacle6 = Obstacle("up", 1, "topleft", (44, 44), (lv1obstacle5.rect.x + 190, lv1obstacle4.rect.y))
        self.obstacleObjects.append(lv1obstacle6)

        lv1obstacle7 = Obstacle("up", 1, "topleft", (44, 44), (lv1obstacle6.rect.x + 190, lv1obstacle4.rect.y))
        self.obstacleObjects.append(lv1obstacle7)

        lv1obstacle8 = Obstacle("up", 1, "bottomright",(44, 44),  wall_right3_rect.bottomleft)
        self.obstacleObjects.append(lv1obstacle8)

        lv1obstacle9 = Obstacle("up", 1, "midbottom", (44, 44), wall_bottom5_rect.midtop)
        self.obstacleObjects.append(lv1obstacle9)

        lv1obstacle10 = Obstacle("up", 1, "midbottom", (44, 44), wall_bottom3_rect.midtop)
        self.obstacleObjects.append(lv1obstacle10)

        lv1obstacle11 = Obstacle("up", 1, "bottomright", (44, 44), wall_bottom7_rect.topright)
        self.obstacleObjects.append(lv1obstacle11)

        # save positions
        save1 = SavePosition(1000, 122)
        self.saveObjects.append(save1)

        save2 = SavePosition(1000, 396)
        self.saveObjects.append(save2)

        # Coins
        '''the coins will be all recreated only when we make the level for the first time or when we want to restart 
        the whole level. In those cases game_over will be True as explained in game class'''
        if game_over:

            self.coinObjects = []

            coin1 = Coin(400, 80)  # creating the coin objects with the specified x and y coordinates
            self.coinObjects.append(coin1.coin_rect)  # adding each object to the coinObjects list

            coin2 = Coin(650, 80)
            self.coinObjects.append(coin2.coin_rect)

            coin3 = Coin(900, 80)
            self.coinObjects.append(coin3.coin_rect)

            coin4 = Coin(150, 320)
            self.coinObjects.append(coin4.coin_rect)

            coin5 = Coin(355, 320)
            self.coinObjects.append(coin5.coin_rect)

            coin6 = Coin(560, 320)
            self.coinObjects.append(coin6.coin_rect)

            coin7 = Coin(765, 320)
            self.coinObjects.append(coin7.coin_rect)

            coin8 = Coin(1160, 320)
            self.coinObjects.append(coin8.coin_rect)

            coin9 = Coin(330, 680)
            self.coinObjects.append(coin9.coin_rect)

            coin10 = Coin(585, 700)
            self.coinObjects.append(coin10.coin_rect)

            coin11 = Coin(839, 700)
            self.coinObjects.append(coin11.coin_rect)

            coin12 = Coin(1150, 770)
            self.coinObjects.append(coin12.coin_rect)



    def draw(self, screen, player):
        super().draw(screen, player)        # calling the draw method in the parent class
