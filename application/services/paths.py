import os
from pathlib import Path


def app_directory():
    path = Path(os.environ["LOCALAPPDATA"]) / "FoodRPG"

    path.mkdir(
        parents=True,
        exist_ok=True,
    )

    return path


def slots_directory():
    path = app_directory() / "slots"

    path.mkdir(
        parents=True,
        exist_ok=True,
    )

    return path


def root_directory():
    return Path(__file__).resolve().parents[2]


def data_directory():
    return root_directory() / "application" / "data"


def docs_directory():
    return root_directory() / "docs"


def help_directory():
    return docs_directory() / "player"


def gameplay_data_directory():
    return root_directory() / "application" / "gameplay" / "data"


def settings_file():
    return app_directory() / "settings.ini"
