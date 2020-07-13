import math
from application.entity.entity import Entity


class Player(Entity):
    def __init__(self, pos, image):
        self.orig_image = image
        super(Player, self).__init__(self.orig_image, pos)
        self.forward = False
        self.turn_left = False
        self.turn_right = False
        self.angle = 0
        self.acceleration = 2

    def move(self, width, height):
        if self.forward:
            self.x_motion = self.acceleration * math.cos(math.radians(self.angle)) #### x right ( pygame coords of the screen)
            self.y_motion = - self.acceleration * math.sin(math.radians(self.angle)) ####  y - down
            Entity.update(self, width, height)
        if self.turn_left:
            self.angle = (self.angle + 10) % 360
        if self.turn_right:
            self.angle = (self.angle - 10) % 360
        Entity.rotate_sprite(self, self.orig_image, self.angle)
