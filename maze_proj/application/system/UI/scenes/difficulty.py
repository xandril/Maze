import pygame

from application.system.UI.UI_elements.Text import Text
from application.system.UI.scenes import main_menu
from application.system.UI.UI_elements.button import Button
from application.system.UI.scenes.game import Game
from application.system.colors import Colors


class Difficulty:
    def __init__(self, screen, images, is_fullscreen, scale):
        self.is_fullscreen = is_fullscreen
        self.scale = scale
        self.screen = screen
        self.running = True
        self.click = False
        self.images = images

        self.elements = pygame.sprite.Group()
        labels = ["easy", "normal", "hard", "back"]
        x_pos_button = self.screen.get_width() // 2
        scale_y_offset = int(50 * scale[1])
        y_pos_button = scale_y_offset
        self.font_size = int(16 * scale[1])
        self.header_font_size = int(20 * scale[1])
        for label in labels:
            y_pos_button += scale_y_offset
            button = Button(Colors.RED, (int(100 * scale[0]), int(20 * scale[1])), label, self.font_size)
            button.set_pos((x_pos_button, y_pos_button))
            self.elements.add(button)

    def _render(self):
        self.screen.fill((255, 255, 255))
        self.elements.draw(self.screen)
        name = Text("Difficulty", self.header_font_size, Colors.BLACK)
        self.screen.blit(name.textSurf,
                         (self.screen.get_width() // 2 - name.textSurf.get_width() // 2, int(self.scale[1]) * 10))

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
                        self.running = False
                        if btn.get_label() == "back":
                            main_menu.MainMenu(self.screen, self.images, self.is_fullscreen, self.scale).run()
                        else:
                            difficult = btn.get_label()
                            Game(self.screen, difficult, self.images, self.is_fullscreen, self.scale).run()
                else:
                    btn.set_color(Colors.RED)

    def run(self):
        timer = pygame.time.Clock()
        while self.running:
            timer.tick(60)
            self._handle_events()
            self._check_buttons()
            self._render()
