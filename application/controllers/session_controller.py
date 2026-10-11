from ..base.controller import Controller
from ..base.controls import TextArea


class SessionController(Controller):
    def __init__(self, state):
        super().__init__(state)

    def open(self):
        session = self.gameplay.session

        self.screen.title = "Session"
        self.screen.description = "Current game session"
        self.screen.clear_controls()

        text_areas = [
            TextArea(
                f"Player: {session.player_name}",
            ),
            TextArea(
                f"Business: {session.business_name}",
            ),
            TextArea(
                f"Business Type: {session.business_type}",
            ),
            TextArea(
                f"Date: {session.date}",
            ),
            TextArea(
                f"Time: {session.time}",
            ),
            TextArea(
                f"Location: {session.location or 'Unknown'}",
            ),
            TextArea(
                f"Objective: {session.objective or 'None'}",
            ),
            TextArea(
                f"Current Task: {session.current_task or 'None'}",
            ),
            TextArea(
                f"Current Activity: {session.current_activity or 'None'}",
            ),
        ]

        self.screen.add_controls(
            *text_areas,
        )

        self.push(self.screen)
