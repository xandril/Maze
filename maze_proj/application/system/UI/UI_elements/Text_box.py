import pygame

from application.system.UI.UI_elements.text_input import TextInput
from application.system.colors import Colors


class TextBox(pygame.sprite.Sprite):
    def __init__(self, color, size, font_size=16):
        super(TextBox, self).__init__()
        self.text_input = TextInput("", "", font_size, True, Colors.BLACK, Colors.RED, 400, 35, -1)
        self.color = color
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()

    def set_pos(self, pos):
        self.rect.center = pos

    def set_color(self, color):
        pass

    def get_rect(self):
        return self.rect

    def draw(self, screen):
        field = pygame.Surface((100, 20))
        field.fill(self.color)

        field.blit(self.text_input.get_surface(),
                   (field.get_width() // 2 - self.text_input.get_surface().get_width() // 2,
                    5))
        screen.blit(field, self.rect.center)

    def handle_text(self, events):
        self.text_input.handle_text(events)

    def get_text(self):
        return self.text_input.get_text()
