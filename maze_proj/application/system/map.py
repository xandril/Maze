from application.entity.finish import Finish
from application.entity.player import Player
from application.entity.start import Start
from application.entity.wall import Wall


class Map:
    def __init__(self, difficult: str, offset_x: int, offset_y: int, scale_x: int,
                 scale_y: int):
        self.level_map = []

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

    def put_objects(self, players_list, objects_list, images):
        y: int = 0
        for line in self.level_map:
            x: int = 0
            for char in line:
                pos_x = x * self.scale_x + self.x_offset + 20
                pos_y = y * self.scale_y + self.y_offset + 20
                pos_center = (pos_x, pos_y)
                if char == '1':
                    objects_list.add(Wall(pos_center, images[1]))
                elif char == 'p':
                    players_list.add(Player(pos_center, images[0]))
                elif char == 's':
                    objects_list.add(Start(pos_center, images[2]))
                elif char == 'f':
                    objects_list.add(Finish(pos_center, images[2]))

                x += 1
            y += 1
