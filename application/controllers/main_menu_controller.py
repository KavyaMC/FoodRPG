from application.controllers.save_slots_controller import (
    SaveSlotMode,
    SaveSlotsController,
)
from application.UI.help_menu import HelpScreen
from application.UI.new_game_screen import NewGameScreen
from application.UI.save_slots_menu import SaveSlotsScreen
from application.UI.settings_menu import SettingsScreen

from ..base.controller import Controller


class MainMenuController(Controller):
    def __init__(self, state, screen):
        super().__init__(
            state,
            screen,
        )

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

        self.screens.pop()

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
        self.state.gameplay_flow.enter()

    def settings(self):
        self.push(
            SettingsScreen(self.state),
        )

    def help(self):
        self.push(
            HelpScreen(self.state),
        )

    def quit(self):
        self.game.quit()
