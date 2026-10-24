import pygame

class Button:

    def __init__(self, text, font, pos, size):
        self.text = text
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), size)
        self.font = font

    def draw(self, screen):
        pygame.draw.rect(screen, 'yellow', self.button, 0, 50)
        pygame.draw.rect(screen, 'black', self.button, 5, 50)
        text = self.font.render(self.text, True, 'black')
        screen.blit(text, (self.pos[0] + 30, self.pos[1] + 25))
        # checked Mouseclick
        action = False
        if self.button.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:      # left mouse click
                action = True
        return action
