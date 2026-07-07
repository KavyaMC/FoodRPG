class Controller:
    def __init__(self, state):
        self.state = state


@property
def game(self):
    return self.state.game

    @property
    def screens(self):
        return self.state.screen_manager

    def speak(self, text, interrupt=False):
        self.state.speak(text, interrupt)

    def push(self, screen):
        self.screens.push_screen(screen)

    def pop(self):
        self.screens.pop_screen()

    def replace(self, screen):
        self.screens.replace_screen(screen)

    def quit(self):
        self.state.quit()
