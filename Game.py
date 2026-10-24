import pygame

from Menu import Menu
from Player import Player
from AudioSettings import AudioSettings
from Button import Button
from Button2 import Button2
from Level1 import Level1
from Level2 import Level2
from Level3 import Level3
from Level4 import Level4
from Level5 import Level5
from Level6 import Level6
from Level8 import Level8
from Level9 import Level9
from Level10 import Level10
from Level11 import Level11
from Level12 import Level12
from Level13 import Level13
from Level14 import Level14
from Level15 import Level15
from Level16 import Level16
from Bosslevel import Bosslevel

pygame.init()

clock = pygame.time.Clock()
screen_width = 1100
screen_hight = 825

screen = pygame.display.set_mode((screen_width, screen_hight), pygame.FULLSCREEN)
pygame.display.set_caption('I wanna be the explorer')

background_ = pygame.Surface((screen.get_width(), screen.get_height()-825))
background_.fill('Black')
background__ = pygame.Surface((screen.get_width() - 1100, screen.get_height()))
background__.fill('Black')
background = pygame.Surface((1100, 825))

font = pygame.font.Font(pygame.font.get_default_font(), 25)

player = Player(1000, 80)
player_lives = 3           # we are going to need this variable later to check if the value of player.lives has changed
main_menu = Menu(0, 0, 'main_menu.png')
controls_menu = Menu(0,0, "controls_menu.jpg")
controls_menu.activ = False
start_button = Button('PLAY GAME', font, (50, 600), (205, 70))
exit_button = Button('EXIT GAME', font, (50, 700), (205, 70))
controls_button = Button('CONTROLS', font, (300, 600), (205, 70))
back_Button = Button2('Back Button.png', 0, 0, (80,40))

pause_screen = Menu(0, 0, 'background0.png')   # creating a Pause screen from the Menu class
pause_screen.activ = False  # setting the activ attribute to false so that the pause screen would not appear directly after running the game
gameover_screen = Menu(0, 0, 'background0.png')  # creating a Game over screen from the Menu class
gameover_screen.activ = False # setting the activ attribute to false so that the pause screen would not appear directly after running the game

# pause screen attributes
pause_button = Button2('pausebutton.png', 1060, 10, (30,30))  # creating a pause button from Button2 class
continue_button = Button("CONTINUE", font, (500, 400), (205, 70))  # creating a continue button from Button class
restart_button = Button("RESTART", font, (500, 400), (205, 70))    # creating a restart button from Button class
exit_button2 = Button('EXIT GAME', font, (500, 600), (205, 70))    # creating an exit button from Button class

# Game over attributes
buy_life_button = Button('BUY LIFE', font, (500, 500), (205, 70))  # creating a buy life button from Button class
restart_buttonGO = Button('RESTART', font, (500, 600), (205, 70))  # creating a restart button from Button class
exit_buttonGO = Button('EXIT GAME', font, (500, 700), (205, 70))  # creating an exit button from Button class
restart_button3 = Button('RESTART', font, (500, 500), (205, 70))  # restart button with different coordinates for the pause screen

# Buttons for muting and playing background music
soundoff_image  = pygame.image.load('volumeicons/soundoff.png') # load image for mute music button
soundon_image  = pygame.image.load('volumeicons/soundon1.png') # load image for play music button

soundoff_button = Button2('volumeicons/soundoff.png', 970, 50, (30,30)) # create buttons using functionality in Button2 Class
soundon_button = Button2('volumeicons/soundon1.png', 1020, 50, (30, 30)) # create buttons using functionality in Button2 Class

# Create the object for audiosettings where sound effects  and music are specified
audioSettings = AudioSettings() #create the AudioSettings class object
audioSettings.playBGMUSIC('ambience') #play the background music

# You won screen
win_screen = Menu(0, 0, 'background0.png')   # creating a you won screen from the Menu class
win_screen.activ = False  # this helps in the if condition that shows the sound on and off buttons


