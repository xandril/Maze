import pygame

from application.system.UI.UI_elements.Text import Text
from application.system.UI.UI_elements.Text_box import TextBox
from application.system.UI.UI_elements.button import Button
from application.system.UI.scenes import main_menu
from application.system.UI.scenes.scoreboard import Scoreboard
from application.system.colors import Colors


def key_func(item):  # for list sort
    return item[1]


class Results:
    def __init__(self, screen, images, is_fullscreen, scale, time, difficult):
        self.is_fullscreen = is_fullscreen
        self.scale = scale
        self.screen = screen
        self.running = True
        self.click = False
        self.images = images
        self.time = time
        self.difficult = difficult
        self.score_list = []
        self._load_score_list(self.difficult)
        self.elements = pygame.sprite.Group()
        self.record = False
        labels = ["back"]
        # self.user_name = None
        self.user_box = None
        self.font_size = int(16 * scale[1])
        self.header_font_size = int(20 * scale[1])
        x_pos_button = self.screen.get_width() // 2
        scale_y_offset = int(100 * scale[1])
        y_pos_button = scale_y_offset

        if self.score_list[self.score_list.__len__() - 1][1] > time:
            labels.insert(0, "add in top")
            self.user_box = TextBox(Colors.BLUE, (int(100 * scale[0]), int(20 * scale[1])), self.font_size+2)
            self.user_box.set_pos((x_pos_button-60*self.scale[0], y_pos_button))

            self.record = True

        for label in labels:
            y_pos_button += scale_y_offset
            button = Button(Colors.RED, (int(100 * scale[0]), int(20 * scale[1])), label, self.font_size)
            button.set_pos((x_pos_button, y_pos_button))
            self.elements.add(button)

    def _render(self):
        self.screen.fill((255, 255, 255))
        self.elements.draw(self.screen)
        x_pos = self.screen.get_width() // 2
        info = Text("Congratulations! You Won!!", self.header_font_size, Colors.BLACK)
        time = Text("your time: " + self.time, self.header_font_size, Colors.BLACK)
        self.screen.blit(info.textSurf,
                         (x_pos - info.textSurf.get_width() // 2, int(self.scale[1]) * 40))
        self.screen.blit(time.textSurf,
                         (x_pos - time.textSurf.get_width() // 2,
                          self.screen.get_height() // 2 - self.header_font_size * 4))

        if self.record:
            self.user_box.draw(self.screen)


        pygame.display.flip()

    def _handle_events(self):
        self.click = False
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True
        if self.record:
            self.user_box.handle_text(events)

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
                        if btn.get_label() == "add in top":
                            user = self.user_box.get_text().strip("")

                            self.score_list.append([user, self.time])
                            self.score_list.sort(key=key_func, reverse=False)
                            self._edit_score_list(self.difficult)
                            Scoreboard(self.screen, self.images, self.is_fullscreen, self.scale).run()
                else:
                    btn.set_color(Colors.RED)

    def run(self):
        timer = pygame.time.Clock()
        while self.running:
            timer.tick(60)
            self._handle_events()
            self._check_buttons()
            self._render()

    def _load_score_list(self, difficult):
        path = "score/" + difficult + ".txt"
        with open(path, 'r') as file:
            next(file)  # skip header
            for line in file.readlines():
                line = line.strip('\n')
                rank, name, time = line.split(" ")
                print("this " + rank, name, time)
                self.score_list.append([name, time])
            print(self.score_list)

    def _edit_score_list(self, difficult):
        # add_header
        path = "score/" + difficult + ".txt"
        with open(path, 'w') as file:
            print(difficult + "_mode", file=file)
            rank = 0
            for element in self.score_list:
                rank += 1
                if rank == 11:
                    break

                print(str(rank) + ". " + element[0] + " " + element[1], file=file)
