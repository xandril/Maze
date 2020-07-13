import pygame

from application.entity.finish import Finish
from application.entity.start import Start
from application.entity.wall import Wall
from application.system.UI.UI_elements.Text import Text
from application.system.UI.scenes.results import Results
from application.system.map import Map
from application.system.UI.scenes import main_menu

X_OFFSET = 40
Y_OFFSET = 40
X_SCALE = 40
Y_SCALE = 40


def timer_caster(time):  # get time in format m:s:ns ( str)
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
    def __init__(self, screen, difficult, images, is_fullscreen, scale):
        self.is_fullscreen = is_fullscreen
        self.scale = scale
        self.start_time = 0
        self.running = True
        self.screen = screen
        self.start = False
        self.finish = False

        self.images = images
        self.objects_list = pygame.sprite.Group()
        self.player_list = pygame.sprite.Group()

        x_offset = int(X_OFFSET * scale[0])
        y_offset = int(Y_OFFSET * scale[1])
        x_scale = int(X_SCALE * scale[0])
        y_scale = int(Y_SCALE * scale[1])
        self.size_font = int(16 * scale[1])
        self.difficult = difficult
        self.maze_map = Map(difficult, x_offset, y_offset, x_scale, y_scale)
        self.maze_map.put_objects(self.player_list, self.objects_list, self.images)
        self.text_timer = Text("00:00:000", self.size_font, (0, 0, 0))

    def _render(self):
        self.screen.fill((255, 255, 255))
        self.player_list.draw(self.screen)

        self.objects_list.draw(self.screen)

        self.screen.blit(self.text_timer.textSurf, (self.screen.get_width() // 2, int(self.scale[1] * 10)))
        pygame.display.flip()

    def _check_collision(self):
        for player in self.player_list:
            for collide_obj in self.objects_list:
                if pygame.sprite.collide_circle(player, collide_obj):
                    if isinstance(collide_obj, Wall):
                        player.back_after_collide()
                    if isinstance(collide_obj, Start):
                        self.start = True
                        self.finish = False
                    if isinstance(collide_obj, Finish):
                        self.finish = True
                        if self.start:
                            self.running = False
                            Results(self.screen, self.images, self.is_fullscreen, self.scale, self.text_timer.get_str(),
                                    self.difficult).run()

    def _update(self):
        self.player_list.sprites()[0].move(self.screen.get_width(), self.screen.get_height())
        self._update_timer()

    def _update_timer(self):
        if not self.start:
            self.start_time = pygame.time.get_ticks()
        elif not self.finish:
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
            self.player_list.sprites()[0].forward = True
        else:
            self.player_list.sprites()[0].forward = False
        if keys[pygame.K_d]:
            self.player_list.sprites()[0].turn_right = True
        else:
            self.player_list.sprites()[0].turn_right = False

        if keys[pygame.K_a]:
            self.player_list.sprites()[0].turn_left = True
        else:
            self.player_list.sprites()[0].turn_left = False

    def run(self):
        timer = pygame.time.Clock()

        while self.running:
            timer.tick(60)
            self._handle_events()
            self._check_collision()
            self._update()
            self._render()