'''The True value is to determine Whether we are starting the level from the beginning, or we just came back to this 
level due to a save. The diffrence is, that when we come back to a level due a save, we dont want to reset its coins.
True means we are making the whole level, False stands for coming back'''
lvl1 = Level1(True)
lvl2 = Level2(True)
lvl3 = Level3(True)
lvl4 = Level4(True)
lvl5 = Level5(True)
lvl6 = Level6(True)
lvl7_boss = Bosslevel('Bosslevel\dragon.png')
lvl8 = Level8(True)
lvl9 = Level9(True)
lvl10 = Level10(True)
lvl11 = Level11(True)
lvl12 = Level12(True)
lvl13 = Level13(True)
lvl14 = Level14(True)
lvl15 = Level15(True)
lvl16 = Level16(True)
levels = [lvl1, lvl2, lvl3, lvl4, lvl5, lvl6, lvl7_boss, lvl8, lvl9, lvl10, lvl11, lvl12, lvl13, lvl14, lvl15, lvl16]

while True:

    clock.tick(60)
    screen.blit(background, (0, 0))

    '''just changing the background color for the diffrent levels'''
    if player.currentlevel < 7:
        background.fill((117, 242, 255))
    else:
        background.fill((58, 121, 127))

    '''drawing main menu if its 'activ' attribute is True, this attribute changes to false when we start the game'''
    if main_menu.activ:
        main_menu.draw(screen)
        if start_button.draw(screen):   # returns True when the mouse clicks the button
            main_menu.activ = False
        if exit_button.draw(screen):
            pygame.quit()
            exit()
        if controls_button.draw(screen):
            controls_menu.activ = True
        if controls_menu.activ:
            controls_menu.draw(screen)
            if back_Button.draw(screen):
                controls_menu.activ = False

    else:
        '''drawing current level when the start button clicked and main menu not activ'''
        levels[player.currentlevel].draw(screen, player)

        '''set all the levels which we overcame to not Done, so that if we have to come back to one of them due to a save
        we wont go straight ahead to the next level because of the done=True'''
        if player.currentlevel > 0:
            levels[player.currentlevel-1].done = False

        '''showing Coins counter on screen'''
        score_text = font.render('Score: ' + str(player.coins_collected), True, 'White')
        scoretxtrect = score_text.get_rect(topleft=(44, 44))
        screen.blit(score_text, scoretxtrect)

        '''showing level counter on screen:'''
        level_text = font.render('Level: ' + str(player.currentlevel + 1), True, 'White')
        leveltxtrect = level_text.get_rect(topleft=(44, 75))
        screen.blit(level_text, leveltxtrect)

        if not pause_screen.activ:  # so that the player won't move when the game is paused
            '''updating the player movement'''
            player.update(screen, levels[player.currentlevel], audioSettings)

        # pause button
        if not gameover_screen.activ:  # if game over screen is not displayed because if it is displayed the user can still pause when he dies
            if pause_button.draw(screen):  # draws pause button and tests if it is clicked
                pause_screen.activ = True  # when it is clicked the pause screen is displayed

        if pause_screen.activ:  # when game is paused
            pause_screen.draw(screen)  # draw pause screen
            pause_text = font.render('GAME PAUSED', True, (0, 0, 0))  # displayed text on pause screen
            pause_textRect = pause_text.get_rect()  # creates a rect around the pause text
            pause_textRect.center = (600, 300)  # position of the text on screen
            screen.blit(pause_text, pause_textRect)  # blitting the text on the screen

            if continue_button.draw(screen):  # draws conitnue button and when the player clicks on continue the pause screen disappears
                pause_screen.activ = False  # setting the activ value of pause screen to false means that it disappears

            if restart_button3.draw(screen):  # draws restart button onto pause screen and tests if the user clicks on restart
                player.restart()  # taking the player back to the beginning of the game
                player_lives = 3  # resetting the variable we defined at the beginning of the code
                for i in range(len(levels)):
                    if i == 6:
                        levels[i].restart('Bosslevel\dragon.png')
                    else:
                        levels[i].restart(True)  # then we want to restart the whole level including its coins
                pause_screen.activ = False  # pause screen goes away when player clicks on restart

            if exit_button2.draw(screen):  # draws the exit button and tests if player clicks on exit, when yes then the game quits
                pygame.quit()
                exit()


        '''updating player's current level. A level becomes done when the player reachs the bottom of the screen.
        When a level is done, the player position must be changed from the bottom of the screen to the top for 
        the next level'''
        if levels[player.currentlevel].done:
            if player.currentlevel < len(levels)-1:         # if we didn't reach the last level yet
                player.currentlevel += 1
                if not levels[player.currentlevel].bosslevel:       # if we are not in a boss level
                    player.reset(player.rect.x, 30)         # changing the player coordinates
                else:            # in boss levels
                    player.reset(60, 500)
            else:       # you won

                win_screen.activ = True  # means the you won screen is now active
                win_screen.draw(screen)  # draws you won screen
                win_text = font.render('You won!', True, (0, 0, 0))  # prints a message when the player wins in color black

                win_textRect = win_text.get_rect()  # creates a rect around the text
                win_textRect.center = (600, 300)  # position of the text on the screen
                screen.blit(win_text, win_textRect)  # blits the message into the screen

                if restart_button3.draw(screen):  # when user clicks on restart
                    player.restart()  # taking the player back to the beginning of the game
                    player_lives = 3  # resetting the variable we defined at the beginning of the code
                    for i in range(len(levels)):
                        if i == 6:
                            levels[i].restart('Bosslevel\dragon.png')
                        else:
                            levels[i].restart(True)  # then we want to restart the whole level including its coins

                    win_screen.activ = False

                if exit_button2.draw(screen):  # when player clicks on exit, quit the game
                    pygame.quit()
                    exit()


        ''' because there is moving objects in the levels, so when the player dies we want to restart all the levels which
        the player has played beginning from the last level in which the player saved till the end, so that 
        when we go back to a that level, all moving objects will be placed back to their origanal place '''
        if player_lives != player.lives:        # check if player has died
            player_lives = player.lives
            if player.lives != 0:               # if player has died but he still have lives..
                for i in range(player.lastCheckpointLevel, len(levels)):
                    if i == 6:
                        levels[i].restart('Bosslevel\dragon.png')
                    else:
                        levels[i].restart(False)        # then we dont want to reset the coins in the level (False)

        '''Case 1: when player dies and the coins collected are at least 2 (he can buy a life for 2 coins, restart , 
         or exit the game)'''
        if not player.alive and player.coins_collected >= 2:  # if he has no more lives (game over).
            # the following lines of codes is used to keep the pause button on the screen after the player buys a life
            if not gameover_screen.activ and not main_menu.activ:  # if game over screen is not displayed because if it is displayed the user can still pause when he dies
                if pause_button.draw(screen):  # draws pause button and tests if it is clicked
                    pause_screen.activ = True  # when it is clicked the pause screen is displayed
                pause_button.draw(screen)  # draws pause button
            gameover_screen.activ = True  # this means the game over screen is displayed
            gameover_screen.draw(screen)  # this displays the game over screen
            lost_text1 = font.render('You lost!', True, (0, 0, 0))  # prints a message when the player loses in color black
            lost_text2 = font.render('Do you wanna buy a life for 2 coins or restart?', True, (0, 0, 0))  # asks the player if he wants to buy a life

            lost_textRect1 = lost_text1.get_rect()  # creates a rect around the first text
            lost_textRect1.center = (600, 300)  # position of the text on the screen
            screen.blit(lost_text1, lost_textRect1)  # blits the message into the screen

            lost_textRect2 = lost_text2.get_rect()  # creates a rect around the second text
            lost_textRect2.center = (600, 400)  # position of the text on the screen
            screen.blit(lost_text2, lost_textRect2)  # blits the message into the screen
            if restart_buttonGO.draw(screen):  # when user clicks on restart
                player.restart()  # taking the player back to the beginning of the game
                player_lives = 3  # resetting the variable we defined at the beginning of the code
                for i in range(len(levels)):
                    if i == 6:
                        levels[i].restart('Bosslevel\dragon.png')
                    else:
                        levels[i].restart(True)  # then we want to restart the whole level including its coins

                gameover_screen.activ = False  # game over screen goes away when player clicks restart

            if buy_life_button.draw(screen):  # if user clicked on buy a life button
                player.reset(player.lastCheckpoint[0], player.lastCheckpoint[1])  # the player is revived and goes back to the last check point
                player.currentlevel = player.lastCheckpointLevel  # sets the current level to the last checkpoint 's level
                player.coins_collected -= 2  # the score of coins is reduced by 2 coins
                player.alive = True  # revival of player
                player.lives += 1  # increase the lives by 1
                for lives in range(player.lives):  # blitting the heart images that represents the lives on the screen
                    screen.blit(player.lives_img, (50 + (lives * 40), 10))

                gameover_screen.activ = False

            if exit_buttonGO.draw(screen):  # when player clicks on exit, quit the game
                pygame.quit()
                exit()

        '''Case 2: when player dies and the coins collected are less than 2 (he cant buy a life, he only has the choice to 
        restart or exit)'''
        if not player.alive and player.coins_collected < 2:
            gameover_screen.activ = True  # means the game over screen is now active
            gameover_screen.draw(screen)  # draws game over screen
            lost_text1 = font.render('You lost!', True,
                                     (0, 0, 0))  # prints a message when the player loses in color black
            lost_text2 = font.render('You don\'t have enough coins to buy a life!', True, (0, 0, 0))

            lost_textRect1 = lost_text1.get_rect()  # creates a rect around the first text
            lost_textRect1.center = (600, 300)  # position of the text on the screen
            screen.blit(lost_text1, lost_textRect1)  # blits the message into the screen

            lost_textRect2 = lost_text2.get_rect()  # creates a rect around the second text
            lost_textRect2.center = (600, 400)  # position of the text on the screen
            screen.blit(lost_text2, lost_textRect2)  # blits the message into the screen

            if restart_button3.draw(screen):  # when user clicks on restart
                player.restart()  # taking the player back to the beginning of the game
                player_lives = 3  # resetting the variable we defined at the beginning of the code
                for i in range(len(levels)):
                    if i == 6:
                        levels[i].restart('Bosslevel\dragon.png')
                    else:
                        levels[i].restart(True)  # then we want to restart the whole level including its coins

                gameover_screen.activ = False

            if exit_button2.draw(screen):  # when player clicks on exit, quit the game
                pygame.quit()
                exit()           # then we want to restart the whole level including its coins

        # Mute and Music On buttons fuctionality. It draws the sound buttons on the screen and works under specified conditions
        # If Sound On Button is clicked: the playBGMUSIC function from audioSettings is triggered and will play the ambience sound that was specified in the dictionary


    if not pause_screen.activ and not gameover_screen.activ and not main_menu.activ and not win_screen.activ:  # sound buttons do not show when the player pauses the game or dies
            if soundon_button.draw(screen):
                audioSettings.playBGMUSIC('ambience') #if the sound on button is clicked, play music
            # If Sound Off Button is clicked: the muteBGMUSIC function from audioSettings is triggered and will mute the ambience sound
            if soundoff_button.draw(screen) and not soundon_button.draw(screen):
                audioSettings.muteBGMUSIC('ambience') #if the sound off button is clicked, mute music

    screen.blit(background_, (0, 825))
    screen.blit(background__, (1100, 0))

    for event in pygame.event.get(): #event loop

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()


# Resources
# pause button image: https://www.pngitem.com/middle/iomoTow_gold-brown-plain-pause-button-icon-svg-clip/
# coin images: https://opengameart.org/content/rotating-coin-0
# heart image : https://opengameart.org/content/heart-1616
# game paused/game over background: https://opengameart.org/content/backgrounds-for-2d-platformers
# playlist link on youtube: https://www.youtube.com/watch?v=Ongc4EVqRjo&list=PLjcN1EyupaQnHM1I9SmiXfbT6aG4ezUvu

