from enum import Enum

from core.models.player import Player

from ..base.controller import Controller


class SaveSlotMode(Enum):
    SAVE = "save"
    LOAD = "load"


class SaveSlotsController(Controller):
    def __init__(self, state, screen, mode, player=None):
        super().__init__(state, screen)
        self.mode = mode
        self.player = player
        self.pending_overwrite = None

    @property
    def title(self):
        return "Choose Save Slot" if self.mode == SaveSlotMode.SAVE else "Load Game"

    def slot_selected(self, slot):
        if self.mode == SaveSlotMode.SAVE:
            self.save(slot)
        else:
            self.load(slot)

    def slot_label(self, slot):
        if not self.save_load.exists(slot):
            return f"Slot {slot} (Empty)"

        data = self.save_load.load(slot)

        if not data:
            return f"Slot {slot} (Empty)"

        player = Player.from_dict(data)

        return f"Slot {slot}: {player.player_name} - {player.business_name}"

    def save(self, slot):
        if self.save_load.exists(slot):
            if self.pending_overwrite != slot:
                self.pending_overwrite = slot

                notification = self.notify.warning(
                    "Save Slot Occupied",
                    f"Press Enter again to overwrite Slot {slot}. Press Escape to cancel.",
                )

                self.speak(notification.title)
                self.speak(notification.message)
                return

        self.pending_overwrite = None

        self.player.validate()

        self.save_load.save(
            slot,
            self.player.to_dict(),
        )

        notification = self.notify.success(
            "Game Saved",
            f"Progress saved to Slot {slot}.",
        )

        self.speak(notification.title)
        self.speak(notification.message)

        # to do
        # push this to gameplay
        # destroy all screen and handle control to gameplay

    def load(self, slot):
        if not self.save_load.exists(slot):
            notification = self.notify.warning(
                "Empty Save Slot",
                f"Slot {slot} does not contain any saved data.",
            )

            self.speak(notification.title)
            self.speak(notification.message)
            return

        data = self.save_load.load(slot)

        self.state.player = self.player = Player.from_dict(data)

        notification = self.notify.success(
            "Game Loaded",
            f"Welcome back {self.player.player_name}.",
        )

        self.speak(notification.title)
        self.speak(notification.message)

        self.pop()

    def back(self):
        self.pop()
