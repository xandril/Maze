import pygame
from pygame.sprite import Sprite

from application.system.UI.UI_elements.Text import Text


class Button(Sprite):
    def __init__(self, color, size, btn_label, font_size=16):
        super(Button, self).__init__()
        self.btn_label = btn_label
        self.labelObj = Text(btn_label, font_size, (0, 0, 0))
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.image.blit(self.labelObj.textSurf, (self.image.get_width() // 2 - self.labelObj.textSurf.get_width() // 2,
                                                 0))  # yeah boi, text get pos on the center of the f'cking button

    def set_pos(self, pos):
        self.rect.center = pos

    def set_color(self, color):
        self.image.fill(color)
        self.image.blit(self.labelObj.textSurf, (self.image.get_width() // 2 - self.labelObj.textSurf.get_width() // 2,
                                                 0))  # yeah boi, text get pos on the center of the f'cking button

    def get_rect(self):
        return self.rect

    def get_label(self):
        return self.btn_label
