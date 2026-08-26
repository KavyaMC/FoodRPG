from application.gameplay.session import Session
from application.player.info import Player

from ..base.controller import Controller


class NewGameController(Controller):
    def __init__(self, state, screen):
        super().__init__(
            state,
            screen,
        )

    def create_character(self):
        player_defaults = self.state.content.load(
            "player_defaults.json",
        )

        player = Player.new(
            player_name=self.screen.player_name.value,
            business_name=self.screen.business_name.value,
            business_category=self.screen.business_category.value,
            defaults=player_defaults,
        )

        try:
            player.validate()

        except ValueError as error:
            notification = self.notify.error(
                "Character Creation Failed",
                str(error),
            )

            self.speak(notification.title)
            self.speak(notification.message)
            return

        slot = getattr(
            self.state,
            "new_game_slot",
            None,
        )

        if slot is None:
            notification = self.notify.error(
                "Save Failed",
                "No save slot was selected.",
            )

            self.speak(notification.title)
            self.speak(notification.message)
            return

        defaults = self.state.content.load(
            "defaults.json",
        )

        session = Session.new(
            player,
            defaults,
        )

        self.save_load.save(
            slot,
            session.to_dict(),
        )

        self.state.start_gameplay(
            session,
        )

        notification = self.notify.success(
            "Game Created",
            f"Game saved to Slot {slot}. Starting gameplay.",
        )

        self.speak(notification.title)
        self.speak(notification.message)

        self.state.gameplay_flow.enter()

    def cancel(self):
        self.pop()
