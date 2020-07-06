import pygame

from System.scenes import main_menu
from System.UI.UI_elements.button import Button
from System.scenes.game import Game


class Difficulty:
    def __init__(self, screen, weight, height):
        self.screen = screen
        self.weight = weight
        self.height = height
        self.running = True
        self.click = False

        self.elements = pygame.sprite.Group()
        easy_button = Button((255, 30, 30), (100, 20), "easy")
        normal_button = Button((255, 30, 30), (100, 20), "normal")
        hard_button = Button((255, 30, 30), (100, 20), "hard")
        back_button = Button((255, 30, 30), (100, 20), "back")
        easy_button.set_pos((self.weight // 2, 30))
        normal_button.set_pos((self.weight // 2, 80))
        hard_button.set_pos((self.weight // 2, 140))
        back_button.set_pos((self.weight // 2, 260))
        self.elements.add(easy_button)
        self.elements.add(normal_button)
        self.elements.add(hard_button)
        self.elements.add(back_button)

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
                if btn.get_label() == "easy":
                    if btn.get_rect().collidepoint((mx, my)) and self.click:
                        self.running = False
                        Game(self.screen, self.weight, self.height, "easy").run()
                if btn.get_label() == "normal":
                    if btn.get_rect().collidepoint((mx, my)) and self.click:
                        self.running = False
                        Game(self.screen, self.weight, self.height, "normal").run()

                if btn.get_label() == "hard":
                    if btn.get_rect().collidepoint((mx, my)) and self.click:
                        self.running = False
                        Game(self.screen, self.weight, self.height, "hard").run()

                if btn.get_label() == "back":
                    if btn.get_rect().collidepoint((mx, my)) and self.click:
                        self.running = False
                        main_menu.MainMenu(self.screen, self.weight, self.height).run()

    def run(self):
        timer = pygame.time.Clock()
        while self.running:
            timer.tick(60)
            self._handle_events()
            self._check_buttons()
            self._render()
