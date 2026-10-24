import pygame

class Obstacle():

    def __init__(self, heading, obstacleID, point, size, position):
        '''
        point parameter:
        top, left, bottom, right
        topleft, bottomleft, topright, bottomright
        midtop, midleft, midbottom, midright
        center, centerx, centery
        '''
        self.id = obstacleID        # every id represents a certain obstacle type(photo)
        self.heading = heading      # represents the direction that the obstacles is heading to

        if self.id == 1:
            obstacleImage = pygame.image.load('obstaclesPics/triangle_obstacle.png').convert_alpha()
            self.obstacleImage = pygame.transform.scale(obstacleImage, size)
        elif self.id == 2:
            obstacleImage = pygame.image.load('obstaclesPics/rectangle_obstacle.PNG').convert_alpha()
            self.obstacleImage = pygame.transform.rotate(obstacleImage, 270)
        elif self.id == 3:
            self.obstacleImage = pygame.image.load('level9pics/apple.PNG').convert_alpha()

        # rotating the photo based on the direction that was given as parameter
        if self.heading == "right":
            self.obstacleImage = pygame.transform.rotate(self.obstacleImage, 270)
        elif self.heading == "down":
            self.obstacleImage = pygame.transform.rotate(self.obstacleImage, 180)
        elif self.heading == "left":
            self.obstacleImage = pygame.transform.rotate(self.obstacleImage, 90)

        # creating rectangle of the photo.
        # point parameter represents the point which we will be using for moving the rect
        # position is a tuple which the point will be having as a value
        self.pointIdentification(point, position)


    def pointIdentification(self, point, position):

        if point == "topleft":
            self.rect = self.obstacleImage.get_rect(topleft=position)
        elif point == "topright":
            self.rect = self.obstacleImage.get_rect(topright=position)
        elif point == "bottomleft":
            self.rect = self.obstacleImage.get_rect(bottomleft=position)
        elif point == "bottomright":
            self.rect = self.obstacleImage.get_rect(bottomright=position)
        elif point == "midtop":
            self.rect = self.obstacleImage.get_rect(midtop=position)
        elif point == "midleft":
            self.rect = self.obstacleImage.get_rect(midleft=position)
        elif point == "midbottom":
            self.rect = self.obstacleImage.get_rect(midbottom=position)
        elif point == "midright":
            self.rect = self.obstacleImage.get_rect(midright=position)
        elif point == "center":
            self.rect = self.obstacleImage.get_rect(center=position)


