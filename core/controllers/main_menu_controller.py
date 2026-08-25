from core.controllers.save_slots_controller import (
    SaveSlotMode,
    SaveSlotsController,
)
from core.helpers.document_helper import open_document
from UI.gameplay_menu import GameplayScreen
from UI.help_menu import HelpScreen
from UI.new_game_screen import NewGameScreen
from UI.save_slots_menu import SaveSlotsScreen
from UI.settings_menu import SettingsScreen

from ..base.controller import Controller


class MainMenuController(Controller):
    def __init__(self, state, screen):
        super().__init__(state, screen)

    def new_game(self):
        controller = SaveSlotsController(
            self.state,
            None,
            SaveSlotMode.SAVE,
        )

        screen = SaveSlotsScreen(
            self.state,
            controller,
        )

        controller.screen = screen
        controller.on_slot_selected = self.new_game_slot_selected

        self.push(screen)

    def new_game_slot_selected(self, slot):
        self.state.new_game_slot = slot

        self.pop()

        self.push(
            NewGameScreen(self.state),
        )

    def continue_game(self):
        self.replace(
            NewGameScreen(self.state),
        )

    def load_game(self):
        controller = SaveSlotsController(
            self.state,
            None,
            SaveSlotMode.LOAD,
        )

        screen = SaveSlotsScreen(
            self.state,
            controller,
        )

        controller.screen = screen
        controller.on_loaded = self.game_loaded

        self.push(screen)

    def game_loaded(self, session):
        self.replace(GameplayScreen(self.state))

    def settings(self):
        self.push(
            SettingsScreen(self.state),
        )

    def help(self):
        self.push(
            HelpScreen(self.state),
        )

    def credits(self):
        open_document("credits.md")

    def quit(self):
        self.game.quit()
