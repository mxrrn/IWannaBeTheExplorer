import pygame

from Level import Level
from Obstacle import Obstacle

class Level14(Level):

    def __init__(self,game_over):
        self.coinObjects = []
        self.restart(game_over)
        self.stones_conditions = [0]*21



    def restart(self, game_over):

        super().__init__()
        self.stones_conditions = [0]*21

        wall_up = pygame.image.load('level14pics/wall_up.jpg')
        wall_up_rect = wall_up.get_rect(topleft=(0, 0))
        self.border.append((wall_up, wall_up_rect))

        wall_right = pygame.image.load('level14pics/wall_right.jpg')
        wall_right = pygame.transform.scale(wall_right, (44, 825))
        wall_right_rect = wall_right.get_rect(topright=(1100, 0))
        self.border.append((wall_right, wall_right_rect))

        wall_left = pygame.image.load('level14pics/wall_left.jpg')
        wall_left = pygame.transform.scale(wall_left, (44, 825))
        wall_left_rect = wall_left.get_rect(topleft=(0, 0))
        self.border.append((wall_left, wall_left_rect))

        wall_down1 = pygame.image.load('level14pics/wall_down.jpg')
        wall_down1 = pygame.transform.scale(wall_down1, (308, 33))
        wall_down1_rect = wall_down1.get_rect(bottomright= wall_right_rect.bottomleft)
        self.border.append((wall_down1, wall_down1_rect))

        wall_down2 = wall_down1
        wall_down2_rect = wall_down2.get_rect(bottomright=wall_down1_rect.bottomleft)
        self.border.append((wall_down2, wall_down2_rect))

        wall_down3 = wall_down1
        wall_down3_rect = wall_down3.get_rect(bottomright=wall_down2_rect.bottomleft)
        self.border.append((wall_down3, wall_down3_rect))


        # obstacles and stones:
        stones = pygame.image.load('level3pics/stone.jpg')
        stones = pygame.transform.scale(stones, (44, 46))

        for i in range(21):
            obstacle = Obstacle("up", 1, "bottomright", (44, 44), (wall_down1_rect.topright[0] - i * 44, wall_down1_rect.topright[1]))
            self.obstacleObjects.append(obstacle)

            stone = stones
            stone_rect = stone.get_rect(bottomright=(wall_down1_rect.topright[0] - i * 44, wall_down1_rect.topright[1]))
            self.stones.append((stone, stone_rect))



    def draw(self, screen, player):

        super().draw(screen, player)

        for i in range(len(self.stones)):
            if self.stones[i][1].colliderect(player.rect.x, player.rect.y + player.dy, player.width, player.height):
                if self.stones_conditions[i] == 0:
                    self.stones_conditions[i] += 1

        for i in range(len(self.stones_conditions)):
            if self.stones_conditions[i] == 1:
                self.border.append(self.stones[i])
                self.stones_conditions[i] += 1
