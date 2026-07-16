from UI.settings_menu import SettingsScreen

from ..base.controller import Controller


class MainMenuController(Controller):
    def __init__(self, state, screen):
        super().__init__(state, screen)

    def new_game(self):
        self.speak("Start a new game")

    def continue_game(self):
        self.speak("continue your previous game.")

    def settings(self):
        self.push(SettingsScreen(self.state))

    def help(self):
        self.speak("Learn more about the game and How to.")

    def credits(self):
        self.speak("Food RPG, v0.1.0. Developed by KavyaMC.")

    def quit(self):
        self.game.quit()
