from dataclasses import dataclass

from ..models.player import Player


@dataclass(slots=True)
class Session:
    SAVE_VERSION = 1

    player: Player

    day: int = 1
    hour: int = 6
    minute: int = 0

    location: str = ""
    objective: str = ""
    current_task: str = ""
    current_activity: str = ""

    tutorial_completed: bool = False

    play_time_seconds: int = 0

    @property
    def player_name(self):
        return self.player.player_name

    @property
    def business_name(self):
        return self.player.business_name

    @property
    def business_type(self):
        return self.player.business_type

    @property
    def time(self):
        return f"{self.hour:02}:{self.minute:02}"

    @property
    def date(self):
        return f"Day {self.day}"

    @classmethod
    def new(cls, player, defaults):
        return cls(
            player=player,
            day=defaults.get("start_day", 1),
            hour=defaults.get("start_hour", 6),
            minute=defaults.get("start_minute", 0),
            location=defaults.get("location", ""),
            objective=defaults.get("objective", ""),
            current_task=defaults.get(
                "current_task",
                "",
            ),
            current_activity=defaults.get(
                "current_activity",
                "",
            ),
            tutorial_completed=defaults.get(
                "tutorial_completed",
                False,
            ),
            play_time_seconds=defaults.get(
                "play_time_seconds",
                0,
            ),
        )

    def to_dict(self):
        return {
            "version": self.SAVE_VERSION,
            "player": self.player.to_dict(),
            "day": self.day,
            "hour": self.hour,
            "minute": self.minute,
            "location": self.location,
            "objective": self.objective,
            "current_task": self.current_task,
            "current_activity": self.current_activity,
            "tutorial_completed": self.tutorial_completed,
            "play_time_seconds": self.play_time_seconds,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            player=Player.from_dict(data.get("player", {})),
            day=data.get("day", 1),
            hour=data.get("hour", 6),
            minute=data.get("minute", 0),
            location=data.get("location", ""),
            objective=data.get("objective", ""),
            current_task=data.get(
                "current_task",
                "",
            ),
            current_activity=data.get(
                "current_activity",
                "",
            ),
            tutorial_completed=data.get(
                "tutorial_completed",
                False,
            ),
            play_time_seconds=data.get(
                "play_time_seconds",
                0,
            ),
        )

    def __str__(self):
        return f"{self.player_name} | {self.date} | {self.time}"
