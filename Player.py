import pygame
from Shot import Shot
from AudioSettings import AudioSettings # this is imported for player sound effects

class Player():
    def __init__(self, x, y):
        self.reset(x,y)
        self.currentlevel = 0
        self.alive = True
        self.coins_collected = 0
        self.lastCheckpoint = (x,y)
        self.lastCheckpointLevel = 0
        self.lives = 3
        self.lives_img = pygame.image.load('heart.png')
        self.in_water = False
        self.col_thresh = 20

    def reset(self, x, y):
        self.right_images = []      # photos of the player when he is looking right
        self.left_images = []       # photos of the player when he is looking left
        self.counter = 0        # for animation speed
        self.index = 0          # for walking throw the list and making the animation

        player_stand_right = pygame.image.load('playerPics\player_stand.png')
        self.player_stand_right = pygame.transform.scale(player_stand_right, (25,25))
        self.player_stand_left = pygame.transform.flip(self.player_stand_right, True, False)

        for i in range(1,9):        # adding player photos to the lists
            img_right = pygame.image.load(f'playerPics\player_walking{i}.png')
            img_right = pygame.transform.scale(img_right, (30,30))
            self.right_images.append(img_right)

            img_left = pygame.transform.flip(img_right, True, False)
            self.left_images.append(img_left)

        self.image = self.player_stand_left     # primary image
        self.rect = self.image.get_rect(topleft = (x,y))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.numberOfJumps = 0      # player is allowed to jump only twice
        self.direction = 0          # in which direction is the player looking, to the left -1, to the right 1
        self.jumpingAllowed = True
        self.shootingAllowed = True
        self.dx = 0
        self.dy = 0
        self.shots = []

    def update(self, screen, lvl, audioSettings):
        self.dx = 0 # as attributes because i want to use them in another classes
        self.dy = 0
        walk_cooldown = 2
        for lives in range(self.lives):
            screen.blit(self.lives_img, (50 + (lives * 40), 10))

        # only when alive, so that the player stops moving when he is dead
        if self.alive:
            key = pygame.key.get_pressed()
            if key[pygame.K_UP] and self.numberOfJumps < 2 and self.jumpingAllowed:     # jumping
                self.jumpingAllowed = False
                if not self.in_water:
                    self.vel_y = -13
                    self.numberOfJumps += 1
                else:
                    self.vel_y = -7
                    self.numberOfJumps = 0
                audioSettings.playSFX('jump') # plays the sound effect from AudioSettings class

            if not key[pygame.K_UP]:            # so that the player won't jump when we keep clicking up
                self.jumpingAllowed = True
            if key[pygame.K_LEFT]:
                if not self.in_water: self.dx -= 5
                else: self.dx -= 3
                self.counter += 1
                self.direction = -1
            if key[pygame.K_RIGHT]:
                if not self.in_water: self.dx += 5
                else: self.dx += 3
                self.counter += 1
                self.direction = 1
            if not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:  # if player is not moving
                self.counter = 0
                self.index = 0
                if self.direction == 1:         # checking what was the last direction
                    self.image = self.player_stand_right
                if self.direction == -1:
                    self.image = self.player_stand_left
            if key[pygame.K_SPACE] and (lvl.bosslevel or lvl.apples) and self.shootingAllowed:  # shooting only allowed in boss levels
                if self.direction == 1:
                    self.shooting((1100, self.rect.centery))    # shooting to the right
                elif self.direction == -1:
                    self.shooting((0, self.rect.centery))       # shooting to the left
                self.shootingAllowed = False         # so that the player won't shoot when we keep clicking space
                audioSettings.playSFX('shooting')  # plays the sound effect from AudioSettings class
            if not key[pygame.K_SPACE]:
                self.shootingAllowed = True         # the bullet is ready to be shot
            if key[pygame.K_b]:         # boss level shortcut
                self.currentlevel = 6

            # animation speed
            if self.counter > walk_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.right_images):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.right_images[self.index]
                if self.direction == -1:
                    self.image = self.left_images[self.index]


            # gravity while in and out water
            if not self.in_water:   self.vel_y += 1
            else:   self.vel_y += .5
            if self.vel_y > 8 and not self.in_water:
                self.vel_y = 8
            elif self.vel_y > 4 and self.in_water:
                self.vel_y = 4
            self.dy += self.vel_y


            # collision with border
            for teil in lvl.border:
                if teil[1].colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
                    # from top side
                    if self.vel_y < 0:
                        self.dy = teil[1].bottom - self.rect.top
                        self.vel_y = 0      # so that the player will stop going upwards
                    # form bottom side
                    else:
                        self.dy = teil[1].top - self.rect.bottom
                        self.numberOfJumps = 0      # so that the player can jump twice again
                if teil[1].colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                    # from right side
                    if self.direction == 1:
                        self.dx = teil[1].left - self.rect.right
                    # from left side
                    else:
                        self.dx = teil[1].right - self.rect.left


            # collision with blocks
            for teil in lvl.blocks:
                if teil[1].colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                    self.dx = 0
                    # collision in the y direction
                if teil[1].colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
                    # check if below platform
                    if abs((self.rect.top + self.dy) - teil[1].bottom) < self.col_thresh and self.currentlevel != 11:
                        self.vel_y = 0
                        self.dy = teil[1].bottom - self.rect.top + 3
                    # check if above platform
                    elif abs((self.rect.bottom + self.dy) - teil[1].top) < self.col_thresh:
                        self.rect.bottom = teil[1].top - 3
                        self.numberOfJumps = 0
                        self.dy = 0


            # if player collides with obstacles he will die
            if self.collisionObstacle(lvl.obstacleObjects):
                self.lives -= 1
                if self.lives == 0:
                    self.alive = False
                else:
                    self.reset(self.lastCheckpoint[0], self.lastCheckpoint[1])
                    self.currentlevel = self.lastCheckpointLevel
                audioSettings.playSFX('gameOver') # plays the sound effect from AudioSettings class


            # if he collides with coins, the counter will go up
            if self.CollisionCoin(lvl):
                self.coins_collected += 1
                audioSettings.playSFX('coinCollect') # plays the sound effect from AudioSettings class

            if self.collisionSavepositions(lvl):
                self.lastCheckpointLevel = self.currentlevel

            # if the level is a boss level and the player collides whith a boss shot, he will die
            if lvl.bosslevel:
                if self.collisionBossShot(lvl):
                    self.lives -= 1
                    self.alive = False
                    audioSettings.playSFX('gameOver') # plays the sound effect from AudioSettings class

            if self.shots and lvl.apples:
                for apple in lvl.apples:
                    for shot in self.shots:
                        if apple.rect.colliderect(shot.rect) and apple in lvl.obstacleObjects:
                            lvl.obstacleObjects.remove(apple)
                            self.shots.remove(shot)

            if lvl.waterBlocks:
                swimming = False
                for water_block in lvl.waterBlocks:
                    if self.rect.colliderect(water_block[1]):
                        self.in_water = True
                        swimming = True
                        break
                    if not swimming:
                        self.in_water = False
            else:   self.in_water = False

            # changing coordinates
            self.rect.x += self.dx
            self.rect.y += self.dy

        screen.blit(self.image, self.rect)

        # moving and drawing player's shots
        for shot in self.shots:
            shot.update()
            shot.render(screen)

    def collisionObstacle(self, obstacles):
        playerPoints = [self.rect.topleft, self.rect.topright, self.rect.bottomleft, self.rect.bottomright,
                        self.rect.midtop, self.rect.midbottom, self.rect.midright, self.rect.midleft]

        # specifiying the three points of the triangle-shaped obstacles
        for obstacle in obstacles:
            if obstacle.id == 1:
                if obstacle.heading == "up":
                    obstaclePoint1 = obstacle.rect.midtop
                    obstaclePoint2 = obstacle.rect.bottomleft
                    obstaclePoint3 = obstacle.rect.bottomright
                elif obstacle.heading == "right":
                    obstaclePoint1 = obstacle.rect.midright
                    obstaclePoint2 = obstacle.rect.topleft
                    obstaclePoint3 = obstacle.rect.bottomleft
                elif obstacle.heading == "left":
                    obstaclePoint1 = obstacle.rect.midleft
                    obstaclePoint2 = obstacle.rect.topright
                    obstaclePoint3 = obstacle.rect.bottomright
                elif obstacle.heading == "down":
                    obstaclePoint1 = obstacle.rect.midbottom
                    obstaclePoint2 = obstacle.rect.topleft
                    obstaclePoint3 = obstacle.rect.topright

                # a mathmatical way to check if a point is inside of a triangle
                obstacleArea = abs((obstaclePoint2[0] - obstaclePoint1[0]) * (obstaclePoint3[1] - obstaclePoint1[1])
                                   - (obstaclePoint3[0] - obstaclePoint1[0]) * (obstaclePoint2[1] - obstaclePoint1[1]))
                # if a point is inside an obstacle of the levels obstacles, that means a collision is detected
                for point in playerPoints:
                    area1 = abs((obstaclePoint1[0] - point[0]) * (obstaclePoint2[1] - point[1])
                                - (obstaclePoint2[0] - point[0]) * (obstaclePoint1[1] - point[1]))
                    area2 = abs((obstaclePoint2[0] - point[0]) * (obstaclePoint3[1] - point[1])
                                - (obstaclePoint3[0] - point[0]) * (obstaclePoint2[1] - point[1]))
                    area3 = abs((obstaclePoint3[0] - point[0]) * (obstaclePoint1[1] - point[1])
                                - (obstaclePoint1[0] - point[0]) * (obstaclePoint3[1] - point[1]))

                    if (area1 + area2 + area3) == obstacleArea:
                        return True
            # if player collides whith rectangle-shaped obstacles (id = 2)
            else:
                if self.rect.colliderect(obstacle.rect):
                    return True
        # if theres no collision with both rectangle and triangle shaped obstacles, return False
        return False

    def CollisionCoin(self, level):
        # if player collides with a coin, remove it from the level, which means it wont be showed anymore
        for coin in level.coinObjects:
            if self.rect.colliderect(coin):
                level.coinObjects.remove(coin)
                return True     # once we find a coin which the player has collided with, we return and add 1 to our counter
        return False

    def collisionBossShot(self, bossLevel):
        # when the player collides with the boss and the boss is alive, because when the boss is dead we are
        # not deleting it but only not showing it, so if the level is done and we collided with the boss, the player wont die
        if int(bossLevel.counter) == 0 or (bossLevel.bossrect.colliderect(self.rect) and not bossLevel.done):
            return True
        # if boss shot touches the player he will die
        for bossshot in bossLevel.bossshoot:
            if self.rect.colliderect(bossshot.rect):
                return True
        return False

    def collisionSavepositions(self, level):
        for save in level.saveObjects:
            if self.rect.colliderect(save.rect):
                save.image.fill('Green')
                if self.currentlevel > self.lastCheckpointLevel:
                    self.lastCheckpoint = (save.x, save.y)
                    return True
                elif self.currentlevel == self.lastCheckpointLevel:
                    if save.y > self.lastCheckpoint[1]:
                        self.lastCheckpoint = (save.x, save.y)
                        return True

    def shooting(self,position):
        shot = Shot(self.rect.x, self.rect.y + self.height//2, position, 'player')
        self.shots.append(shot)

    def restart(self):
        self.reset(1000, 80)
        self.currentlevel = 0
        self.coins_collected = 0
        self.lastCheckpoint = (1000, 80)
        self.lastCheckpointLevel = 0
        self.lives = 3
        self.in_water = False
        self.alive = True


'''
Quellen:
- player animation, gravity and collision with blocks in update method: https://www.youtube.com/@CodingWithRuss
- collisionObstacle algorithm: http://www.jeffreythompson.org/collision-detection/tri-point.php
'''
