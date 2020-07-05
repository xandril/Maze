from entity.entity import Entity


class Wall(Entity):
    def __init__(self, pos, image):
        self.orig_image = image
        super(Wall, self).__init__(self.orig_image, pos)



