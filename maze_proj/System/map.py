from entity.wall import Wall


class Map:
    def __init__(self, fname: str, map_width: int, map_height: int, offset_x: int, offset_y: int, scale_x: int,
                 scale_y: int):
        self.level_map = []
        self.map_width = map_width
        self.map_height = map_height
        self.x_offset = offset_x
        self.y_offset = offset_y
        self.scale_x = scale_x
        self.scale_y = scale_y
        with open(fname, 'r') as file:
            for line in file.readlines():
                self.level_map.append(line.strip('\n').split())

    def put_objects(self, sprite_list, image):
        y: int = 0
        for line in self.level_map:
            x: int = 0
            for char in line:
                if char == '1':
                    wall_x = x * self.scale_x + self.x_offset
                    wall_y = y * self.scale_y + self.y_offset
                    wall_rect_center = (wall_x, wall_y)
                    sprite_list.add(Wall(wall_rect_center, image))
                    print("create shit on pos ", x, y)
                x += 1
            y += 1
