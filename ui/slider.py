import pygame

class Slider:
    def __init__(self, x,y,width,min_val,max_val, step=1, 
                 initial = None, label='',value_to_text=None):
        self.track_rect = pygame.Rect(x,y,width, 6)
        self.handle_radius = 10
        self.min = float(min_val)
        self.max = float(max_val)
        self.step = float(step)
        if initial is not None:
            self.value = float(initial)
        else:
            self.value = float(min_val)
        self.label = label
        self.value_to_text = value_to_text
        self.dragging = False
        self._hit_rect = pygame.Rect(0,0,
                                     self.handle_radius*2+8,
                                     self.handle_radius*2+8)
    def set_in_change(self, cb):
        self.on_change = cb
    def _clamp(self, v:float)->float:
        v = max(self.min, min(self.max, v))
        if self.step>0:
            v = round(v/self.step) * self.step
        return max(self.min, min(self.max, v))
    def _pos_to_val(self, px:int)->float:
        ratio = (px - self.track_rect.left)/self.track_rect.width
        return self._clamp(self.min + ratio*(self.max - self.min))
    def draw(self, screen, font=None):
        pygame.draw.rect(screen, (210,210,210), self.track_rect, border_radius=3)
        pygame.draw.rect(screen, (60,60,60), self.track_rect,1, border_radius=3)
        hx = self._pos_to_val()
        hy = self.track_rect.centery
        pygame.draw.circle(screen, (40,40,40), (hx, hy), self.handle_radius)
        if font and self.label:
            if callable(self.value_to_text):
                vtxt = f'{int(self.value)}'
                text = font.render(f'{self.label}: {vtxt}',1,(0,0,0))
                screen.blit(text, (self.track_rect.left, self.track_rect.top - 28))
                self._hit_rect.center = (hx,hy)