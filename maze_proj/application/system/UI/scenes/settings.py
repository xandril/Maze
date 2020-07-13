import pygame

from application.system.UI.UI_elements.Text import Text
from application.system.UI.UI_elements.button import Button
from application.system.UI.scenes import main_menu
from application.system.colors import Colors


class Settings:
    def __init__(self, screen, images, is_fullscreen, scale):
        self.scale = scale
        self.is_fullscreen = is_fullscreen
        self.screen = screen
        self.running = True
        self.click = False
        self.images = images
        name_list = [(800, 600), (1024, 600), (1280, 720), (1920, 1080), "fullscreen", "back"]
        self.elements = pygame.sprite.Group()
        base_y_scale = int(50 * self.scale[1])
        button_y_pos = base_y_scale
        button_x_pos = self.screen.get_width() // 2
        self.font_size = int(scale[1] * 15)
        self.header_font_size = int(scale[1] * 20)

        for item in name_list:
            button_y_pos += base_y_scale
            label = item if type(item) == str else str(item[0]) + 'X' + str(item[1])
            button = Button(Colors.RED, (int(100 * scale[0]), int(20 * scale[1])), label, self.font_size)
            button.set_pos((button_x_pos, button_y_pos))
            self.elements.add(button)

    def _render(self):

        self.screen.fill((255, 255, 255))
        self.elements.draw(self.screen)
        name = Text("Settings", self.header_font_size, Colors.BLACK)
        screen_res = Text("Screen Resolution and fullscreen", self.font_size, Colors.BLACK)
        text_pos_x = self.screen.get_width() // 2
        self.screen.blit(name.textSurf, (text_pos_x - name.textSurf.get_width() // 2, int(self.scale[1]) * 10))
        self.screen.blit(screen_res.textSurf,
                         (text_pos_x - screen_res.textSurf.get_width() // 2, self.header_font_size*2))

        pygame.display.flip()

    def _handle_events(self):
        self.click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

    def _check_buttons(self):
        mx, my = pygame.mouse.get_pos()

        for btn in self.elements:
            if isinstance(btn, Button):
                if btn.get_rect().collidepoint((mx, my)):
                    btn.set_color(Colors.GREEN)
                    if self.click:
                        if btn.get_label() == "back":
                            self.running = False
                            main_menu.MainMenu(self.screen, self.images, self.is_fullscreen, self.scale).run()
                        elif btn.get_label() == "fullscreen":
                            self.is_fullscreen = not self.is_fullscreen
                            if self.is_fullscreen:
                                self.screen = pygame.display.set_mode(
                                    (self.screen.get_width(), self.screen.get_height()), pygame.FULLSCREEN)
                            else:
                                self.screen = pygame.display.set_mode(
                                    (self.screen.get_width(), self.screen.get_height()))
                        else:
                            width, height = map(int, btn.get_label().split("X"))
                            # map(function, iterables)
                            width = int(0.8 * width)
                            height = int(0.8 * height)
                            if self.is_fullscreen:
                                self.screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
                            else:
                                self.screen = pygame.display.set_mode((width, height))

                            button_x = self.screen.get_width() // 2
                            base_y_scale = int(50 * self.scale[1])

                            button_y = base_y_scale
                            for res_btn in self.elements:
                                if isinstance(res_btn, Button):
                                    button_y += base_y_scale
                                    res_btn.set_pos((button_x, button_y))
                else:
                    btn.set_color(Colors.RED)

    def run(self):
        timer = pygame.time.Clock()
        while self.running:
            timer.tick(60)
            self._handle_events()
            self._check_buttons()
            self._render()
