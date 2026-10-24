import pygame
import CoinAnimation

# all levels extend this class, so that we won't need to define the common attributes in each class level
class Level():
    def __init__(self):
        # common attributes for all levels
        self.border = []
        self.obstacleObjects = []
        self.saveObjects = []
        self.blocks = []
        self.stones = []
        self.hidden_path = []
        self.border_to_be_removed = []
        self.decoration = []
        self.apples = []
        self.waterBlocks = []
        self.done = False
        self.bosslevel = False

        '''The following lines of codes are responsible for the coins. A list of coins is created which 
        consists of the coin images, then the size of the coins is made smaller to 15 by 15 pixels'''
        coins = []
        for i in range(6):
            coin = pygame.image.load(f'coinspics/coin{i}.png')  # uploading the images
            coin = pygame.transform.scale(coin, (15, 15))  # changing the size of the images
            coins.append(coin)  # appending the smaller coins images to the list coins

        self.coin_animation = CoinAnimation.CoinAnimation(coins)  # creating an object form class coinAnimation and passing the ocins list as parameter

    def draw(self, screen, player):     # drawing the level

        for tile in self.waterBlocks:
            screen.blit(tile[0], tile[1])

        for tile in self.decoration:
            screen.blit(tile[0], tile[1])

        for tile in self.obstacleObjects:
            screen.blit(tile.obstacleImage, tile.rect)

        for tile in self.blocks:
            screen.blit(tile[0], tile[1])

        for c in self.coinObjects:  # loops through list of ocins that were added in each level
            self.coin_animation.draw(screen, c.x, c.y)  # draws each coin into the screen based on the given x and y coordinates
        self.coin_animation.update()  # animates the coin by calling the update method from CoinAnimation class

        for tile in self.border:
            screen.blit(tile[0], tile[1])

        for tile in self.saveObjects:
            screen.blit(tile.image, tile.rect)

        # when the player if off screen
        if player.rect.y >= 825:
            self.done = True




