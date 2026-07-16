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
            self.speak(f"Slot {slot} already occupied.")
            return

        self.speak(f"Saving to slot {slot}")

    def load(self, slot):
        if not self.save_load.exists(slot):
            self.speak(f"Slot {slot} is empty.")
            return

        self.speak(f"Loading slot {slot}")

    def back(self):
        self.pop()
