from application.base.controls import Button
from application.base.screen import ControlScreen
from application.gameplay.controllers.options_controller import (
    GameplayOptionsController,
)


class OptionsScreen(ControlScreen):
    def __init__(self, state):
        super().__init__(
            state,
            title="Game Paused",
            description="Choose an option",
        )

        self.controller = GameplayOptionsController(
            state,
            self,
        )

        self.add_controls(
            Button("Continue", self.controller.continue_game),
            Button(
                "Save",
                self.controller.save,
            ),
            Button(
                "Settings",
                self.controller.settings,
            ),
            Button(
                "Return to Main Menu",
                self.controller.return_to_menu,
            ),
            Button(
                "Quit",
                self.controller.quit,
            ),
        )
