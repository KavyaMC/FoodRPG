from core.base.controller import Controller
from UI.status_menu import SessionScreen


class GameplayController(Controller):
    def __init__(self, state, screen):
        super().__init__(state, screen)

    def options(self):
        self.speak("Not implemented yet")

    def session(self):
        self.push(SessionScreen(self.state))
