from configparser import ConfigParser

from .paths import app_directory


class Settings:
    def __init__(self):
        self.config = ConfigParser()
        self.path = app_directory() / "settings.ini"
        self.load()

    def _create_defaults(self):
        self.config["speech"] = {
            "backend": "AUTO",
            "enabled": "true",
        }
        self.save()

    def load(self):
        if self.path.exists():
            self.config.read(self.path)
        else:
            self._create_defaults()

    def save(self):
        with self.path.open("w") as file:
            self.config.write(file)

    def get(self, section, option, default=""):
        return self.config.get(
            section,
            option,
            fallback=str(default),
        )

    def getboolean(self, section, option, default=False):
        return self.config.getboolean(
            section,
            option,
            fallback=default,
        )

    def getint(self, section, option, default=0):
        return self.config.getint(
            section,
            option,
            fallback=default,
        )

    def getfloat(self, section, option, default=0.0):
        return self.config.getfloat(
            section,
            option,
            fallback=default,
        )

    def set(self, section, option, value):
        if not self.config.has_section(section):
            self.config.add_section(section)

        self.config.set(
            section,
            option,
            str(value),
        )
