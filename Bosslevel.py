import pygame
from Level import Level
from Shot import Shot
from AudioSettings import AudioSettings


class Bosslevel(Level):
    def __init__(self, image):
        self.coinObjects = []
        self.restart(image)
        self.counter = 30 #timer
        self.image = pygame.image.load(image)
        self.bossrect = self.image.get_rect(bottomright = (1056,781))
        self.bosshealth = 800
        self.bosslevel = True
        self.bossshoot = []         # list of all boss shots
        self.shoot_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.shoot_timer, 750)
        self.counter_font = pygame.font.Font(pygame.font.get_default_font(), 25)


    def restart(self, image):

        super().__init__()
        self.counter = 30 #timer
        self.image = pygame.image.load(image)
        self.bossrect = self.image.get_rect(bottomright = (1056,781))
        self.bosshealth = 800
        self.bosslevel = True
        self.bossshoot = []         # list of all boss shots
        self.shoot_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.shoot_timer, 750)
        self.counter_font = pygame.font.Font(pygame.font.get_default_font(), 25)


        wall_up = pygame.image.load('level1pics/wall_up.jpg')
        wall_up_rect = wall_up.get_rect(topleft = (0,0))
        self.border.append((wall_up, wall_up_rect))
        wall_right = pygame.image.load('level2pics/wall_right.jpg')
        wall_right_rect = wall_right.get_rect(topright=(1100, 0))
        self.border.append((wall_right, wall_right_rect))
        wall_left = pygame.image.load('level3pics/wall_left.jpg')
        wall_left_rect = wall_left.get_rect(topleft=(0, 0))
        self.border.append((wall_left, wall_left_rect))
        wall_bottomright = pygame.image.load('Bosslevel/wall_bottomright-left.jpg')
        wall_bottomright_rect = wall_bottomright.get_rect(bottomright=(1100, 825))
        self.border.append((wall_bottomright, wall_bottomright_rect))
        wall_bottomleft = wall_bottomright
        wall_bottomleft_rect = wall_bottomleft.get_rect(bottomleft=(0, 825))
        self.border.append((wall_bottomleft, wall_bottomleft_rect))
        wall_midbottom = pygame.image.load('Bosslevel/wall_midbottom.jpg')
        wall_midbottom_rect = wall_midbottom.get_rect(bottomright = wall_bottomright_rect.bottomleft)
        self.border.append((wall_midbottom, wall_midbottom_rect))
        self.border_to_be_removed.append((wall_midbottom, wall_midbottom_rect))

    def draw(self,screen, player):
        super().draw(screen, player)

        # drawing healthbar
        healthbar = pygame.Rect(150, 10, self.bosshealth, 20)
        pygame.draw.rect(screen, 'Red', healthbar)
        # drawing timer
        timer_text = self.counter_font.render(str(int(self.counter)), True, 'Black')
        timertxtrect = timer_text.get_rect(midtop=(550, 44))
        screen.blit(timer_text, timertxtrect)

        for bossshot in self.bossshoot:  # moving and showing all shots
            bossshot.update()
            bossshot.render(screen)

        # if the boss is still alive
        if self.bosshealth != 0:
            if player.alive:
                self.counter -= 0.01666667
                for shot in player.shots:           # when player shoots the boss, boss health will be decreased
                    if self.bossrect.colliderect(shot.rect):
                        self.bosshealth -= 40
                        player.shots.remove(shot)       # otherwise every shot will be hitting the boss multiple times
                for event in pygame.event.get():
                    if event.type == self.shoot_timer:
                        self.shooting(player.rect.center)
            # showing boss only when e is alive
            screen.blit(self.image, self.bossrect)
        else:   # if boss dead
            for tile in self.border_to_be_removed:
                if tile in self.border:
                    self.border.remove(tile)
    def shooting(self, player_pos):
        shot = Shot(self.bossrect.x - 25, self.bossrect.y + 140, player_pos, 'dragon')
        self.bossshoot.append(shot)


'''
Quellen:
- boss shooting timer: https://www.youtube.com/@ClearCode
'''