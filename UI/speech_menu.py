from core.base.controls import Button, ComboBox, Toggle
from core.base.screen import ControlScreen
from core.controllers.speech_controller import SpeechController


class SpeechScreen(ControlScreen):
    def __init__(self, state):
        super().__init__(
            state,
            title="Text to Speech",
            description="Configure text to speech settings.",
        )

        self.controller = SpeechController(state, self)

        self.add_controls(
            ComboBox(
                "Speech Backend",
                options=self.speech.get_available_backends(),
                index=0,
                on_changed=self.controller.backend_changed,
                announce=self.speak,
            ),
            Toggle(
                "Enabled",
                value=self.speech.enabled,
                on_changed=self.controller.enabled_changed,
                announce=self.speak,
            ),
            Button(
                "Back",
                self.controller.back,
            ),
        )
