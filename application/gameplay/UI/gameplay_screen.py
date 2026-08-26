from application import keybindings
from application.base.controls import Button
from application.base.screen import ControlScreen
from application.gameplay.controllers.gameplay_controller import (
    GameplayController,
)


class GameplayScreen(ControlScreen):
    def __init__(self, state):
        super().__init__(
            state,
            title="Gameplay",
            description="Welcome to the game",
        )

        self.controller = GameplayController(
            state,
            self,
        )

        self.add_controls(
            Button(
                "Options",
                self.controller.options,
            ),
            Button(
                "Session",
                self.controller.session,
            ),
        )

    def handle_input(self, event):
        if event.type != keybindings.KEYDOWN:
            return

        if event.key in keybindings.BACK_KEYS:
            self.controller.options()
            return

        super().handle_input(event)
