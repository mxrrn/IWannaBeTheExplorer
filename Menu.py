import pygame

class Menu:
    def __init__(self, x, y, image):

        image = pygame.image.load(image)
        self.image = pygame.transform.scale(image, (1100,826))
        self.x = x
        self.y = y
        self.activ = True       # means that we are in main menu now

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))



