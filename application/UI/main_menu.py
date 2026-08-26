from application.base.controls import Button
from application.base.screen import ControlScreen
from application.controllers.main_menu_controller import MainMenuController


class MainMenuScreen(ControlScreen):
    def __init__(self, state):
        super().__init__(
            state,
            title="Main Menu",
            description="Welcome to the game.",
        )

        self.controller = MainMenuController(
            state,
            self,
        )

        self.add_controls(
            Button("New Game", self.controller.new_game),
            Button("Load Game", self.controller.load_game),
            Button("Settings", self.controller.settings),
            Button("Documentation", self.controller.help),
            Button("Quit", self.controller.quit),
        )
