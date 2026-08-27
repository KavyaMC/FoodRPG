import os

from application.services.paths import help_directory


def open_document(filename):
    os.startfile(help_directory() / filename)
