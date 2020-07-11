import pygame

from System.image_loader import ImageLoader
from System.scenes.main_menu import MainMenu

base_x = 40
base_y = 40
base_width = 800
base_height = 600


class App:
    def __init__(self, width, height, title, is_fullscreen):
        pygame.init()
        self.is_fullscreen = is_fullscreen
        self.sprite_list = []
        # add player_sprite
        self.x_scale = width / base_width
        self.y_scale = height / base_height
        self.sprite_list.append(
            ImageLoader.load_and_convert_image("sprites/space-ship-png-sprite.png",
                                               (int(base_x * 0.66 * self.x_scale), int(base_y * 0.66 * self.y_scale)),
                                               -90))
        # add wall_sprite
        self.sprite_list.append(
            ImageLoader.load_and_convert_image("sprites/brick_wall.png", (int(base_x * self.x_scale), int(base_y * self.y_scale)), 0))
        if not is_fullscreen:
            self.screen = pygame.display.set_mode((width, height))
        else:
            self.screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

        self.width = width
        self.height = height

        pygame.display.set_caption(title)

    def start(self):
        MainMenu(self.screen, self.sprite_list, self.is_fullscreen, (self.x_scale, self.y_scale)).run()
