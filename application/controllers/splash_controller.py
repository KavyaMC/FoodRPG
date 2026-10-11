from ..base.controller import Controller
from .main_menu_controller import MainMenuController


class SplashController(Controller):
    DURATION = 3.0

    def __init__(self, state):
        super().__init__(state)

        self.elapsed = 0.0

    def open(self):
        self.elapsed = 0.0

        self.screen.title = "Food RPG"
        self.screen.description = "An accessible food business simulation."

        self.screen.clear_controls()

        self.push(self.screen)

    def update(self, dt):
        self.elapsed += dt

        if self.elapsed < self.DURATION:
            return

        self.screens.pop()

        controller = MainMenuController(
            self.state,
        )

        controller.open()
