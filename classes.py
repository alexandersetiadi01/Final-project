import pygame as pg
from setting import *
import menu
import random


class Platform(pg.sprite.Sprite):
    def __init__(self, filename, x, y, w, h):                     # set the parameter of the class
        pg.sprite.Sprite.__init__(self)                           # inherit

        self.image = pg.image.load(filename)                      # load image
        self.image = pg.transform.scale(self.image, (w, h))       # transform image size
        self.rect = self.image.get_rect()                         # get image rectangle
        self.rect.x = x                                           # coordinate x
        self.rect.y = y                                           # coordinate y


class Meteor(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):                               # set the parameter of the class
        pg.sprite.Sprite.__init__(self)                           # inherit

        self.image = pg.image.load(image_meteor)                  # load image
        self.image = pg.transform.scale(self.image, (w, h))       # transform image size
        self.rect = self.image.get_rect()                         # get image rectangle
        self.rect.x = x                                           # coordinate x
        self.rect.y = y                                           # coordinate y

    def update(self):                                             # update function
        self.rect.y += speed                                      # increase rect.y by speed
        if self.rect.y > 660:                                     # if rect.y is more 660
            self.rect.y = random.randint(-500, -200)              # reset rect.y to random between -600 to -200
            #-300


class Coin(pg.sprite.Sprite):
    def __init__(self, x, y):                                     # set the parameter of the class
        pg.sprite.Sprite.__init__(self)                           # inherit
        self.image = pg.image.load(image_coin)
        self.image = pg.transform.scale(self.image, (25, 25))     # load image
        self.rect = self.image.get_rect()                         # transform image size
        self.rect.x = x                                           # get image rectangle
        self.rect.y = y                                           # coordinate x


class Detector(pg.sprite.Sprite):
    def __init__(self, x, w, h):                                  # set the parameter of the class
        pg.sprite.Sprite.__init__(self)                           # inherit
        self.image = pg.image.load(image_detector)                # load image
        self.image = pg.transform.scale(self.image, (w, h))       # transform image size
        self.rect = self.image.get_rect()                         # get image rectangle
        self.rect.x = x                                           # coordinate x
        self.rect.y = 3000                                        # coordinate y


class Safe_house(pg.sprite.Sprite):
    def __init__(self,  filename, x, y):                           # set the parameter of the class
        pg.sprite.Sprite.__init__(self)                            # inherit

        self.image = pg.image.load(filename)                       # load image
        self.image = pg.transform.scale(self.image, (300, 300))    # transform image size
        self.rect = self.image.get_rect()                          # get image rectangle
        self.rect.x = x                                            # coordinate x
        self.rect.y = y                                            # coordinate y


class Level(object):
    def __init__(self, character):
        self.platforms_list = pg.sprite.Group()                    # group for platform
        self.meteor_list = pg.sprite.Group()                       # group for meteor
        self.detector_list = pg.sprite.Group()                     # group for detector
        self.coin_list = pg.sprite.Group()                         # group for coin
        self.safe_house_list = pg.sprite.Group()                   # group for safe house

        self.character = character

        self.world_shift_x = 0                                     # set world_shift_x to 0
        self.world_shift_y = 0                                     # set world_shift_y to 0

        self.left_shift = screen_width/2 - screen_width/8          # set the left_shift according this calculation
        self.right_shift = screen_width/4 + screen_width/10        # set the right_shift according this calculation
        self.down_shift = screen_height / 4 + screen_height / 10   # set the down_shift according this calculation
        self.up_shift = screen_height / 4                          # set the up_shift according this calculation

    def update(self):
        self.platforms_list.update()                               # update all sprite inside group
        self.meteor_list.update()                                  # update all sprite inside group
        self.coin_list.update()                                    # update all sprite inside group
        self.detector_list.update()                                # update all sprite inside group
        self.safe_house_list.update()                              # update all sprite inside group

    # shift the map and all of the platform according to character movement
    def moving_world(self, shift_x, shift_y):
        self.world_shift_x += shift_x
        self.world_shift_y += shift_y

        for all_platform in self.platforms_list:
            all_platform.rect.x += shift_x
            all_platform.rect.y += shift_y
        for all_meteor in self.meteor_list:
            all_meteor.rect.x += shift_x
            all_meteor.rect.y += shift_y
        for all_coin in self.coin_list:
            all_coin.rect.x += shift_x
            all_coin.rect.y += shift_y
        for all_detector in self.detector_list:
            all_detector.rect.x += shift_x
            all_detector.rect.y += shift_y
        for all_safe_house in self.safe_house_list:
            all_safe_house.rect.x += shift_x
            all_safe_house.rect.y += shift_y

    # character's point of view when the shift happens
    def point_of_view(self):
        # horizontal
        if self.character.rect.x <= self.left_shift:
            view = self.left_shift - self.character.rect.x
            self.character.rect.x = self.left_shift
            self.moving_world(view, 0)
        if self.character.rect.x >= self.right_shift:
            view = self.right_shift - self.character.rect.x
            self.character.rect.x = self.right_shift
            self.moving_world(view, 0)

        # vertical
        if self.character.rect.y <= self.up_shift:
            view = self.up_shift - self.character.rect.y
            self.character.rect.y = self.up_shift
            self.moving_world(0, view)
        if self.character.rect.y >= self.down_shift:
            view = self.down_shift - self.character.rect.y
            self.character.rect.y = self.down_shift
            self.moving_world(0, view)

    def blitme(self, screen):
        self.platforms_list.draw(screen)                           # draw all images in this group
        self.meteor_list.draw(screen)                              # draw all images in this group
        self.coin_list.draw(screen)                                # draw all images in this group
        self.safe_house_list.draw(screen)                          # draw all images in this group


