from application.base.screen import InteractionScreen


class TutorialScreen(InteractionScreen):
    def __init__(self, state):
        super().__init__(
            state,
            title="Gameplay Tutorial",
            description=[
                (
                    "Welcome to FoodRPG. "
                    "Business registration is complete. "
                    "You can now begin managing your business."
                ),
                (
                    "The gameplay screen contains the actions "
                    "available at your current stage of the game."
                ),
                (
                    "Select an action and press Enter to activate it. "
                    "Press Escape to return to the gameplay screen."
                ),
                (
                    "Select Session to review information about "
                    "your current game, including your business, "
                    "location, objective, current task, and "
                    "in-game time."
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
        self.state.gameplay.session.tutorial_completed = True
        self.state.gameplay.resume()
        self.screens.pop()
