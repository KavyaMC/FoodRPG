import json

from .paths import slots_directory


class SaveLoad:
    SLOT_COUNT = 4

    def __init__(self):
        self.directory = slots_directory()
        self._create_slots()

    def _create_slots(self):
        for slot in range(1, self.SLOT_COUNT + 1):
            path = self._slot_path(slot)
            if not path.exists():
                with path.open("w", encoding="utf-8") as file:
                    json.dump({}, file, indent=4)

    def _slot_path(self, slot):
        if slot < 1 or slot > self.SLOT_COUNT:
            raise ValueError(f"Invalid slot: {slot}")
        return self.directory / f"slot_{slot}.json"

    def exists(self, slot):
        data = self.load(slot)
        return bool(data)

    def save(self, slot, data):
        with self._slot_path(slot).open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def load(self, slot):
        with self._slot_path(slot).open("r", encoding="utf-8") as file:
            return json.load(file)

    def delete(self, slot):
        self.save(slot, {})
