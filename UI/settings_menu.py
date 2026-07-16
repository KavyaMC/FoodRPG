from core.base.controls import Button
from core.base.screen import ControlScreen
from core.controllers.settings_controller import SettingsController


class SettingsScreen(ControlScreen):
    def __init__(self, state):
        super().__init__(
            state,
            title="Settings menu",
            description="Configure game settings.",
        )

        self.controller = SettingsController(state, self)

        self.add_controls(
            Button("Accessibility", self.controller.accessibility),
            Button("Back", self.controller.back),
        )
