from core.base.controls import Button
from core.base.screen import ControlScreen
from core.controllers.help_controller import HelpController


class HelpScreen(ControlScreen):
    def __init__(self, state):
        super().__init__(state, title="Help menu", description="Learn more about the game")

        self.controller = HelpController(state, self)

        self.add_controls(
            Button("Introduction", self.controller.introduction),
            Button("Getting Started", self.controller.getting_started),
            Button("Keyboard Shortcuts", self.controller.keyboard_shortcuts),
            Button("Accessibility", self.controller.accessibility),
            Button("Installation", self.controller.installation),
            Button("About", self.controller.about),
            Button("Back", self.controller.back),
        )
