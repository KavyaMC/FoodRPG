from enum import Enum

from core.models.gameplay_session import Session
from UI.gameplay_menu import GameplayScreen

from ..base.controller import Controller


class SaveSlotMode(Enum):
    SAVE = "save"
    LOAD = "load"


class SaveSlotsController(Controller):
    def __init__(self, state, screen, mode):
        super().__init__(state, screen)

        self.mode = mode
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

        session = Session.from_dict(data)

        return f"Slot {slot}: {session.player_name} - {session.business_name}"

    def enter_gameplay(self):
        gameplay_screen = GameplayScreen(self.state)

        self.screens.clear()
        self.screens.push(gameplay_screen)

    def save(self, slot):
        if self.save_load.exists(slot):
            if self.pending_overwrite != slot:
                self.pending_overwrite = slot

                notification = self.notify.warning(
                    "Save Slot Occupied",
                    (f"Press Enter again to overwrite Slot {slot}. Press Escape to cancel."),
                )

                self.speak(notification.title)
                self.speak(notification.message)
                return

        self.pending_overwrite = None

        self.save_load.save(
            slot,
            self.session.to_dict(),
        )

        notification = self.notify.success(
            "Game Saved",
            f"Progress saved to Slot {slot}.",
        )

        self.speak(notification.title)
        self.speak(notification.message)
        self.enter_gameplay()

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

        session = Session.from_dict(data)
        self.state.session = session

        notification = self.notify.success(
            "Game Loaded",
            f"Welcome back {session.player_name}.",
        )

        self.speak(notification.title)
        self.speak(notification.message)
        self.enter_gameplay()

    def back(self):
        self.pop()
