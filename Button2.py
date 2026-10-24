'''
This class is used to create a button as an icon. It takes the path , coordinates, and the size of the image.
It also draws the button into the screen and tests if the player clicked on the butoon with the mouse.
'''

import pygame


class Button2:

    def __init__(self, img, x, y, size):
        img = pygame.image.load(img)  # load image given in parameter
        self.image = pygame.transform.scale(img, size)  # change size of image
        self.x = x  # x coordinate
        self.y = y  # y coordinate
        self.button = pygame.rect.Rect((self.x, self.y), size)  # button attribute that has the coordinates and size

    def draw(self, screen):  # this function draws the button into the screen and checks if the player clicked on it
        screen.blit(self.image, (self.x, self.y))

        #check if there is a mouse click
        action = False  # mous clikc is false at the beginning
        if self.button.collidepoint(pygame.mouse.get_pos()):  # when player clicks on the button(when there is a collision )
            if pygame.mouse.get_pressed()[0]:    # left mouse click
                action = True  # mouse is clicked
        return action  # in order to test with an if conditoin in the main game loop