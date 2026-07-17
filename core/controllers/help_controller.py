from core.base.controller import Controller
from core.helpers.document_helper import open_document


class HelpController(Controller):
    def introduction(self):
        open_document("introduction.md")

    def getting_started(self):
        open_document("getting_started.md")

    def keyboard_shortcuts(self):
        open_document("keyboard_shortcuts.md")

    def accessibility(self):
        open_document("accessibility.md")

    def installation(self):
        open_document("installation.md")

    def about(self):
        open_document("about.md")

    def back(self):
        self.pop()
