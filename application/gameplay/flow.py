from application.gameplay.UI.gameplay_screen import GameplayScreen
from application.gameplay.UI.tutorial import TutorialScreen


class Flow:
    def __init__(self, state):
        self.state = state
        self.screens = state.screen_manager

    def enter(self):
        self.screens.clear()

        gameplay = GameplayScreen(
            self.state,
        )

        self.screens.push(gameplay)

        gameplay_state = self.state.gameplay

        if gameplay_state is None:
            raise RuntimeError("Cannot enter gameplay without an active gameplay state.")

        if not gameplay_state.session.tutorial_completed:
            gameplay_state.start_tutorial()

            self.screens.push(
                TutorialScreen(
                    self.state,
                ),
            )
        else:
            gameplay_state.start()
