import pygame
from pygame.sprite import Sprite

from System.UI.UI_elements.Text import Text


class Button(Sprite):
    def __init__(self, color, size, btn_label="dafaq"):
        super(Button, self).__init__()
        self.btn_label = btn_label
        self.labelObj = Text(btn_label, 14, (0, 0, 0))
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.image.blit(self.labelObj.textSurf, (self.image.get_width() // 2 - 20, 2))

    def set_pos(self, pos):
        self.rect.center = pos

    def get_rect(self):
        return self.rect

    def get_label(self):
        return self.btn_label
