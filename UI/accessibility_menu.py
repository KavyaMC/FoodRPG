from core.base.controls import Button
from core.base.screen import ControlScreen
from core.controllers.accessibility_controller import AccessibilityController


class AccessibilityScreen(ControlScreen):
    def __init__(self, state):
        super().__init__(
            state, title="Accessibility menu", description="Configure accessibility settings"
        )
        self.controller = AccessibilityController(state, self)
        self.add_controls(
            Button("Text to Speech", self.controller.speech),
            Button("Back", self.controller.back),
        )
