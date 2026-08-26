from application.base.controls import (
    Button,
    ComboBox,
)
from application.base.screen import ControlScreen
from application.controllers.settings_controller import (
    SettingsController,
)


class SettingsScreen(ControlScreen):
    SPEECH_BACKENDS = (
        "AUTO",
        "NVDA",
        "JAWS",
        "OneCore",
        "SAPI",
    )

    VERBOSITY_LEVELS = (
        "Low",
        "Normal",
        "High",
    )

    def __init__(self, state):
        super().__init__(
            state,
            title="Settings",
            description="Configure game settings.",
        )

        self.controller = SettingsController(
            state,
            self,
        )

        current_backend = self.settings.get(
            "speech",
            "backend",
        )

        if current_backend not in self.SPEECH_BACKENDS:
            current_backend = "AUTO"

        current_verbosity = self.settings.get(
            "speech",
            "verbosity",
        )

        if current_verbosity not in self.VERBOSITY_LEVELS:
            current_verbosity = "Normal"

        self.speech_backend = ComboBox(
            "Speech Backend",
            self.SPEECH_BACKENDS,
            index=self.SPEECH_BACKENDS.index(current_backend),
            on_changed=(self.controller.backend_changed),
        )

        self.verbosity_control = ComboBox(
            "Speech Verbosity",
            self.VERBOSITY_LEVELS,
            index=self.VERBOSITY_LEVELS.index(current_verbosity),
            on_changed=(self.controller.verbosity_changed),
        )

        self.add_controls(
            self.speech_backend,
            self.verbosity_control,
            Button(
                "Back",
                self.controller.back,
            ),
        )

    def open(self):
        super().open()
