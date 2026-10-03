from ..base.controller import Controller
from .save_slots_controller import (
    SaveSlotMode,
    SaveSlotsController,
)
from .settings_controller import SettingsController


class OptionsController(Controller):
    def __init__(self, state):
        super().__init__(state)

        self.confirm_return = False
        self.confirm_quit = False

    def open(self):
        menu = self.get_menu("options")
        self.load_menu(menu)
        self.push(self.screen)

    def save(self):
        controller = SaveSlotsController(
            self.state,
            SaveSlotMode.SAVE,
        )

        controller.on_saved = self.save_completed
        controller.open()

    def save_completed(self, slot):
        self.screens.pop()

    def settings(self):
        controller = SettingsController(self.state)
        controller.open()

    def return_to_menu(self):
        if not self.confirm_return:
            self.confirm_return = True

            notification = self.notify.warning(
                "Return to Main Menu",
                (
                    "Current progress will not be saved. "
                    "Press Enter again to return to the "
                    "Main Menu. Press Escape to cancel."
                ),
            )

            self.speak(notification.title)
            self.speak(notification.message)
            return

        self.confirm_return = False
        self.game.return_to_main_menu()

    def quit(self):
        if not self.confirm_quit:
            self.confirm_quit = True

            notification = self.notify.warning(
                "Quit Game",
                (
                    "Press Save to save your progress before "
                    "quitting, or press Quit again to quit "
                    "without saving."
                ),
            )

            self.speak(notification.title)
            self.speak(notification.message)
            return

        self.confirm_quit = False
        self.game.quit()

    def continue_game(self):
        self.state.gameplay.resume()
        self.screens.pop()
