import pygame

from System.UI.UI_elements.Text import Text
from System.map import Map
from System.scenes import main_menu
from entity.player import Player

X_OFFSET = 40
Y_OFFSET = 40
X_SCALE = 40
Y_SCALE = 40


def _create_player(pos, sprite_list, image):
    player = Player(pos, image)
    sprite_list.add(player)
    return player


def timer_caster(time):
    m = round((time // 60) % 60)
    s = (time % 60)
    ms = str((round((s - int(s)) * 1000)))
    s = round(s)
    if m < 10:
        m = str('0' + str(m))
    else:
        m = str(m)
    if s < 10:
        s = str('0' + str(s))
    else:
        s = str(s)
    return m + ":" + s + ":" + ms


class Game:
    def __init__(self, screen, difficult: str, images, is_fullscreen, scale):
        self.is_fullscreen = is_fullscreen
        self.scale = scale
        self.start_time = pygame.time.get_ticks()
        self.running = True
        self.screen = screen

        self.images = images
        self.walls_list = pygame.sprite.Group()
        self.player_list = pygame.sprite.Group()
        x_offset = int(X_OFFSET * scale[0])
        y_offset = int(Y_OFFSET * scale[1])
        x_scale = int(X_SCALE * scale[0])
        y_scale = int(Y_SCALE * scale[1])
        self.size_font = int(16 * scale[1])
        self.maze_map = Map(difficult, x_offset, y_offset, x_scale, y_scale).put_objects(self.walls_list,
                                                                                         self.images[1])
        self.player = _create_player((self.screen.get_width() // 2, 10), self.player_list, self.images[0])
        self.text_timer = Text("00:00:000", self.size_font, (0, 0, 0))

    def _render(self):
        self.screen.fill((255, 255, 255))
        self.player_list.draw(self.screen)
        self.walls_list.draw(self.screen)
        self.screen.blit(self.text_timer.textSurf, (self.screen.get_width() // 2, int(self.scale[1] * 10)))
        pygame.display.flip()

    def _check_collision(self):
        if pygame.sprite.groupcollide(self.player_list, self.walls_list, True, False, pygame.sprite.collide_circle):
            self.player = _create_player((30, self.screen.get_height() - 30), self.player_list, self.images[0])

    def _update(self):
        self.player.move(self.screen.get_width(), self.screen.get_height())
        time = (pygame.time.get_ticks() - self.start_time) / 1000
        self.text_timer = Text(timer_caster(time), self.size_font, (0, 0, 0))

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()  # get tuple of 1 and 0; 1- key pressed / 0 - not pressed
        if keys[pygame.K_ESCAPE]:
            self.running = False
            main_menu.MainMenu(self.screen, self.images, self.is_fullscreen, self.scale).run()

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
