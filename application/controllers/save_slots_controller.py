from collections.abc import Callable
from enum import Enum

from application.base.controls import Button
from application.gameplay.session import Session

from ..base.controller import Controller


class SaveSlotMode(Enum):
    SAVE = "save"
    LOAD = "load"


class SaveSlotsController(Controller):
    SLOT_COUNT = 4

    def __init__(self, state, mode):
        super().__init__(state)

        self.mode = mode
        self.pending_overwrite = None

        self.on_saved: Callable[[int], None] | None = None
        self.on_loaded: Callable[[Session], None] | None = None
        self.on_slot_selected: Callable[[int], None] | None = None

    @property
    def title(self):
        if self.mode == SaveSlotMode.SAVE:
            return "Choose Save Slot"

        return "Load Game"

    def open(self):
        self.screen.title = self.title
        self.screen.description = "Choose a save slot."

        self.build_slots()

        self.push(self.screen)

    def build_slots(self):
        self.screen.clear_controls()

        for slot in range(
            1,
            self.SLOT_COUNT + 1,
        ):
            self.screen.add_control(
                Button(
                    self.slot_label(slot),
                    lambda s=slot: self.slot_selected(s),
                )
            )

    def slot_selected(self, slot):
        if self.mode == SaveSlotMode.SAVE:
            self.save(slot)
            return

        self.load(slot)

    def slot_label(self, slot):
        if not self.save_load.exists(slot):
            return f"Slot {slot} (Empty)"

        data = self.save_load.load(slot)

        if not data:
            return f"Slot {slot} (Empty)"

        session = Session.from_dict(data)

        return f"Slot {slot}: {session.player.player_name} - {session.player.business_name}"

    def save(self, slot):
        if self.on_slot_selected:
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
            self.on_slot_selected(slot)
            return

        if not self.state.gameplay:
            notification = self.notify.error(
                "Save Failed",
                "There is no active game session to save.",
            )

            self.speak(notification.title)
            self.speak(notification.message)

            return

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
            self.state.gameplay.session.to_dict(),
        )

        notification = self.notify.success(
            "Game Saved",
            f"Progress saved to Slot {slot}.",
        )

        self.speak(notification.title)
        self.speak(notification.message)

        if self.on_saved:
            self.on_saved(slot)
            return

        self.pop()

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

        if not data:
            notification = self.notify.warning(
                "Empty Save Slot",
                f"Slot {slot} does not contain any saved data.",
            )

            self.speak(notification.title)
            self.speak(notification.message)

            return

        session = Session.from_dict(data)

        self.state.start_gameplay(session)

        notification = self.notify.success(
            "Game Loaded",
            f"Welcome back {session.player.player_name}.",
        )

        self.speak(notification.title)
        self.speak(notification.message)

        if self.on_loaded:
            self.on_loaded(session)
            return

        self.pop()

    def back(self):
        self.pending_overwrite = None
        self.pop()
