# Resources:
# coin animation class: https://youtu.be/1e4BxUbhJKU
'''The main funciton of this class is to animate the coins. When creating an object from this class, a list must
be passed as parameter (list of coin images in this case). Then, once an object is created, an index variable, that
will help us to loop through the images in the coin images list, as well as an animtion tiemr and speed will be created.'''


class CoinAnimation:

    def __init__(self, coin_images_list):  # it takes a list as parameter
        self.coin_images_list = coin_images_list
        self.img_index = 0  # to loop through the images in coin images list
        self.animation_timer = 0  # to help us with animation
        self.animation_speed = 10  # the lower the number the faster the coins turn

    def update(self):
        self.animation_timer += 1  # increments until 10 (animation speed)
        if self.animation_timer >= self.animation_speed:  # when it reaches 10, it is set back to 0
            self.animation_timer = 0  # set timer back to 0(to go again from 0 to 10 in the next image or frame in the list)
            self.img_index += 1  # to go to the next coin image in the list, but the index keeps incrementing until the last image
            if self.img_index > len(self.coin_images_list) - 1:  # when the index reaches the last image in the list (here len -1 because the length of a list is 1 more than the last index)
                self.img_index = 0  # go back to the first image in the list

    # this function draws each coin to the screen according to the given x and y coordinates
    def draw(self, screen, x, y):
        screen.blit(self.coin_images_list[self.img_index], (x, y))
