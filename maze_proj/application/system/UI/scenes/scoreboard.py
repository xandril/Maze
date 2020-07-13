import pygame

from application.system.UI.UI_elements.Text import Text
from application.system.UI.UI_elements.button import Button
from application.system.UI.scenes import main_menu
from application.system.colors import Colors


class Scoreboard:
    def __init__(self, screen, images, is_fullscreen, scale):
        self.is_fullscreen = is_fullscreen
        self.scale = scale
        self.screen = screen
        self.running = True
        self.click = False
        self.images = images
        self.score_list = []

        self.elements = pygame.sprite.Group()
        self.font_size = int(16 * scale[1])
        self.header_font_size = int(20 * scale[1])
        button_w = int(100 * scale[0])
        button_h = int(20 * scale[1])
        x_offset = button_w
        x_pos_button = x_offset + button_h * 2
        y_pos_button = button_h + button_h

        labels = ["easy", "normal", "hard", "back"]
        for label in labels:
            x_pos_button += x_offset
            button = Button(Colors.RED, (button_w, button_h), label, self.font_size)
            button.set_pos((x_pos_button, y_pos_button))
            self.elements.add(button)

    def _load_score_list(self, path):
        self.score_list.clear()
        with open(path, 'r') as file_path:
            for line in file_path.readlines():
                line = line.strip('\n')
                self.score_list.append(line)

    def _draw_text(self, x_pos):
        y_offset = self.font_size * 2
        y_pos = 60
        for line in self.score_list:
            y_pos += y_offset
            text = Text(line, self.font_size, Colors.BLACK)
            self.screen.blit(text.textSurf, (x_pos - int(30 * self.scale[0]) // 2, y_pos))

    def _render(self):
        self.screen.fill((255, 255, 255))
        self.elements.draw(self.screen)
        x_pos = self.screen.get_width() // 2
        info = Text("Scoreboard", self.header_font_size, Colors.BLACK)
        x_pos -= info.textSurf.get_width() // 2
        self.screen.blit(info.textSurf,
                         (x_pos, int(self.scale[1]) * 40))
        self._draw_text(x_pos)

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
                        elif btn.get_label() == "easy":
                            self._load_score_list("score/easy.txt")
                        elif btn.get_label() == "normal":
                            self._load_score_list("score/normal.txt")
                        elif btn.get_label() == "hard":
                            self._load_score_list("score/hard.txt")
                else:
                    btn.set_color(Colors.RED)

    def run(self):
        timer = pygame.time.Clock()
        while self.running:
            timer.tick(60)
            self._handle_events()
            self._check_buttons()
            self._render()
