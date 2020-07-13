import pygame as pg


class Entity(pg.sprite.Sprite):
    def __init__(self, image, pos):
        super(Entity, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.x_motion = 0
        self.y_motion = 0
        self.radius = int(self.rect.width * .9 / 2)
        self.old_pos = (0, 0)  # for collide

    def rotate_sprite(self, image, angle):
        old_rect_center = self.rect.center
        self.image = pg.transform.rotate(image, angle)
        self.rect = self.image.get_rect()
        self.rect.center = old_rect_center

    def update(self, width, height):
        x = (self.rect.centerx + self.x_motion) % width
        y = (self.rect.centery + self.y_motion) % height
        self.old_pos = self.rect.center  # save old_pos for check_collide
        self.rect.center = (x, y)

    def back_after_collide(self):
        self.rect.center = self.old_pos
