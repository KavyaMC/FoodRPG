from core.base.controls import Button
from core.base.screen import ControlScreen


class SaveSlotsScreen(ControlScreen):
    SLOT_COUNT = 4

    def __init__(self, state, controller):
        super().__init__(state)

        self.controller = controller
        self.title = controller.title

        self._build()

    def _build(self):
        for slot in range(1, self.SLOT_COUNT + 1):
            self.add_controls(
                Button(
                    self.controller.slot_label(slot),
                    lambda s=slot: self.controller.slot_selected(s),
                )
            )
