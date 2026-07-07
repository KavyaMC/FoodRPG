from services.screen_manager import ScreenManager
from services.speech import Speech


class GameState:
    def __init__(self):
        self.running = True
        self._init_services()

    def _init_services(self):
        self.speech = Speech()
        self.screen_manager = ScreenManager()

    def speak(self, text, interrupt=False):
        self.speech.speak(text, interrupt)
