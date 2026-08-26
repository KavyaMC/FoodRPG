from application.base.controller import Controller
from application.gameplay.UI.options import OptionsScreen
from application.gameplay.UI.status_screen import StatusScreen


class GameplayController(Controller):
    def __init__(self, state, screen):
        super().__init__(
            state,
            screen,
        )

    @property
    def area(self):
        return self.gameplay.area

    def options(self):
        self.state.gameplay.pause()

        self.push(
            OptionsScreen(
                self.state,
            ),
        )

    def session(self):
        self.push(
            StatusScreen(
                self.state,
            ),
        )

    def notifications(self):
        self.speak("Not implemented yet. Work in progress. system coming soon")

    def achievements(self):
        self.speak("Not implemented yet. Work in progress. system coming soon")

    def business(self):
        self.speak("Not implemented yet. Work in progress. system coming soon")
