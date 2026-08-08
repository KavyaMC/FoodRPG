from enum import Enum


class GameplayMode(Enum):
    LOADING = "loading"
    TUTORIAL = "tutorial"
    PLAYING = "playing"
    PAUSED = "paused"
    INTERACTION = "interaction"
