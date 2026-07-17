from .services.notifications import NotificationService
from .services.save_load import SaveLoad
from .services.screen_manager import ScreenManager
from .services.settings import Settings
from .services.speech import Speech


class GameState:
    def __init__(self, game):
        self.game = game
        self.running = True
        self._init_services()

    def _init_services(self):
        self.settings = Settings()

        backend = self.settings.get("speech", "backend", "AUTO")
        enabled = self.settings.getboolean("speech", "enabled", True)

        self.speech = Speech(mode=backend, enabled=enabled)
        self.screen_manager = ScreenManager()
        self.save_load = SaveLoad()
        self.notifications = NotificationService()

    def speak(self, text, interrupt=False):
        self.speech.speak(text, interrupt)
