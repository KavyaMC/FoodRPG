class GameClock:
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

    def __init__(
        self,
        session,
        start_day=None,
        start_hour=None,
        start_minute=None,
    ):
        self.session = session

        self.start_day = session.day if start_day is None else start_day

        self.start_hour = session.hour if start_hour is None else start_hour

        self.start_minute = session.minute if start_minute is None else start_minute

    def advance(self, minutes):
        if minutes < 0:
            raise ValueError("Minutes cannot be negative.")

        total_minutes = self.session.hour * self.MINUTES_PER_HOUR + self.session.minute + minutes

        day_offset, time_minutes = divmod(
            total_minutes,
            self.MINUTES_PER_DAY,
        )

        self.session.day += day_offset

        (
            self.session.hour,
            self.session.minute,
        ) = divmod(
            time_minutes,
            self.MINUTES_PER_HOUR,
        )

    def reset(self):
        self.session.day = self.start_day
        self.session.hour = self.start_hour
        self.session.minute = self.start_minute
