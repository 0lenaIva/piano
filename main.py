from pygame import*
from settings import WINDOW_WIDTH, WINDOW_HEIGHT,WHITE,KEYS
from keys import create_key_rects, draw_keys
from sounds import load_sounds
init()

screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption("Piano Game")

sounds = load_sounds(KEYS)
pressed_keys = set()
key_rects = create_key_rects(7)
keys_list = list(KEYS.keys())

running = True

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        #клавіатура
        if e.type == KEYDOWN:
            pass
        #миша
        if e.type == MOUSEBUTTONDOWN:
            pos = e.pos
            for i, rect in enumerate(key_rects):
                if rect.collidepoint(pos):
                    sounds[keys_list[i]].play()
                    pressed_keys.add(i)
        if e.type == MOUSEBUTTONUP:
            pos = e.pos
            for i, rect in enumerate(key_rects):
                if i in pressed_keys and rect.collidepoint(pos):
                    pressed_keys.remove(i)

    screen.fill(WHITE)
    draw_keys(screen, key_rects, pressed_keys)
    display.update()

quit()