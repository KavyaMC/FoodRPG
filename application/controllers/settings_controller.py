from ..base.controller import Controller


class SettingsController(Controller):
    def __init__(self, state, screen):
        super().__init__(state, screen)

    def backend_changed(self, backend):
        self.speech.set_mode(backend)

        self.settings.set(
            "speech",
            "backend",
            backend,
        )

        self.settings.save()

        notification = self.notify.success(
            "Speech Backend Updated",
            (f"Speech backend changed to {backend}."),
        )

        self.speak(notification.title)
        self.speak(notification.message)

    def verbosity_changed(self, verbosity):
        self.settings.set(
            "speech",
            "verbosity",
            verbosity,
        )

        self.settings.save()

        notification = self.notify.success(
            "Speech Verbosity Updated",
            f"Speech verbosity changed to {verbosity}.",
        )

        self.speak(notification.title)
        self.speak(notification.message)

    def back(self):
        self.pop()
