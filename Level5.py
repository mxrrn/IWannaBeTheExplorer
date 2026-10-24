import pygame

from Coin import Coin
from Level import Level


class Level5(Level):
    def __init__(self, game_over):
        self.coinObjects = []
        self.restart(game_over)

    def restart(self, game_over):

        super().__init__()

        wall_right = pygame.image.load('level5pics/wall_right_left.jpg')
        wall_right_rect = wall_right.get_rect(bottomright=(1100, 825))
        self.border.append((wall_right, wall_right_rect))

        wall_left = wall_right
        wall_left_rect = wall_left.get_rect(bottomleft=(0, 825))
        self.border.append((wall_left, wall_left_rect))


        # coins:

        if game_over:

            self.coinObjects = []

            coin1 = Coin(539, 130)
            self.coinObjects.append(coin1.coin_rect)

            coin2 = Coin(539, 260)
            self.coinObjects.append(coin2.coin_rect)

            coin3 = Coin(539, 390)
            self.coinObjects.append(coin3.coin_rect)

            coin4 = Coin(539, 520)
            self.coinObjects.append(coin4.coin_rect)

            coin5 = Coin(539, 650)
            self.coinObjects.append(coin5.coin_rect)

            coin6 = Coin(539, 780)
            self.coinObjects.append(coin6.coin_rect)


    def draw(self, screen, player):

        super().draw(screen, player)