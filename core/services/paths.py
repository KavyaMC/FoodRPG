import os
from pathlib import Path


def app_directory():
    path = Path(os.environ["LOCALAPPDATA"]) / "FoodRPG"
    path.mkdir(parents=True, exist_ok=True)
    return path
