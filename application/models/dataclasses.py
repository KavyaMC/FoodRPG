from dataclasses import dataclass
from typing import Callable


@dataclass
class Action:
    label: str
    action: Callable

    def execute(self):
        return self.action()


@dataclass
class MenuItem:
    label: str
    action: Action | None = None
    submenu: str | None = None


@dataclass
class Menu:
    items: list[MenuItem]
