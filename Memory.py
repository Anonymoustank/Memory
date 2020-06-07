import pygame as pg
from random import choice
GREEN = (20, 255, 140)
GREY = (210, 210, 210)
GRAY = GREY
YELLOW = (255, 200, 0)
BROWN = (100, 40, 0)
WHITE = (255, 255, 255)
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
list = [BLACK, BLACK, ORANGE, ORANGE, WHITE, WHITE, GREEN, GREEN, YELLOW, YELLOW, BROWN, BROWN, RED, RED, PURPLE, PURPLE]
card_list = []
matching_images = pg.sprite.Group()
for i in range(1, 17):
    exec("card%s = Block(BLACK, 50, 30)" % i)
    exec("card%s.rect.x = x_value" % i)
    exec("card%s.rect.y = y_value" % i)
    exec("card.add(card%s)" % i)
    color = choice(list)
    list.remove(color)
    exec("sprite_%s = Block(color, 20, 20)" % i)
    exec("sprite_%s.rect.x = x_value" % i)
    exec("sprite_%s.rect.y = y_value" % i)
    exec("matching_images.add(sprite_%s)" % i)
    exec("card_list.append(card%s)" % i)
    x_value += 100
    if i % 4 == 0:
        x_value = 75
        y_value += 100

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            pos = pg.mouse.get_pos()
            x, y = pos
            for i in card_list:
                if abs(i.rect.x - x) <= 35 and abs(i.rect.y - y) <= 35:
                    i.rect.x = -100
    screen.fill(GRAY)
    matching_images.draw(screen)
    card.draw(screen)
    pg.display.update()
    
    



pg.quit()