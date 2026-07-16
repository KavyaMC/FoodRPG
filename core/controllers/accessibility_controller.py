from UI.speech_menu import SpeechScreen

from ..base.controller import Controller


class AccessibilityController(Controller):
    def __init__(self, state, screen):
        super().__init__(state, screen)

    def speech(self):
        self.push(SpeechScreen(self.state))

    def back(self):
        self.pop()
