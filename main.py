import pygame as pg
import sys
from  pygame.locals import *

pg.init()
display_surf = pg.display.set_mode((800,600))
fps = pg.time.Clock()
fps.tick(60)
color1 = (0,0,0)    #Black
color2 = (255,255,255)  #white
stick1 = pg.Rect((20,300), (10,45))
stick2 = pg.Rect((780,300), (10,45))
while True:
    # pg.draw.rect(display_surf, color2, pg.Rect(20,300,10,45))
    # pg.draw.rect(display_surf, color2, pg.Rect(770,300,10,45))
    for event in pg.event.get():
        if event== QUIT:
            pg.quit()
            sys.exit()
    
    pg.display.update()
