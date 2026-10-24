import pygame.image


class SavePosition():

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.image = pygame.Surface((30, 30))
        self.image.fill('dark red')
        self.rect = self.image.get_rect(center=(self.x, self.y))

