from core.models.gameplay_session import Session
from core.models.player import Player
from UI.gameplay_menu import GameplayScreen

from ..base.controller import Controller


class NewGameController(Controller):
    def __init__(self, state, screen):
        super().__init__(state, screen)

    def create_character(self):
        player = Player(
            player_name=self.screen.player_name.value,
            business_name=self.screen.business_name.value,
            business_category=(self.screen.business_category.value),
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

        session = Session(
            player=player,
        )

        self.state.session = session

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

        self.save_load.save(
            slot,
            session.to_dict(),
        )

        notification = self.notify.success(
            "Game Created",
            (f"Game saved to Slot {slot}. Starting gameplay."),
        )

        self.speak(notification.title)
        self.speak(notification.message)

        self.enter_gameplay()

    def enter_gameplay(self):
        gameplay = GameplayScreen(
            self.state,
        )

        self.screens.clear()
        self.screens.push(gameplay)

    def cancel(self):
        self.pop()
