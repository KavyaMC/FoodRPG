from dataclasses import dataclass
from enum import Enum, auto


class NotificationType(Enum):
    INFO = auto()
    SUCCESS = auto()
    WARNING = auto()
    ERROR = auto()


@dataclass(slots=True)
class GameplayNotification:
    title: str
    message: str
    type: NotificationType
    day: int
    hour: int
    minute: int
    read: bool = False


class GameplayNotifications:
    def __init__(self):
        self._notifications = []

    def add(
        self,
        title,
        message,
        notification_type=NotificationType.INFO,
        day=1,
        hour=0,
        minute=0,
    ):
        notification = GameplayNotification(
            title=title,
            message=message,
            type=notification_type,
            day=day,
            hour=hour,
            minute=minute,
        )

        self._notifications.append(notification)

        return notification

    def history(self):
        return list(self._notifications)

    def unread(self):
        return [notification for notification in self._notifications if not notification.read]

    def unread_count(self):
        return len(self.unread())

    def mark_read(self, notification):
        notification.read = True

    def mark_all_read(self):
        for notification in self._notifications:
            notification.read = True
