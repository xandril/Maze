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


class Game:
    def __init__(self, title: str, width: int, height: int):
        self.running = True
        self.width = width
        self.height = height
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        wall_image = ImageLoader.load_and_convert_image("sprites/brick_wall.png", (40, 40), 0)
        player_image = ImageLoader.load_and_convert_image("sprites/space-ship-png-sprite.png", (20, 20), -90)
        self.walls_list = pygame.sprite.Group()
        self.maze_map = Map("maps/level.txt", MAZE_WIDTH, MAZE_HEIGHT, X_OFFSET, Y_OFFSET, X_SCALE, Y_SCALE)
        self.maze_map.put_objects( self.walls_list, wall_image)
        self.player = Player((width // 2, height // 2), player_image)

        self.player_list = pygame.sprite.Group()
        self.player_list.add(self.player)

    def _render(self):
        self.screen.fill((255, 255, 255))
        self.player_list.draw(self.screen)
        self.walls_list.draw(self.screen)
        pygame.display.flip()

    def _check_collision(self):
        if pygame.sprite.groupcollide(self.player_list, self.walls_list, False, False):
            print("collide")



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
