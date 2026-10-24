import pygame

# Resources:
# Pygame mixer music Documentation https://www.pygame.org/docs/ref/music.html
# Music source https://garoslaw.itch.io/monolith-ost?download
# Background Song https://www.youtube.com/watch?v=aTYVdK3GNxI&list=LL&index=19&t=367s
# Soundeffects source https://maskedsound.itch.io/8-bit-sfx-pack?download
# Channel Guide https://www.youtube.com/@RikCross

class AudioSettings():
    def __init__(self):
            pygame.mixer.init() #initialize pygame mixer library to work with music

            # Volume can generally be specified between 0 - 1
            self.sfxVolume = 0.4 # sound effects volume
            self.musicVolume = 0.2 # music volume
            self.muteVolume = 0 # muted volume for mute function

            # Dictionary for specifying sound effects to certain movements in the game, this allows us to access specific sounds later when calling the sound effects function
            self.sfx = {
                # create sound name in keys
                # calling pygame.mixer.sound in values will create the sound + specify sound file path in the parameters
                'jump' : pygame.mixer.Sound('audio/OGG/03_Jump_v1.ogg'),
                'coinCollect' : pygame.mixer.Sound('audio/OGG/01_Coin Pickup_v1.ogg'),
                'death' : pygame.mixer.Sound('audio/OGG/01_Death_v3.ogg'),
                'gameOver' : pygame.mixer.Sound('audio/OGG/04_Game Over_v3.ogg'),
                'shooting': pygame.mixer.Sound('audio/OGG/01_Laser_v1.ogg'),
                'dragonfire': pygame.mixer.Sound('audio/OGG/01_Punch_v2.ogg'),
            }

            # Dictionary for specifying specific music. This is specifically for Background Music
            self.music = {
                # create sound name in keys
                # give the sound file path in values (this works the same way as self.sfx except for changes in the functions below)
                'ambience' : 'audio/ambience.wav',
                # 'bossmusic' : 'audio/BGMUSIC/13 Challenger.ogg',
                # 'deathScreen' : 'audio/BGMUSIC/26 Ruin.ogg',
            }


    def playBGMUSIC(self, audioname):
        # play background music function using the self.music Dictionary

        pygame.mixer.music.load(self.music[audioname]) #load the music + give the audioname in the parameters when used in Game class.
        pygame.mixer.music.set_volume(self.musicVolume) #specifies the music volume but the settings are set within the attributes
        pygame.mixer.music.play(-1) # (-1) loops the music
        self.musicMute = False


    def muteBGMUSIC(self, audioname):
        #mute background music function using the self.music Dictionary

        pygame.mixer.music.load(self.music[audioname]) #load the music  + give the audioname in the parameters when used in Game class.
        pygame.mixer.music.set_volume(self.muteVolume) #specify the music volume which is 0 in this case
        pygame.mixer.music.play(-1) # ensures that the music plays on loop but the volume is set at 0
        self.musicMute = True

    def playSFX(self, sfxname):
        #game sound effects mainly for the player´s movements. This function is mainly accessed in Player class
        self.sfx[sfxname].set_volume(self.sfxVolume)
        self.sfx[sfxname].play()

