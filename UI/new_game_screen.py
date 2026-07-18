from core.base.controls import (
    Button,
    ComboBox,
    LabelField,
    TextField,
)
from core.base.screen import ControlScreen
from core.controllers.new_game_controller import NewGameController


class NewGameScreen(ControlScreen):
    def __init__(self, state):
        super().__init__(
            state,
            title="New Game",
            description="Create your character.",
        )

        self.controller = NewGameController(state, self)

        self.player_name = TextField(
            "Player Name",
            placeholder="Enter your name",
        )

        self.business_name = TextField(
            "Business Name",
            placeholder="Green Acres",
        )

        self.business_sector = ComboBox(
            "Business Sector",
            self.controller.sectors,
            on_changed=self.controller.business_sector_changed,
        )

        self.business_category = ComboBox(
            "Business Category",
            [],
            on_changed=self.controller.business_category_changed,
        )

        self.business_type = ComboBox(
            "Business Type",
            [],
            on_changed=self.controller.business_type_changed,
        )

        self.business_model = ComboBox(
            "Business Model",
            [],
        )

        self.ownership_model = LabelField(
            "Ownership Model",
            "Entrepreneur",
        )

        self.add_controls(
            self.player_name,
            self.business_name,
            self.business_sector,
            self.business_category,
            self.business_type,
            self.business_model,
            self.ownership_model,
            Button(
                "Create Character",
                self.controller.create_character,
            ),
            Button(
                "Cancel",
                self.controller.cancel,
            ),
        )
