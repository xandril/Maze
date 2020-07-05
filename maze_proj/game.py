import pygame

from System.image_loader import ImageLoader
from System.map import Map
from entity.player import Player

CELL_SIZE = 40
X_OFFSET = 40
Y_OFFSET = 40
X_SCALE = 40
Y_SCALE = 40
MAZE_HEIGHT = 8
MAZE_WIDTH = 8


def _create_player(pos, sprite_list, image):
    player = Player(pos, image)
    sprite_list.add(player)
    return player


class Game:
    def __init__(self, title: str, width: int, height: int):
        self.running = True
        self.width = width
        self.height = height
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.images = []
        # add player_sprite
        self.images.append(
            ImageLoader.load_and_convert_image("sprites/space-ship-png-sprite.png", (int(X_OFFSET * 0.66), int(Y_OFFSET * 0.66)),
                                               -90))
        # add wall_sprite
        self.images.append(ImageLoader.load_and_convert_image("sprites/brick_wall.png", (X_OFFSET, Y_OFFSET), 0))
        self.walls_list = pygame.sprite.Group()
        self.player_list = pygame.sprite.Group()
        self.maze_map = Map("maps/level.txt", MAZE_WIDTH, MAZE_HEIGHT, X_OFFSET, Y_OFFSET, X_SCALE, Y_SCALE)
        self.maze_map.put_objects(self.walls_list, self.images[1])
        self.player = _create_player((30, self.height - 30), self.player_list, self.images[0])

    def _render(self):
        self.screen.fill((255, 255, 255))
        self.player_list.draw(self.screen)
        self.walls_list.draw(self.screen)
        pygame.display.flip()

    def _check_collision(self):
        if pygame.sprite.groupcollide(self.player_list, self.walls_list, True, False, pygame.sprite.collide_circle):
            self.player = _create_player((30, self.height - 30), self.player_list, self.images[0])

    def _update(self):
        self.player.move()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()  # get tuple of 1 and 0; 1- key pressed / 0 - not pressed
        if keys[pygame.K_w]:
            self.player.forward = True
        else:
            self.player.forward = False
        if keys[pygame.K_d]:
            self.player.turn_right = True
        else:
            self.player.turn_right = False

        if keys[pygame.K_a]:
            self.player.turn_left = True
        else:
            self.player.turn_left = False

    def run(self):
        timer = pygame.time.Clock()

        while self.running:
            timer.tick(60)
            self._handle_events()
            self._update()
            self._check_collision()
            self._render()
