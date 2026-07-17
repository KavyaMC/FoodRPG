from ..base.controller import Controller


class SpeechController(Controller):
    def __init__(self, state, screen):
        super().__init__(state, screen)

    def backend_changed(self, backend):
        self.speech.set_mode(backend)
        self.settings.set("speech", "backend", backend)
        self.settings.save()

        notification = self.notify.success(
            "Speech Backend Updated", f"Speech backend changed to {backend}."
        )

        self.speak(notification.title)
        self.speak(notification.message)

    def enabled_changed(self, enabled):
        if enabled:
            self.speech.set_enabled(True)
            self.settings.set("speech", "enabled", True)
            self.settings.save()

            notification = self.notify.success("Speech Enabled", "Speech output has been enabled.")

            self.speak(notification.title)
            self.speak(notification.message)

        else:
            notification = self.notify.info("Speech Disabled", "Speech output has been disabled.")

            self.speak(notification.title)
            self.speak(notification.message)

            self.speech.set_enabled(False)
            self.settings.set("speech", "enabled", False)
            self.settings.save()

    def back(self):
        self.pop()
