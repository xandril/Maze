from application.entity.entity import Entity


class Finish(Entity):
    def __init__(self, pos, image):
        self.orig_image = image
        super(Finish, self).__init__(self.orig_image, pos)
