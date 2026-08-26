from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Activity:
    id: str
    name: str
    duration: int
