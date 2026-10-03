from ..base.controller import Controller
from ..base.controls import TextArea


class SessionController(Controller):
    def __init__(self, state):
        super().__init__(state)

    def open(self):
        session = self.gameplay.session

        text = (
            f"Date: {session.date}\n"
            f"Time: {session.time}\n"
            f"Location: {session.location or 'Unknown'}\n"
            f"Objective: {session.objective or 'None'}\n"
            f"Current Task: {session.current_task or 'None'}"
        )

        self.screen.title = "Session"
        self.screen.description = "Current game session"
        self.screen.clear_controls()
        self.screen.add_control(TextArea(text))
        self.push(self.screen)
