from ..base.controller import Controller
from .help_controller import HelpController
from .settings_controller import SettingsController


class OptionsController(Controller):
    MENU_FILE = "menus.json"

    def __init__(self, state):
        super().__init__(state)

    def open(self):
        menu = self.get_menu("options")

        self.load_menu(menu)
        self.push(self.screen)

    def continue_game(self):
        self.gameplay.resume()
        self.pop()

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
        self.speak(
            "Notifications are not implemented yet.",
        )

    def achievements(self):
        self.speak(
            "Achievements are not implemented yet.",
        )

    def quit(self):
        self.game.quit()
