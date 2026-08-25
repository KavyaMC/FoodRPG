from core.base.controller import Controller
from UI.resume_screen import ResumeScreen
from UI.status_menu import SessionScreen


class GameplayController(Controller):
    def __init__(self, state, screen):
        super().__init__(state, screen)

    def options(self):
        self.push(
            ResumeScreen(self.state),
        )

    def session(self):
        self.push(SessionScreen(self.state))
