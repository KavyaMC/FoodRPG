from core.base.controls import Button
from core.base.screen import ControlScreen
from core.controllers.resume_controller import ResumeController


class ResumeScreen(ControlScreen):
    def __init__(self, state):
        super().__init__(
            state,
            title="Game Paused",
            description="Choose an option",
        )

        self.controller = ResumeController(
            state,
            self,
        )

        self.add_controls(
            Button(
                "Back",
                self.controller.back,
            ),
            Button(
                "Save",
                self.controller.save,
            ),
            Button(
                "Settings",
                self.controller.settings,
            ),
            Button(
                "Return to Main Menu",
                self.controller.return_to_menu,
            ),
            Button(
                "Quit",
                self.controller.quit,
            ),
        )
