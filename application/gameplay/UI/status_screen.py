from application.base.controls import LabelField
from application.base.screen import ControlScreen


class StatusScreen(ControlScreen):
    def __init__(self, state):
        super().__init__(
            state,
            title="Session",
            description="Current game session",
        )

        session = state.gameplay.session

        self.add_controls(
            LabelField(
                "Date",
                session.date,
            ),
            LabelField(
                "Time",
                session.time,
            ),
            LabelField(
                "Location",
                session.location or "Unknown",
            ),
            LabelField(
                "Objective",
                session.objective or "None",
            ),
            LabelField(
                "Current Task",
                session.current_task or "None",
            ),
        )
