class StateObject:
    def __init__(self, state):
        self.state = state

    @property
    def game(self):
        return self.state.game

    @property
    def screens(self):
        return self.state.screen_manager

    @property
    def settings(self):
        return self.state.settings

    @property
    def save_load(self):
        return self.state.save_load

    @property
    def notify(self):
        return self.state.notifications

    @property
    def speech(self):
        return self.state.speech

    def speak(self, text, interrupt=False):
        self.speech.speak(text, interrupt)

    @property
    def verbosity(self):
        return self.state.speech.verbosity

    def set_verbosity(self, verbosity):
        self.speech.set_verbosity(verbosity)

    @property
    def keybindings(self):
        return self.state.keybindings

    @property
    def gameplay(self):
        return self.state.gameplay

    @property
    def session(self):
        return self.gameplay.session
