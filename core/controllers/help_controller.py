from core.base.controller import Controller
from core.helpers.document_helper import open_help


class HelpController(Controller):
    def introduction(self):
        open_help("introduction.md")

    def getting_started(self):
        open_help("getting_started.md")

    def keyboard_shortcuts(self):
        open_help("keyboard_shortcuts.md")

    def accessibility(self):
        open_help("accessibility.md")

    def installation(self):
        open_help("installation.md")

    def about(self):
        open_help("about.md")

    def back(self):
        self.pop()
