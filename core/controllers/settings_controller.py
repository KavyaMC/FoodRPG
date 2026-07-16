from UI.accessibility_menu import AccessibilityScreen

from ..base.controller import Controller


class SettingsController(Controller):
    def __init__(self, state, screen):
        super().__init__(state, screen)

    def accessibility(self):
        self.push(AccessibilityScreen(self.state))

    def save(self):
        self.speak("Settings saved.")

    def back(self):
        self.pop()
