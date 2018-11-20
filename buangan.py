# movement ver.1
'''        if keys[pg.K_RIGHT]:
            if char.rect.right >= setting.screen_width/2:
                if bgshift < setting.screen_width:
                    screen.blit(bg, (bgshift, 0))
                    x -= 4
            else:
                char.change_speed(5, 0)
                #char.move_right()
        if keys[pg.K_LEFT]:
            if char.rect.left <= setting.screen_width/4:
                if bgshift < setting.screen_width:
                    screen.blit(bg, (bgshift, 0))
                    x += 4
            else:
                char.change_speed(-5, 0)
                #char.move_left()
        if keys[pg.K_ESCAPE]:
            sys.exit()

        if keys[pg.K_UP]:
            char.move_up()
        if keys[pg.K_DOWN]:
            char.move_down()
        # jump
        if not char.jump:
            if keys[pg.K_SPACE]:
                char.jump = True
        else:
            if char.jump_count >= -7:
                neg = 2
                if char.jump_count < 0:
                    neg = -2
                char.rect.y -= (char.jump_count ** 2) * 0.5 * neg
                char.jump_count -= 1
            else:
                char.jump = False
                char.jump_count = 7
'''
# movement ver.2
'''# button event
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    sys.exit()
                if event.key == pg.K_RIGHT:
                    char.change_speed(5, 0)
                if event.key == pg.K_LEFT:
                    char.change_speed(-5, 0)
                if event.key == pg.K_UP:
                    char.change_speed(0, -5)
                if event.key == pg.K_DOWN:
                    char.change_speed(0, 5)
            if event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT:
                    char.change_speed(-5, 0)
                if event.key == pg.K_LEFT:
                    char.change_speed(5, 0)
                if event.key == pg.K_UP:
                    char.change_speed(0, 5)
                if event.key == pg.K_DOWN:
                    char.change_speed(0, -5)
            '''



'''
class Road(pg.sprite.Sprite):
    def __init__(self, setting, screen):
        super(Road, self).__init__()
        self.screen = screen
        self.setting = setting

        self.image = pg.image.load("images/road.png")
        self.image = pg.transform.scale(self.image, (150, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 450

        self.image2 = pg.image.load("images/road.png")
        self.image2 = pg.transform.scale(self.image2, (100, 50))
        self.rect2 = self.image2.get_rect()
        self.rect2.x = 150
        self.rect2.y = 300

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image2, self.rect2)
'''

'''
# character movement
    def change_speed(self, hspeed, vspeed):
        self.hspeed += hspeed
        self.vspeed += vspeed
'''



'''
    def move_right(self):
        self.rect.x += self.move_speed

    def move_left(self):
        self.rect.x -= self.move_speed

    def move_up(self):
        self.rect.y -= self.move_speed

    def move_down(self):
        self.rect.y += self.move_speed

    # make the character appear in screen
'''


## platform
    #p1 = Platform("images/road.png", 450, 450, 150, 50)
    #p2 = Platform("images/road.png", 550, 300, 150, 50)
    #p3 = Platform("images/road.png", 650, 350, 150, 50)
    #p4 = Platform("images/road.png", 750, 500, 150, 50)
    #
    ## collision group
    #collide_group = pg.sprite.Group()
    #collide_group.add(p1)
    #collide_group.add(p2)
    #collide_group.add(p3)
    #collide_group.add(p4)
    #collide_group.draw(screen)

#screen.blit(bg, (bgshift - bg.get_rect().width, 0))



