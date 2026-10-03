from ..base.controller import Controller
from .gameplay_controller import (
    GameplayController,
)
from .help_controller import (
    HelpController,
)
from .new_game_controller import (
    NewGameController,
)
from .save_slots_controller import (
    SaveSlotMode,
    SaveSlotsController,
)
from .settings_controller import (
    SettingsController,
)


class MainMenuController(Controller):
    def __init__(self, state):
        super().__init__(state)

    def open(self):
        menu = self.get_menu("main_menu")

        self.load_menu(menu)

        self.push(self.screen)

    def new_game(self):
        controller = SaveSlotsController(
            self.state,
            SaveSlotMode.SAVE,
        )

        controller.on_slot_selected = self.new_game_slot_selected

        controller.open()

    def new_game_slot_selected(self, slot):
        self.state.new_game_slot = slot

        self.screens.pop()

        controller = NewGameController(
            self.state,
        )

        controller.open()

    def load_game(self):
        controller = SaveSlotsController(
            self.state,
            SaveSlotMode.LOAD,
        )

        controller.on_loaded = self.game_loaded

        controller.open()

    def game_loaded(self, session):
        controller = GameplayController(
            self.state,
        )

        controller.open()

    def settings(self):
        controller = SettingsController(
            self.state,
        )

        controller.open()

    def help(self):
        controller = HelpController(
            self.state,
        )

        controller.open()

    def notifications(self):
        # NotificationsController goes here.
        pass

    def achievements(self):
        # AchievementsController goes here.
        pass

    def quit(self):
        self.game.quit()
