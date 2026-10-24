import pygame
'''This class is responsible for creating coin objects. To create a coin object from this class, it should take the x and y 
coordinates as parameters.'''

class Coin():

    def __init__(self, x, y):

        self.coin_img = pygame.image.load('coinspics/coin0.png')    # load the coin image
        self.coin_rect = self.coin_img.get_rect()                   # creating a rect object from the coin image
        self.coin_rect.x = x                                        # specifying x and y values (coordinates)
        self.coin_rect.y = y



