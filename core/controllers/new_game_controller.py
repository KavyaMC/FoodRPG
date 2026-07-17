from ..base.controller import Controller


class NewGameController(Controller):
    def __init__(self, state, screen):
        super().__init__(state, screen)

    def start(self, data):
        notification = self.notify.info(
            "New Game", "Character creation is ready for future implementation."
        )

        self.speak(notification.title)
        self.speak(notification.message)

    def back(self):
        self.pop()
