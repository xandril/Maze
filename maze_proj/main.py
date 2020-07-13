import pygame

from application.app import App
from application.system.UI.UI_elements.text_input import TextInput


def main():
    App(int(800 * 0.8), int(600 * 0.8), "dafaq", False).start()


if __name__ == "__main__":
    main()

