from pygame import *
import sys
import pygame as pg
from setting import *


def menu_screen(run_game):
    # initialize pygame
    pg.init()
    # game title
    pg.display.set_caption("escape from apocalypse 1.1")
    # set screen width and height
    screen = pg.display.set_mode((screen_width, screen_height))

    # button image
    play = pg.image.load("images/playButton.png").convert()

    # background image
    bg_menu = pg.image.load("images/menu bg2.jpg").convert()
    bg_menu = pg.transform.scale(bg_menu, (screen_width, screen_height))

    # font type and size and all the text
    font = pg.font.SysFont("Arial", 20)
    font1 = pg.font.SysFont("Times New Roman", 30)
    text = font.render("what you need to know before playing this game", True, White)
    text1 = font.render("1. use arrow key to move", True, White)
    text2 = font.render("2. try not to get hit by the meteor", True, White)
    text3 = font.render("3. try not to fall", True, White)
    text4 = font.render("4. follow the coins and collect them all to win the game", True, White)
    text5 = font.render("5. good luck have fun", True, White)
    text6 = font1.render("Escape from Apocalypse", True, Yellow)

    while True:
        # draw the play button image
        rect_play = draw.rect(screen, (White), (230, 230, 300, 130))

        # draw background image and text
        screen.blit(bg_menu, (0, 0))
        screen.blit(play, (200, 200))
        screen.blit(text, (200, 450))
        screen.blit(text1, (200, 470))
        screen.blit(text2, (200, 490))
        screen.blit(text3, (200, 510))
        screen.blit(text4, (200, 530))
        screen.blit(text5, (200, 550))
        screen.blit(text6, (200, 50))

        Event = event.wait()

        # reaction to mouse click
        if Event.type == MOUSEBUTTONDOWN:
            if rect_play.collidepoint(mouse.get_pos()):
                run_game()
        if Event.type == QUIT:
            sys.exit()

        pg.display.update()


def game_over_meteor(run_game):
    # initialize pygame
    pg.init()
    # game title
    pg.display.set_caption("escape from apocalypse 1.1")
    # set screen width and height
    screen = pg.display.set_mode((screen_width, screen_height))

    # button image
    play = pg.image.load("images/playButton.png").convert()

    # background image
    bg_menu = pg.image.load("images/menu bg2.jpg").convert()
    bg_menu = pg.transform.scale(bg_menu, (screen_width, screen_height))

    # font type and size and the text
    font = pg.font.SysFont("Arial", 35)
    text = font.render("getting hit by meteor surely will kill you", False, Red)

    while True:
        # draw the play button image
        rect_play = draw.rect(screen, (White), (230, 230, 300, 130))

        # draw background image and text
        screen.blit(bg_menu, (0, 0))
        screen.blit(play, (200, 200))
        screen.blit(text, (200, 110))

        Event = event.wait()

        # reaction to mouse click
        if Event.type == MOUSEBUTTONDOWN:
            if rect_play.collidepoint(mouse.get_pos()):
                run_game()
        if Event.type == QUIT:
            sys.exit()

        display.update()


def game_over_fall(run_game):
    # initialize pygame
    pg.init()
    # game title
    pg.display.set_caption("escape from apocalypse 1.1")
    # set screen width and height
    screen = pg.display.set_mode((screen_width, screen_height))

    # button image
    play = pg.image.load("images/playButton.png").convert()

    # background image
    bg_menu = pg.image.load("images/menu bg2.jpg").convert()
    bg_menu = pg.transform.scale(bg_menu, (screen_width, screen_height))

    # font type and size and the text
    font = pg.font.SysFont("Arial", 35)
    text = font.render("no one will survive from that height", False, Red)

    while True:
        # draw the play button image
        rect_play = draw.rect(screen, (White), (230, 230, 300, 130))

        # draw background image and text
        screen.blit(bg_menu, (0, 0))
        screen.blit(play, (200, 200))
        screen.blit(text, (200, 110))
        Event = event.wait()

        # reaction to mouse click
        if Event.type == MOUSEBUTTONDOWN:
            if rect_play.collidepoint(mouse.get_pos()):
                run_game()
        if Event.type == QUIT:
            sys.exit()

        display.update()


def win(run_game):
    # initialize pygame
    pg.init()
    # game title
    pg.display.set_caption("escape from apocalypse 1.1")
    # set screen width and height
    screen = pg.display.set_mode((screen_width, screen_height))

    # button image
    play = pg.image.load("images/playButton.png").convert()

    # background image
    bg_menu = pg.image.load("images/menu bg2.jpg").convert()
    bg_menu = pg.transform.scale(bg_menu, (screen_width, screen_height))

    # font type and size and the text
    font = pg.font.SysFont("Arial", 35)
    font1 = pg.font.SysFont("Times New Roman", 20)
    text = font.render("well done, you have reached safe house", False, Green)
    text1 = font1.render(" thanks for the help of this 4 people: ", True, White)
    text2 = font1.render(" Muhammad Erizky Suryaputra", True, White)
    text3 = font1.render(" Jotika Adhisthana", True, White)
    text4 = font1.render(" youtuber called John Hammond", True, White)
    text5 = font1.render(" this game is now playable XD ", True, White)
    text6 = font1.render(" coming soon level 02 ", True, White)

    while True:
        # draw the play button image
        rect_play = draw.rect(screen, (White), (230, 230, 300, 130))

        # draw background image and text
        screen.blit(bg_menu, (0, 0))
        screen.blit(play, (200, 200))
        screen.blit(text, (200, 110))
        screen.blit(text1, (200, 430))
        screen.blit(text2, (200, 450))
        screen.blit(text3, (200, 470))
        screen.blit(text4, (200, 490))
        screen.blit(text5, (200, 510))
        screen.blit(text6, (200, 530))
        Event = event.wait()

        # reaction to mouse click
        if Event.type == MOUSEBUTTONDOWN:
            if rect_play.collidepoint(mouse.get_pos()):
                run_game()
        if Event.type == QUIT:
            sys.exit()

        display.update()


def not_enough_coin(run_game):
    # initialize pygame
    pg.init()
    # game title
    pg.display.set_caption("escape from apocalypse 1.1")
    # set screen width and height
    screen = pg.display.set_mode((screen_width, screen_height))

    # button image
    play = pg.image.load("images/playButton.png").convert()

    # background image
    bg_menu = pg.image.load("images/menu bg2.jpg").convert()
    bg_menu = pg.transform.scale(bg_menu, (screen_width, screen_height))

    # font type and size and the text
    font = pg.font.SysFont("Arial", 35)
    text = font.render("you don't have enough money to enter the safe house", False, Red)

    while True:
        # draw the play button image
        rect_play = draw.rect(screen, (White), (230, 230, 300, 130))

        # draw background image and text
        screen.blit(bg_menu, (0, 0))
        screen.blit(play, (200, 200))
        screen.blit(text, (200, 110))
        Event = event.wait()

        # reaction to mouse click
        if Event.type == MOUSEBUTTONDOWN:
            if rect_play.collidepoint(mouse.get_pos()):
                run_game()
        if Event.type == QUIT:
            sys.exit()

        display.update()

# tired of life? die is not the answer