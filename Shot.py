import pygame
import math

class Shot:

    def __init__(self, x, y, target, shooter):
        self.x = x
        self.y = y
        self.target = target
        self.shooter = shooter
        if self.shooter == 'player':    # player shots
            self.image = pygame.Surface((5, 5))
            self.image.fill('dark red')
            self.rect = self.image.get_rect(center = (self.x, self.y))
        elif self.shooter == 'dragon':      # dragon shots
            image = pygame.image.load('Bosslevel\dragonfire.png')
            self.image = pygame.transform.scale(image, (75,40))
            self.rect = self.image.get_rect(center = (self.x, self.y))

        # Calculate direction and velocity to the target
        dx, dy = self.target[0] - x, self.target[1] - y

        dist = math.hypot(dx, dy)       # sqrt((x2 - x1)^2 + (y2 - y1)^2)
        self.vx = dx / dist * 5  # 5 pixels per frame
        self.vy = dy / dist * 5

    def update(self):       # moving the shot
        self.rect.x += self.vx
        self.rect.y += self.vy

    def render(self, screen):   # showing the shot
        if self.shooter == "player" :
            screen.blit(self.image, self.rect)
        if self.shooter == "dragon":
            screen.blit(self.image, self.rect)
