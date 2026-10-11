import os

from application.base.controls import Button
from application.services.paths import help_directory

from ..base.controller import Controller


class HelpController(Controller):
    def __init__(self, state):
        super().__init__(state)

    def open(self):
        menu = self.get_menu("help_menu")
        self.load_menu(menu)
        self.push(self.screen)

    def create_button(self, item):
        if item.get("action") == "open_document":
            filename = item["file"]
            return Button(
                item["label"],
                lambda: self.open_document(filename),
            )

        return super().create_button(item)

    def open_document(self, filename):
        os.startfile(help_directory() / filename)

    def back(self):
        self.pop()
