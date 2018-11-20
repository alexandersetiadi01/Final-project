import pygame as pg
from setting import *


class Character(pg.sprite.Sprite):                                  # inherit sprite
    def __init__(self, screen):
        super(Character, self).__init__()                           # super class
        self.screen = screen

        # character's image
        self.image = pg.image.load("images/ninja.png")
        self.image = pg.transform.scale(self.image, (100, 100))
        self.image1 = pg.image.load("images/ninja1.png")
        self.image1 = pg.transform.scale(self.image1, (100, 100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # coordinate for character
        self.rect.x = 60
        self.rect.y = 300

        # for movement
        self.hspeed = 0
        self.vspeed = 0

    # character's starting position when the game starts
    def starting_pos(self, level):
        self.level = level
        self.set_position = (self.rect.x, self.rect.y)

    def update(self, collide, event=None):
        self.gravity()  # call gravity function

        # collision with platform
        self.rect.x += self.hspeed
        collision_list = pg.sprite.spritecollide(self, collide, False)
        for collided_object in collision_list:
            if self.hspeed > 0:
                self.rect.right = collided_object.rect.left
            elif self.hspeed < 0:
                self.rect.left = collided_object.rect.right

        self.rect.y += self.vspeed
        collision_list = pg.sprite.spritecollide(self, collide, False)
        for collided_object in collision_list:
            if self.vspeed > 0:
                self.rect.bottom = collided_object.rect.top
                self.vspeed = 0
            elif self.vspeed < 0:
                self.rect.top = collided_object.rect.bottom
                self.vspeed = 0

        # button event
        if not event == None:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    self.hspeed += speed

                if event.key == pg.K_LEFT:
                    self.hspeed -= speed

                if event.key == pg.K_UP:
                    if self.vspeed == 0:
                    #if len(collision_list)>= 1:
                        self.vspeed -= speed*2

            if event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT:
                    if self.hspeed > 0:
                        self.hspeed = 0

                if event.key == pg.K_LEFT:
                    if self.hspeed < 0:
                        self.hspeed = 0

    # function for gravitation
    def gravity(self, gravity=.35):
        if self.vspeed == 0:
            self.vspeed = 1
        else:
            self.vspeed += gravity

    # image for character to face right direction
    def right_blitme(self):
        self.screen.blit(self.image, self.rect)

    # image for character to face left direction
    def left_blitme(self):
        self.screen.blit(self.image1, self.rect)


