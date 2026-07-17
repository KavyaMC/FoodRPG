from enum import Enum

from ..base.controller import Controller


class SaveSlotMode(Enum):
    SAVE = "save"
    LOAD = "load"


class SaveSlotsController(Controller):
    def __init__(self, state, screen, mode):
        super().__init__(state, screen)
        self.mode = mode

    @property
    def title(self):
        if self.mode == SaveSlotMode.SAVE:
            return "Choose Save Slot"
        return "Load Game"

    def slot_selected(self, slot):
        if self.mode == SaveSlotMode.SAVE:
            self.save(slot)
        else:
            self.load(slot)

    def save(self, slot):
        if self.save_load.exists(slot):
            notification = self.notify.warning(
                "Save Slot Occupied", f"Slot {slot} already contains saved data."
            )
            self.speak(notification.title)
            self.speak(notification.message)
            return

        # TODO: Save game data

        notification = self.notify.success("Game Saved", f"Progress saved to Slot {slot}.")
        self.speak(notification.title)
        self.speak(notification.message)

    def load(self, slot):
        if not self.save_load.exists(slot):
            notification = self.notify.warning(
                "Empty Save Slot", f"Slot {slot} does not contain any saved data."
            )
            self.speak(notification.title)
            self.speak(notification.message)
            return

        # TODO: Load game data

        notification = self.notify.info("Loading Game", f"Loading save from Slot {slot}.")
        self.speak(notification.title)
        self.speak(notification.message)

    def back(self):
        self.pop()
