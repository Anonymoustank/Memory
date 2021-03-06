import pygame as pg
from random import choice
GREEN = (20, 255, 140)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)
GRAY = GREY
YELLOW = (255, 200, 0)
BROWN = (100, 40, 0)
BLUE = (0, 0, 100)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 100, 10)

pg.init()
WIDTH = 500
HEIGHT = 500
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(GREEN)
pg.display.set_caption("Memory")

running = True
cards_uncovered = 0
end_screen = True

class Block(pg.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pg.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.color = color
        pg.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.rect.center = (int(width/2), int(height/2))
card = pg.sprite.Group()
y_value = 75
x_value = 75
list = [BLACK, BLACK, ORANGE, ORANGE, BLUE, BLUE, GREEN, GREEN, YELLOW, YELLOW, BROWN, BROWN, RED, RED, PURPLE, PURPLE]
card_list = []
sprite_list = []
matching_images = pg.sprite.Group()
for i in range(1, 17):
    exec("card%s = Block(BLACK, 50, 30)" % i)
    exec("card%s.rect.x = x_value" % i)
    exec("card%s.rect.y = y_value" % i)
    exec("card.add(card%s)" % i)
    exec("card_list.append(card%s)" % i)
    color = choice(list)
    list.remove(color)
    exec("sprite_%s = Block(color, 20, 20)" % i)
    exec("sprite_%s.rect.x = x_value" % i)
    exec("sprite_%s.rect.y = y_value" % i)
    exec("matching_images.add(sprite_%s)" % i)
    exec("sprite_list.append(sprite_%s)" % i)
    x_value += 100
    if i % 4 == 0:
        x_value = 75
        y_value += 100
not_hidden = []
attempts = 0
myfont = pg.font.SysFont('verdana', 25)
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            end_screen = False
        if event.type == pg.MOUSEBUTTONUP:
            if cards_uncovered == 2:
                cards_uncovered = 0
                attempts += 1
                for a in not_hidden:
                    a.rect.x += 600
                not_hidden = []
            pos = pg.mouse.get_pos()
            x, y = pos
            for i in card_list:
                if i.rect.collidepoint(pos):
                    cards_uncovered += 1
                    i.rect.x -= 600
                    not_hidden.append(i)
                    if cards_uncovered == 1:
                        check_sprite_one = card_list.index(i)
                        check_card_one = i
                        check_sprite_one = sprite_list[check_sprite_one]
                    elif cards_uncovered == 2:
                        check_sprite_two = card_list.index(i)
                        check_card_two = i
                        check_sprite_two = sprite_list[check_sprite_two]
                        if check_sprite_one.color == check_sprite_two.color:
                            sprite_list.remove(check_sprite_one)
                            sprite_list.remove(check_sprite_two)
                            card_list.remove(check_card_one)
                            card_list.remove(check_card_two)
                            check_sprite_one.kill()
                            check_card_one.kill()
                            check_sprite_two.kill()
                            check_card_two.kill()
                            not_hidden = []
    screen.fill(GRAY)
    matching_images.draw(screen)
    card.draw(screen)
    attempts_made = myfont.render("Attempts: " + str(attempts), True, (BLACK))
    screen.blit(attempts_made, (0, 0))
    pg.display.update()
    if len(sprite_list) == 0:
        running = False

while end_screen:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            end_screen = False
    screen.fill(GRAY)
    textsurface = myfont.render("You Win!", True, (BLACK))
    screen.blit(textsurface, (screen.get_width() // 3 + 30, 225))
    attempts_made = myfont.render("Attempts: " + str(attempts), True, (BLACK))
    screen.blit(attempts_made, (0, 0))
    pg.display.update()
    
pg.quit()