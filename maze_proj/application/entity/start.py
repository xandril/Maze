from application.entity.entity import Entity


class Start(Entity):
    def __init__(self, pos, image):
        self.orig_image = image
        super(Start, self).__init__(self.orig_image, pos)
