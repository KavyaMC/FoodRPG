import json
from pathlib import Path

from application.services.paths import gameplay_data_directory


class ContentLoader:
    def __init__(self, data_directory=None):
        self.data_directory = Path(data_directory or gameplay_data_directory())

    def load(self, filename):
        path = self.data_directory / filename

        if not path.is_file():
            raise FileNotFoundError(f"Content file not found: {path}")

        try:
            with path.open(
                "r",
                encoding="utf-8",
            ) as file:
                return json.load(file)

        except json.JSONDecodeError as error:
            raise ValueError(f"Invalid JSON in {filename}: {error}") from error

    def exists(self, filename):
        return (self.data_directory / filename).is_file()

    def get(self, filename, key, default=None):
        data = self.load(filename)
        return data.get(key, default)
