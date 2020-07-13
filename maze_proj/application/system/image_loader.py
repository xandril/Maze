import pygame


class ImageLoader:
    @staticmethod
    def load_and_convert_image(fname, scale, angle):
        image = pygame.image.load(fname)
        image = pygame.transform.scale(image, scale)
        image = pygame.transform.rotate(image, angle)
        return image

    @staticmethod
    def draw_and_convert_image(color, scale, angle):
        image = pygame.Surface(scale)
        image = pygame.transform.rotate(image, angle)
        image.fill(color)
        image.set_colorkey(color)
        return image
