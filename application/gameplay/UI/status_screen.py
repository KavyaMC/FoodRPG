from core.base.controls import LabelField
from core.base.screen import ControlScreen


class SessionScreen(ControlScreen):
    def __init__(self, state):
        super().__init__(
            state,
            title="Session",
            description="Current game session",
        )

        session = state.session

        self.add_controls(
            LabelField(
                "Day",
                str(session.day),
            ),
            LabelField(
                "Time",
                f"{session.hour:02}:{session.minute:02}",
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
