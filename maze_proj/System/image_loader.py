import pygame


class ImageLoader:
    @staticmethod
    def load_and_convert_image(fname, scale, angle):
        image = pygame.image.load(fname)
        image = pygame.transform.scale(image, scale)
        image = pygame.transform.rotate(image, angle)
        return image
