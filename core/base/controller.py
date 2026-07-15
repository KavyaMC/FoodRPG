from .state_object import StateObject


class Controller(StateObject):
    def __init__(self, state, screen):
        super().__init__(state)
        self.screen = screen

    def push(self, screen):
        self.screens.push(screen)

    def pop(self):
        self.screens.pop()

    def replace(self, screen):
        self.screens.replace_screen(screen)

    def update(self):
        pass

    def quit(self):
        self.game.quit()
