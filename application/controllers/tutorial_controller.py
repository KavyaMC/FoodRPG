from ..base.controller import Controller
from ..base.controls import Button, TextArea
from ..helpers.DataLoader import DataLoader


class TutorialController(Controller):
    TUTORIAL_FILE = "tutorial.json"

    def __init__(self, state):
        super().__init__(state)

        self.page = 0
        self.pages = []

    def open(self):
        data_loader = DataLoader()
        data = data_loader.load(self.TUTORIAL_FILE)

        tutorial = data["tutorial"]

        self.screen.title = tutorial.get("title", "Gameplay Tutorial")
        self.screen.description = tutorial.get(
            "description",
            "Learn the basics of gameplay.",
        )

        self.pages = tutorial.get("pages", [])
        self.page = 0

        self.build_page()
        self.push(self.screen)

    def build_page(self):
        self.screen.clear_controls()

        self.screen.add_control(
            TextArea(self.pages[self.page]),
        )

        self.screen.add_control(
            Button("Next", self.next),
        )

    def next(self):
        if self.page >= len(self.pages) - 1:
            self.complete()
            return

        self.page += 1
        self.build_page()
        self.screen.announce()

    def complete(self):
        self.gameplay.session.tutorial_completed = True
        self.gameplay.resume()
        self.screens.pop()
