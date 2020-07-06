import pygame

from System.UI.UI_elements.button import Button
from System.scenes.difficulty import Difficulty
from System.scenes.info import Info


class MainMenu:
    def __init__(self, screen, weight, height):
        self.screen = screen
        self.weight = weight
        self.height = height
        self.running = True
        self.click = False

        self.elements = pygame.sprite.Group()
        game_button = Button((255, 30, 30), (100, 20), "play")
        settings_button = Button((255, 30, 30), (100, 20), "settings")
        score_button = Button((255, 30, 30), (100, 20), "score")
        info_button = Button((255, 30, 30), (100, 20), "info")
        exit_button = Button((255, 30, 30), (100, 20), "exit")
        game_button.set_pos((self.weight // 2, 30))
        settings_button.set_pos((self.weight // 2, 80))
        score_button.set_pos((self.weight // 2, 140))
        info_button.set_pos((self.weight // 2, 200))
        exit_button.set_pos((self.weight // 2, 260))
        self.elements.add(game_button)
        self.elements.add(settings_button)
        self.elements.add(score_button)
        self.elements.add(info_button)
        self.elements.add(exit_button)

    def _render(self):
        self.screen.fill((255, 255, 255))
        self.elements.draw(self.screen)
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
                if btn.get_label() == "play":
                    if btn.get_rect().collidepoint((mx, my)) and self.click:
                        self.running = False
                        Difficulty(self.screen, self.weight, self.height).run()
                if btn.get_label() == "settings":
                    if btn.get_rect().collidepoint((mx, my)) and self.click:
                        pass
                if btn.get_label() == "score":
                    if btn.get_rect().collidepoint((mx, my)) and self.click:

                        pass
                if btn.get_label() == "info":
                    if btn.get_rect().collidepoint((mx, my)) and self.click:

                        Info(self.screen, self.weight, self.height).run()
                if btn.get_label() == "exit":
                    if btn.get_rect().collidepoint((mx, my)) and self.click:
                        self.running = False

    def run(self):
        timer = pygame.time.Clock()
        while self.running:
            timer.tick(60)
            self._handle_events()
            self._check_buttons()
            self._render()
