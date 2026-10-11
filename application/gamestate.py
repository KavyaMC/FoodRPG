from helpers.DataLoader import DataLoader
from models.item_catalog import ItemCatalog

from .gameplay.state import GameplayState
from .services.content_loader import ContentLoader
from .services.keybindings import KeyBindings
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
        self.current_save_slot = None
        data_loader = DataLoader()
        item_data = data_loader.load("items.json")
        self.items = ItemCatalog(item_data)
        self._init_services()

    def _init_services(self):
        self.speach = Speech()
        self.settings = Settings()

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
        volume = float(
            self.settings.get("speech", "volume", str(Speech.DEFAULT_VOLUME))
        )
        rate = float(self.settings.get("speech", "rate", str(Speech.DEFAULT_RATE)))

        self.speech = Speech(
            mode=backend,
            verbosity=verbosity,
            volume=volume,
            rate=rate,
        )

        self.screen_manager = ScreenManager()
        self.save_load = SaveLoad()
        self.notifications = NotificationService()
        self.content = ContentLoader()
        self.keybindings = KeyBindings()

    def speak(self, text, interrupt=False):
        self.speech.speak(text, interrupt)

    def start_gameplay(self, session):
        self.gameplay = GameplayState(session)

    def save_game(self):
        if self.gameplay is None:
            raise RuntimeError(
                "Cannot save without an active gameplay state.",
            )

        if self.current_save_slot is None:
            raise RuntimeError(
                "Cannot save without an active save slot.",
            )

        self.save_load.save(
            self.current_save_slot,
            self.gameplay.session.to_dict(),
        )

    def end_gameplay(self):
        self.gameplay = None
        self.current_save_slot = None
