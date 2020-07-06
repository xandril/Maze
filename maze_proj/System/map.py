from entity.wall import Wall


class Map:
    def __init__(self, difficult: str, map_width: int, map_height: int, offset_x: int, offset_y: int, scale_x: int,
                 scale_y: int):
        self.level_map = []
        self.map_width = map_width
        self.map_height = map_height
        self.x_offset = offset_x
        self.y_offset = offset_y
        self.scale_x = scale_x
        self.scale_y = scale_y
        file_path = None
        if difficult == "easy":
            file_path = "maps/easy.txt"
        elif difficult == "normal":
            file_path = "maps/normal.txt"
        elif difficult == "hard":
            file_path = "maps/hard.txt"

        with open(file_path, 'r') as file_path:
            for line in file_path.readlines():
                self.level_map.append(line.strip('\n').split())

    def put_objects(self, sprite_list, image):
        y: int = 0
        for line in self.level_map:
            x: int = 0
            for char in line:
                if char == '1':
                    wall_x = x * self.scale_x + self.x_offset + 20
                    wall_y = y * self.scale_y + self.y_offset + 20
                    wall_rect_center = (wall_x, wall_y)
                    sprite_list.add(Wall(wall_rect_center, image))
                x += 1
            y += 1
