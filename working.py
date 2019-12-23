import time
import pygame as pg

pg.init()

game_display = pg.display.set_mode((450, 130))
pg.display.set_caption("CLOCK")
now = time.localtime()
print(time.localtime())
hours = now[3]
minutes = now[4]
seconds = now[5]
print(str(hours) + ":"  + str(minutes) + ":" + str(seconds))
dot = ":"
clock_tick = pg.time.Clock()
# Colors
white = (255, 255, 255)
black = (0, 0, 0)


def clock():
    global seconds
    global hours
    global minutes
    timi = str(hours).zfill(2) + dot + str(minutes).zfill(2) + dot + str(seconds).zfill(2)
    seconds += 1
    time.sleep(1)
    if seconds == 60:
        seconds = 00
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1
    if hours == 24:
        hours = 00
    font = pg.font.Font(None, 150)
    timi_render = font.render(timi, 1, white)
    game_display.fill(black)
    game_display.blit(timi_render, (10, 10))


a = 1
while a == 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            a = 2
    clock()
    pg.display.flip()
    clock_tick.tick(60)

pg.quit()
quit()
