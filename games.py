# version 0.1
import pygame as pg                               # import pygame as pg
from setting import *                             # import all variable from setting
from character import Character                   # import class character from character
from classes import Level_01                      # import class level_01 from classses


import menu                                       # import menu
import sys                                        # import sys


def run_game():
    pg.init()                                                   # initialize pygame
    window = screen_width, screen_height                        # variable to set screen width and height
    screen = pg.display.set_mode(window)                        # variable to set the display size
    # background images
    bg = pg.image.load("images/sky_bg.jpg").convert()           # image for background
    bg = pg.transform.scale(bg, (screen_width, screen_height))  # transform the scale of the background image
    # coordinate x for background
    x = 0                                                       # coordinate x for the background

    pg.display.set_caption("Escape from Apocalypse ver.1.0")    # title of the game
    font = pg.font.SysFont("Times New Roman", 30)               # font type and size to write something
    point = 0                                                   # set point to 0

    char = Character(screen)                                    # variable to call class character

    lvl01 = Level_01(char)                                      # variable to call class Level_01

    lvl_list = []                                               # create an empty list
    lvl_list.append(lvl01)                                      # add lvl01 to lvl_list list
    current_lvl_number = 0                                      # set current_lvl_number to 0
    current_lvl = lvl_list[current_lvl_number]                  # variable to get the index in lvl_list
    char.starting_pos(current_lvl)                              # call funtion starting pos in character class to
                                                                # to get the starting position for our character

    clock = pg.time.Clock()                                     # function time clock in pygame
    fps = 60                                                    # set fps to 60

    pg.mixer.music.load("iseng/soundtrack.mp3")                 # load music
    pg.mixer.music.play(-1, 0.0)                                # start the music with playback so it'll become endless

    while True:                                                 # while loop
        bgshift = x % bg.get_rect().width                       # set variable for this calculation

        for event in pg.event.get():
            if event.type == pg.QUIT:                           # if we click on x on the top left corner of the screen
                sys.exit()                                      # it will close the game

        screen.blit(bg, (bgshift - bg.get_rect().width, 0))     # draw the background image on screen
        # moving background
        if bgshift < screen_width:
            screen.blit(bg, (bgshift, 0))

        if char.hspeed > 0:                                     # if char horizontal speed more than 0
            if bgshift < screen_width:                          # if bg shift less then screen's width
                screen.blit(bg, (bgshift, 0))
                x -= 4                                          # scroll the background to the left
        if char.hspeed < 0:                                     # if char horizontal speed less than 0
            if bgshift < screen_width:                          # if bg shift less then screen's width
                screen.blit(bg, (bgshift, 0))
                x += 4                                          # scroll the background to the right

        # when we press key
        keys = pg.key.get_pressed()                             # variable for key pressed
        if keys[pg.K_ESCAPE]:                                   # if you press escape button
            sys.exit()                                          # exit the game

        # collision
        hit = pg.sprite.spritecollide(char, current_lvl.meteor_list, False)
        if hit:
            menu.game_over_meteor(run_game)

        fall = pg.sprite.spritecollide(char, current_lvl.detector_list, False)
        if fall:
            menu.game_over_fall(run_game)

        text = font.render("Coins:{} ".format(point), True, Gray)
        collect = pg.sprite.spritecollide(char, current_lvl.coin_list, True)
        if collect:
            point += 25
        screen.blit(text, (screen_width/2 - 75, 0))

        finish = pg.sprite.spritecollide(char, current_lvl.safe_house_list, False)
        if finish:
            if point >= 600:
                menu.win(run_game)
            elif point < 600:
                menu.not_enough_coin(run_game)

        char.update(current_lvl.platforms_list, event)
        event = None

        current_lvl.update()

        current_lvl.blitme(screen)

        current_lvl.point_of_view()

        clock.tick(fps)

        # character's direction
        if char.hspeed < 0:
            char.left_blitme()
        if char.hspeed > 0:
            char.right_blitme()
        if char.hspeed == 0:
            char.right_blitme()

        pg.display.update()


menu.menu_screen(run_game)