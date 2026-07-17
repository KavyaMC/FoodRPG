import os

from core.services.paths import help_directory


def open_help(filename):
    os.startfile(help_directory() / filename)
