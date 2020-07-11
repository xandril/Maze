import pygame

from System.UI.UI_elements.Text import Text
from System.UI.UI_elements.button import Button
from System.scenes.difficulty import Difficulty
from System.scenes.info import Info
from System.scenes.settings import Settings
from colors import Colors


class MainMenu:
    def __init__(self, screen, images, is_fullscreen, scale):
        self.header_font_size = int(20 * scale[1])
        self.is_fullscreen = is_fullscreen
        self.scale = scale

        self.screen = screen
        self.running = True
        self.click = False
        self.images = images
        self.elements = pygame.sprite.Group()
        labels = ["play", "settings", "score", "info", "exit"]
        x_pos_button = self.screen.get_width() // 2
        scale_y_offset = int(50 * scale[1])
        y_pos_button = scale_y_offset
        self.font_size = int(scale[1] * 16)
        for label in labels:
            y_pos_button += scale_y_offset
            button = Button(Colors.RED, (int(100 * scale[0]), int(20 * scale[1])), label, self.font_size)
            button.set_pos((x_pos_button, y_pos_button))
            self.elements.add(button)

    def _render(self):
        self.screen.fill(Colors.WHITE)
        self.elements.draw(self.screen)
        name = Text("Main menu", self.header_font_size, Colors.BLACK)
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
                        if btn.get_label() == "play":
                            Difficulty(self.screen, self.images, self.is_fullscreen, self.scale).run()
                        if btn.get_label() == "settings":
                            Settings(self.screen, self.images, self.is_fullscreen, self.scale).run()

                        if btn.get_label() == "info":
                            Info(self.screen, self.images, self.is_fullscreen, self.scale).run()
                        if btn.get_label() == "score":
                            pass
                        if btn.get_label() == "exit":
                            self.running = False
                else:
                    btn.set_color(Colors.RED)

    def run(self):
        timer = pygame.time.Clock()
        while self.running:
            timer.tick(60)
            self._handle_events()
            self._check_buttons()
            self._render()
