from configparser import ConfigParser

from .paths import settings_file


class Settings:
    def __init__(self):
        self.path = settings_file()
        self.config = ConfigParser()

        if self.path.exists():
            self.config.read(self.path)

        self._create_defaults()
        self.save()

    def _create_defaults(self):
        if not self.config.has_section("speech"):
            self.config.add_section("speech")

        if not self.config.has_option("speech", "backend"):
            self.config.set("speech", "backend", "AUTO")

        if not self.config.has_option("speech", "enabled"):
            self.config.set("speech", "enabled", "true")

    def load(self):
        if self.path.exists():
            self.config.read(self.path)
        else:
            self._create_defaults()
            self.save()

    def save(self):
        with self.path.open("w", encoding="utf-8") as file:
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

        self.save()
