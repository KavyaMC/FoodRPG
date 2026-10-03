from ..base.controller import Controller
from ..gameplay.session import Session
from ..models.player import Player


class NewGameController(Controller):
    MENU_FILE = "data/forms.json"

    def __init__(self, state):
        super().__init__(state)

        self.player_name = None
        self.business_name = None
        self.business_category = None

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
        if item["label"] == "Business Category":
            businesses = self.state.content.load(
                "businesses.json",
            )

            item = item.copy()
            item["options"] = businesses

        control = super().create_combo(item)

        if item["label"] == "Business Category":
            self.business_category = control

        return control

    def create_character(self):
        player_defaults = self.state.content.load(
            "player_defaults.json",
        )

        player = Player.new(
            player_name=self.player_name.value,
            business_name=self.business_name.value,
            business_category=self.business_category.value,
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
