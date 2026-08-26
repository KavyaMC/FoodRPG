from application.base.controls import (
    Button,
    ComboBox,
    TextField,
)
from application.base.screen import ControlScreen
from application.controllers.new_game_controller import (
    NewGameController,
)


class NewGameScreen(ControlScreen):
    def __init__(self, state):
        super().__init__(
            state,
            title="New Game",
            description="Create your character.",
        )

        self.controller = NewGameController(
            state,
            self,
        )

        businesses = state.content.load(
            "businesses.json",
        )

        self.player_name = TextField(
            "Player Name",
            placeholder="Enter your name",
        )

        self.business_name = TextField(
            "Business Name",
            placeholder="Enter your business name",
        )

        self.business_category = ComboBox(
            "Business Category",
            businesses,
        )

        self.add_controls(
            self.player_name,
            self.business_name,
            self.business_category,
            Button(
                "Create Character",
                self.controller.create_character,
            ),
            Button(
                "Cancel",
                self.controller.cancel,
            ),
        )
