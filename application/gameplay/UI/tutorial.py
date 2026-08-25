from core.base.screen import InteractionScreen


class TutorialScreen(InteractionScreen):
    def __init__(self, state):
        super().__init__(
            state,
            title="Gameplay Tutorial",
            description=[
                (
                    "Welcome to FoodRPG. "
                    "Congrats on completing Business registration "
                    "and welcome to managing it."
                ),
                (
                    "Your gameplay screen contains the actions "
                    "available to you at your current stage of the game."
                ),
                (
                    "Select an action and press Enter to activate it. "
                    "Use Escape to return to the gameplay screen."
                ),
                (
                    "You can open the Session screen to review "
                    "information about your current game, including "
                    "your business, location, objective, task, "
                    "and in-game time."
                ),
                (
                    "As you play, your business will grow and "
                    "new gameplay systems and actions will become available."
                ),
                ("This concludes the basic gameplay tutorial. Select Next to finish the tutorial."),
            ],
        )

    def next(self):
        if self.description_focus.index >= len(self.description) - 1:
            self.complete()
            return

        self.description_focus.index += 1
        self.announce_focus()

    def complete(self):
        self.state.session.tutorial_completed = True
        self.screens.pop()
