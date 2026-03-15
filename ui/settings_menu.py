import pygame
from buttons import Button
from ui.slider import Slider

class SettjngsMenu:
    def __init__(self, screen_rect, initial_volume, initial_keys,
                 min_keys, max_keys, on_change, on_back):
        self.screen_rect = screen_rect
        self.on_change = on_change
        self.on_back = on_back
        cx = screen_rect.centerx
        top = 140

        back_idle = pygame.transform.scale(
            pygame.image.load('/assets/images/buttons/exit_unhover.png'),
            (48,48)
        )
        back_hover = pygame.transform.scale(
            pygame.image.load('/assets/images/buttons/exit_hover.png'),
            (48,48)
        )

        self.back_btn = Button(
            40,30,48,48,
            '',
            self._back,
            img_idle=back_idle,
            img_hover=back_hover
        )