class Level_01(Level):
    def __init__(self, character):                                 # parameter for class
        super(Level_01, self).__init__(character)                  # super class

        # platform list of images
        plat = [[image_longland, 10, 300, 150, 50],
                 [image_longland, 450, 450, 150, 50],
                 [image_longland, 600, 300, 150, 50],
                 [image_longland, 800, 450, 150, 50],
                 [image_longland, 1000, 250, 150, 50],
                 [image_longland, 1400, 500, 150, 50],
                 [image_longland, 1600, 350, 150, 50],
                 [image_longland, 1900, 500, 150, 50],
                 [image_longland, 2350, 500, 150, 50],
                 [image_longland, 2550, 400, 150, 50],
                 [image_longland, 2800, 600, 600, 50],
                 [image_longland, 3650, 500, 100, 50],
                 [image_longland, 3850, 400, 100, 50],
                 [image_longland, 4100, 300, 150, 50],
                 [image_longland, 4350, 200, 150, 50],
                 [image_longland, 4950, 800, 350, 50],
                 [image_longland, 5450, 650, 200, 50],
                 [image_longland, 5950, 650, 200, 50],
                 [image_longland, 6200, 500, 150, 50],
                 ]

        # coins list of images
        coins = [[300, 200], [360, 260], [675, 250], [870, 435],
                 [870, 150], [1200, 100], [1380, 300], [1550, 100],
                 [1850, 100], [1950, 450], [2200, 235], [2400, 300],
                 [2600, 350], [2850, 480], [3050, 480], [3500, 450],
                 [4000, 240], [4300, 100], [4800, 270], [4924, 370],
                 [5300, 460], [5600, 450], [5900, 450], [6000, 450]
                 ]

        # meteor list of images
        meteor = [[200, random.randint(-500, -200), 90, 90],
                    [600, random.randint(-500, -200), 90, 90],
                    [900, random.randint(-500, -200), 90, 90],
                    [1300, random.randint(-500, -200), 90, 90],
                    [1550, random.randint(-500, -200), 90, 90],
                    [1700, random.randint(-500, -200), 90, 90],
                    [2000, random.randint(-500, -200), 90, 90],
                    [2300, random.randint(-500, -200), 90, 90],
                    [2450, random.randint(-500, -200), 90, 90],
                    [2600, random.randint(-500, -200), 90, 90],
                    [2850, random.randint(-500, -200), 90, 90],
                    [3100, random.randint(-500, -200), 90, 90],
                    [3450, random.randint(-500, -200), 90, 90],
                    [3950, random.randint(-500, -200), 90, 90],
                    [4200, random.randint(-500, -200), 90, 90],
                    [4500, random.randint(-500, -200), 90, 90],
                    [4850, random.randint(-500, -200), 90, 90],
                    [5170, random.randint(-500, -200), 90, 90],
                    [5400, random.randint(-500, -200), 90, 90],
                    [5800, random.randint(-500, -200), 90, 90]
                    ]

        # detector list of images
        detector = [[0, 6000, 50],
                    [0, 6000*2, 50],
                    [-3000, 6000, 50]
                    ]
        # safe_zone list of images
        safe_zone = [[image_finish, 6350, 300]]
                     #[image_win, 100, 2000]

        # loop to add images from the list to group
        for plt in plat:
            plt = Platform(plt[0], plt[1], plt[2], plt[3], plt[4])
            self.platforms_list.add(plt)

        for mtr in meteor:
            mtr = Meteor(mtr[0], mtr[1], mtr[2], mtr[3])
            self.meteor_list.add(mtr)

        for mtr in self.meteor_list:
            mtr.update()

        for coin in coins:
            coin = Coin(coin[0], coin[1])
            self.coin_list.add(coin)

        for detect in detector:
            detect = Detector(detect[0], detect[1], detect[2])
            self.detector_list.add(detect)

        for house in safe_zone:
            house = Safe_house(house[0], house[1], house[2])
            self.safe_house_list.add(house)


# coming soon
#class Level_02(Level):
#    def __init__(self, character):
#        super(Level_02, self).__init__(character)
#        #self.character_start = self.character_start_x, self.character_start_y = 0, 0
