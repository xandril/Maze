import pygame


class Text(pygame.sprite.Sprite):
    def __init__(self, text, text_size, color):
        # Call the parent class (Sprite) constructor
        self.text = text
        super(Text, self).__init__()
        self.font = pygame.font.SysFont("Arial", text_size)
        self.textSurf = self.font.render(text, 1, color)

    def get_str(self):
        return self.text
