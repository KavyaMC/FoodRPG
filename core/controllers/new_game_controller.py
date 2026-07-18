import json
from pathlib import Path

from core.base.controller import Controller
from core.controllers.save_slots_controller import (
    SaveSlotMode,
    SaveSlotsController,
)
from core.models.player import Player
from UI.save_slots_menu import SaveSlotsScreen


class NewGameController(Controller):
    def __init__(self, state, screen):
        super().__init__(state, screen)

        config = Path("config") / "business_models.json"

        with open(config, "r", encoding="utf-8") as file:
            self.business_data = json.load(file)

        self.sectors = list(self.business_data["sectors"].keys())

    def business_sector_changed(self, sector):
        categories = list(self.business_data["sectors"][sector]["categories"].keys())

        self.screen.business_category.set_options(categories)
        self.screen.business_type.set_options([])
        self.screen.business_model.set_options([])

    def business_category_changed(self, category):
        sector = self.screen.business_sector.value

        types = list(self.business_data["sectors"][sector]["categories"][category]["types"].keys())

        self.screen.business_type.set_options(types)
        self.screen.business_model.set_options([])

    def business_type_changed(self, business_type):
        sector = self.screen.business_sector.value
        category = self.screen.business_category.value

        models = self.business_data["sectors"][sector]["categories"][category]["types"][
            business_type
        ]["models"]

        self.screen.business_model.set_options(models)

    def create_character(self):
        player = Player(
            player_name=self.screen.player_name.value,
            business_name=self.screen.business_name.value,
            business_sector=self.screen.business_sector.value,
            business_category=self.screen.business_category.value,
            business_type=self.screen.business_type.value,
            business_model=self.screen.business_model.value,
            ownership_model=self.screen.ownership_model.value,
        )

        try:
            player.validate()

        except ValueError as error:
            notification = self.notify.error(
                "Character Creation Failed",
                str(error),
            )

            self.speak(notification.title)
            self.speak(notification.message)
            return

        controller = SaveSlotsController(
            self.state,
            None,
            SaveSlotMode.SAVE,
            player,
        )

        screen = SaveSlotsScreen(
            self.state,
            controller,
        )

        controller.screen = screen

        self.push(screen)

    def cancel(self):
        self.pop()
