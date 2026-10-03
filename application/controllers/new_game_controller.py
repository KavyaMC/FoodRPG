from ..base.controller import Controller
from ..controllers.gameplay_controller import GameplayController
from ..gameplay.session import Session
from ..models.player import Player


class NewGameController(Controller):
    MENU_FILE = "forms.json"

    def __init__(self, state):
        super().__init__(state)

        self.player_name = None
        self.business_name = None
        self.business_type = None

    def open(self):
        form = self.get_menu("new_game")

        self.load_menu(form)
        self.push(self.screen)

    def create_text_field(self, item):
        control = super().create_text_field(item)

        match item["label"]:
            case "Player Name":
                self.player_name = control

            case "Business Name":
                self.business_name = control

        return control

    def create_combo(self, item):
        if item["label"] == "Business Type":
            businesses = self.data_loader.load(
                "businesses.json",
            )

            item = item.copy()
            item["options"] = businesses

        control = super().create_combo(item)

        if item["label"] == "Business Type":
            self.business_type = control

        return control

    def create_game(self):
        player_defaults = self.data_loader.load(
            "player_defaults.json",
        )

        player = Player.new(
            player_name=self.player_name.value,
            business_name=self.business_name.value,
            business_type=self.business_type.value,
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

        defaults = self.data_loader.load(
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

        controller = GameplayController(
            self.state,
        )

        controller.open()

    def cancel(self):
        self.pop()
