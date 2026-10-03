from .clock import GameClock
from .mode import GameplayMode


class GameplayState:
    def __init__(self, session):
        self.session = session
        self.clock = GameClock(session)
        self.mode = GameplayMode.LOADING

    def start(self):
        self.mode = GameplayMode.PLAYING

    def pause(self):
        self.mode = GameplayMode.PAUSED

    def resume(self):
        self.mode = GameplayMode.PLAYING

    def start_tutorial(self):
        self.mode = GameplayMode.TUTORIAL

    def start_interaction(self):
        self.mode = GameplayMode.INTERACTION
