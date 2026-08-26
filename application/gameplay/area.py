from dataclasses import dataclass, field


@dataclass(slots=True)
class Area:
    id: str
    name: str
    description: str = ""

    activities: list = field(
        default_factory=list,
    )

    def add_activity(self, activity):
        self.activities.append(activity)

    def get_activity(self, activity_id):
        for activity in self.activities:
            if activity.id == activity_id:
                return activity

        return None

    def available_activities(self, state):
        return [activity for activity in self.activities if activity.can_execute(state)]
