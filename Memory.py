import pygame as pg
import time
GREEN = (20, 255, 140)
GREY = (210, 210, 210)
GRAY = GREY
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
BLACK = (0, 0, 0)

pg.init()
WIDTH = 500
HEIGHT = 500
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(GREEN)
pg.display.set_caption("Memory")

running = True

class Block(pg.sprite.Sprite):
    def __init__(self, shape, color, width, height):
        super().__init__()
        self.image = pg.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        if shape == "rectangle":
            pg.draw.rect(self.image, color, [0, 0, width, height])
            self.rect = self.image.get_rect()
            self.rect.center = (int(width/2), int(height/2))
        elif shape == "circle":
            pg.draw.circle(self.image, color, (width // 2, height // 2), width // 2)
            self.rect = self.image.get_rect()
            self.rect.center = (int(width/2), int(height/2))

matching_images = pg.sprite.Group()

red_square = Block("rectangle", RED, 20, 20)
black_circle = Block("circle", BLACK, 20, 20)
black_circle.rect.x = 100
black_circle.rect.y = 150
matching_images.add(black_circle)
matching_images.add(red_square)
matching_images.draw(screen)
pg.display.update()
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill(GRAY)
    matching_images.draw(screen)
    pg.display.update()
    
    



pg.quit()