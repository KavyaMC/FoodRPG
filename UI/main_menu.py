from core.base.controls import Button
from core.base.screen import ControlScreen
from core.controllers.main_menu_controller import MainMenuController


class MainMenuScreen(ControlScreen):
    def __init__(self, state):
        super().__init__(state, title="Main Menu", description="Welcome to main menu")

        self.controller = MainMenuController(state, self)

        self.add_controls(
            Button("New Game", self.controller.new_game),
            Button("Continue", self.controller.continue_game),
            Button("Settings", self.controller.settings),
            Button("Help", self.controller.help),
            Button("Credits", self.controller.credits),
            Button("Quit", self.controller.quit),
        )

    def handle_input(self, event):
        self.controller.handle_input(event)
