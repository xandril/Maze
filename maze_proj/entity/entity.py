import pygame as pg


class Entity(pg.sprite.Sprite):
    def __init__(self, image, pos):
        super(Entity, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.x_motion = 0
        self.y_motion = 0

    def rotate_sprite(self, image, angle):
        old_rect_center = self.rect.center
        self.image = pg.transform.rotate(image, angle)
        self.rect = self.image.get_rect()
        self.rect.center = old_rect_center

    def update(self):
        x = (self.rect.centerx + self.x_motion) % 600
        y = (self.rect.centery + self.y_motion) % 600
        self.rect.center = (x, y)
