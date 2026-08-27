from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto


class NotificationType(Enum):
    INFO = auto()
    SUCCESS = auto()
    WARNING = auto()
    ERROR = auto()


@dataclass
class Notification:
    title: str
    message: str
    type: NotificationType
    created_at: datetime
    read: bool = False


class NotificationService:
    def __init__(self):
        self._notifications = []

    def add(self, title, message, notification_type=NotificationType.INFO):
        notification = Notification(
            title=title,
            message=message,
            type=notification_type,
            created_at=datetime.now(),
        )

        self._notifications.append(notification)
        return notification

    def info(self, title, message):
        return self.add(title, message, NotificationType.INFO)

    def success(self, title, message):
        return self.add(title, message, NotificationType.SUCCESS)

    def warning(self, title, message):
        return self.add(title, message, NotificationType.WARNING)

    def error(self, title, message):
        return self.add(title, message, NotificationType.ERROR)

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

    def clear(self):
        self._notifications.clear()
