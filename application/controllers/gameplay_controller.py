from ..base.controller import Controller
from .options_controller import OptionsController
from .session_controller import SessionController
from .tutorial_controller import TutorialController


class GameplayController(Controller):
    def __init__(self, state):
        super().__init__(state)

    def open(self):
        self.screens.clear()

        if self.gameplay is None:
            raise RuntimeError(
                "Cannot enter gameplay without an active gameplay state.",
            )

        data = self.get_menu("gameplay_menu")

        business_type = self.gameplay.session.player.business_type

        business_options = data.get(
            "business_options",
            {},
        ).get(
            business_type,
            [],
        )

        generic_options = data.get(
            "generic_options",
            [],
        )

        menu = {
            "title": data.get(
                "title",
                "Gameplay",
            ),
            "description": data.get(
                "description",
                "Welcome to the game.",
            ),
            "items": business_options + generic_options,
        }

        self.add_menu(
            "gameplay",
            menu,
        )

        self.open_menu("gameplay")
        self.push(self.screen)

        if not self.gameplay.session.tutorial_completed:
            self.gameplay.start_tutorial()

            controller = TutorialController(
                self.state,
            )

            controller.open()
            return

        self.gameplay.start()

    def kitchen(self):
        self.speak(
            "Kitchen is not implemented yet.",
        )

    def details(self):
        controller = SessionController(
            self.state,
        )

        controller.open()

    def options(self):
        self.gameplay.pause()

        controller = OptionsController(
            self.state,
        )

        controller.open()
