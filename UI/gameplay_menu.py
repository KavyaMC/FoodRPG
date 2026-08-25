from core.base.controls import Button
from core.base.screen import ControlScreen
from core.controllers.gameplay_controller import GameplayController

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
                "Status",
                self.controller.session,
            ),
        )
