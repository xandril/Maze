import pygame

from System.scenes.main_menu import MainMenu


class App:
    def __init__(self, width, height, title):
        pygame.init()

        self.screen = pygame.display.set_mode((width, height))
        self.width = width
        self.height = height
        pygame.display.set_caption(title)

    def start(self):
        MainMenu(self.screen, self.width, self.height).run()


