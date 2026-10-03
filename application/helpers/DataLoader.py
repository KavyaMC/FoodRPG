import json

from application.services.paths import data_directory


class DataLoader:
    def load(self, filename):
        path = data_directory() / filename

        with open(
            path,
            "r",
            encoding="utf-8",
        ) as file:
            return json.load(file)
