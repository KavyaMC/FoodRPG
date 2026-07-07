import pygame

from .base_controller import Controller


class MainMenuController(Controller):
    def __init__(self, state, screen):
        super().__init__(state)
        self.screen = screen

    def handle_input(self, event):
        if event.type != pygame.KEYDOWN:
            return

        match event.key:
            case pygame.K_UP:
                self.screen.move_previous()

            case pygame.K_DOWN:
                self.screen.move_next()

            case pygame.K_RETURN | pygame.K_KP_ENTER:
                self.screen.activate_current()

            case pygame.K_ESCAPE:
                self.quit()

    def new_game(self):
        pass

    def continue_game(self):
        pass

    def settings(self):
        pass

    def help(self):
        pass

    def credits(self):
        pass

    def quit(self):
        self.quit()
