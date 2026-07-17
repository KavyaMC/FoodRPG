from core.base.controls import Button
from core.base.screen import ControlScreen
from core.controllers.new_game_controller import NewGameController


class NewGameScreen(ControlScreen):
    def __init__(self, state):
        super().__init__(state, title="New Game", description="Welcome to character creation")

        self.controller = NewGameController(state, self)

        self.player_name = ""
        self.business_sector = ""
        self.business_type = ""
        self.business_model = ""
        self.platform = ""
        self.business_name = ""

        self.add_controls(Button("start", self.start), Button("back", self.controller.back))

    def start(self):
        data = {
            "player_name": self.player_name,
            "business_sector": self.business_sector,
            "business_type": self.business_type,
            "business_model": self.business_model,
            "platform": self.platform,
            "business_name": self.business_name,
        }

        self.controller.start(data)
