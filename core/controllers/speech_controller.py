from ..base.controller import Controller


class SpeechController(Controller):
    def __init__(self, state, screen):
        super().__init__(state, screen)

    def backend_changed(self, backend):
        self.speech.set_mode(backend)
        self.settings.set("speech", "backend", backend)
        self.settings.save()

    def enabled_changed(self, enabled):
        self.speech.set_enabled(enabled)
        self.settings.set("speech", "enabled", enabled)
        self.settings.save()

    def back(self):
        self.pop()
