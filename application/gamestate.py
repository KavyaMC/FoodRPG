from .gameplay.flow import Flow
from .gameplay.state import GameplayState
from .services.content_loader import ContentLoader
from .services.notifications import NotificationService
from .services.save_load import SaveLoad
from .services.screen_manager import ScreenManager
from .services.settings import Settings
from .services.speech import Speech


class GameState:
    def __init__(self, game):
        self.game = game
        self.running = True
        self.gameplay = None

        self._init_services()
        self.gameplay_flow = Flow(self)

    def _init_services(self):
        self.settings = Settings()
        self.content = ContentLoader()

        backend = self.settings.get(
            "speech",
            "backend",
            Speech.DEFAULT_BACKEND,
        )

        verbosity = self.settings.get(
            "speech",
            "verbosity",
            Speech.DEFAULT_VERBOSITY,
        )

        self.speech = Speech(
            mode=backend,
            verbosity=verbosity,
        )

        self.screen_manager = ScreenManager()
        self.save_load = SaveLoad()
        self.notifications = NotificationService()

    def speak(self, text, interrupt=False):
        self.speech.speak(
            text,
            interrupt,
        )

    def start_gameplay(self, session):
        self.gameplay = GameplayState(session)

    def end_gameplay(self):
        self.gameplay = None
