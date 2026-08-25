class GameClock:
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24

    def __init__(self, session):
        self.session = session

    def advance(self, minutes):
        if minutes < 0:
            raise ValueError("Minutes cannot be negative.")

        total_minutes = self.session.hour * self.MINUTES_PER_HOUR + self.session.minute + minutes

        day_offset, time_minutes = divmod(
            total_minutes,
            self.HOURS_PER_DAY * self.MINUTES_PER_HOUR,
        )

        self.session.day += day_offset

        self.session.hour, self.session.minute = divmod(
            time_minutes,
            self.MINUTES_PER_HOUR,
        )

    def reset(self):
        self.session.day = 1
        self.session.hour = 6
        self.session.minute = 0
