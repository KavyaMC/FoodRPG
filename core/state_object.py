class StateObject:
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