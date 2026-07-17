from core.controllers.save_slots_controller import SaveSlotMode, SaveSlotsController
from UI.help_menu import HelpScreen
from UI.save_slots_menu import SaveSlotsScreen
from UI.settings_menu import SettingsScreen

from ..base.controller import Controller


class MainMenuController(Controller):
    def __init__(self, state, screen):
        super().__init__(state, screen)

    def new_game(self):
        self.speak("Start a new game")

    def continue_game(self):
        controller = SaveSlotsController(self.state, None, SaveSlotMode.LOAD)
        screen = SaveSlotsScreen(self.state, controller)
        controller.screen = screen
        self.push(screen)

    def settings(self):
        self.push(SettingsScreen(self.state))

    def help(self):
        self.push(HelpScreen(self.state))

    def credits(self):
        self.speak("Food RPG, v0.1.0. Developed by KavyaMC.")

    def quit(self):
        self.game.quit()
