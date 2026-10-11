from ..base.controller import Controller


class SettingsController(Controller):
    def __init__(self, state):
        super().__init__(state)

        self.pending_settings = {}

    def open(self):
        menu = self.get_menu("settings_menu")

        self.pending_settings = {
            "backend": self.speech.mode,
            "verbosity": self.speech.verbosity,
            "volume": self.speech.volume,
            "rate": self.speech.rate,
        }

        menu = dict(menu)
        menu["items"] = [
            self._prepare_item(item)
            for item in menu.get(
                "items",
                [],
            )
        ]

        self.load_menu(menu)
        self.push(self.screen)

    def _prepare_item(self, item):
        item = dict(item)

        match item.get("label"):
            case "Speech Backend":
                item["value"] = self.pending_settings["backend"]

            case "Speech Verbosity":
                item["value"] = self.pending_settings["verbosity"]

            case "Speech Volume":
                item["value"] = self.pending_settings["volume"]

            case "Speech Rate":
                item["value"] = self.pending_settings["rate"]

        return item

    def backend_changed(self, backend):
        self.pending_settings["backend"] = backend
        self.speech.set_mode(backend)

    def verbosity_changed(self, verbosity):
        self.pending_settings["verbosity"] = verbosity
        self.speech.set_verbosity(verbosity)

    def volume_changed(self, volume):
        self.pending_settings["volume"] = volume
        self.speech.set_volume(volume)

    def rate_changed(self, rate):
        self.pending_settings["rate"] = rate
        self.speech.set_rate(rate)

    def reset_settings(self):
        self.pending_settings = {
            "backend": self.speech.DEFAULT_BACKEND,
            "verbosity": self.speech.DEFAULT_VERBOSITY,
            "volume": self.speech.DEFAULT_VOLUME,
            "rate": self.speech.DEFAULT_RATE,
        }

        self.speech.set_mode(
            self.pending_settings["backend"],
        )

        self.speech.set_verbosity(
            self.pending_settings["verbosity"],
        )

        self.speech.set_volume(
            self.pending_settings["volume"],
        )

        self.speech.set_rate(
            self.pending_settings["rate"],
        )

        self._refresh_controls()

        self.speak("Settings set to defaults.")

    def _refresh_controls(self):
        for control in self.screen.controls:
            match control.label:
                case "Speech Backend":
                    control.index = control.options.index(
                        self.pending_settings["backend"],
                    )
                    control.highlight = control.index

                case "Speech Verbosity":
                    control.index = control.options.index(
                        self.pending_settings["verbosity"],
                    )
                    control.highlight = control.index

                case "Speech Volume":
                    control.value = self.pending_settings["volume"]

                case "Speech Rate":
                    control.value = self.pending_settings["rate"]

    def back(self):
        self.settings.set(
            "speech",
            "backend",
            self.pending_settings["backend"],
        )

        self.settings.set(
            "speech",
            "verbosity",
            self.pending_settings["verbosity"],
        )

        self.settings.set(
            "speech",
            "volume",
            self.pending_settings["volume"],
        )

        self.settings.set(
            "speech",
            "rate",
            self.pending_settings["rate"],
        )

        self.settings.save()

        self.pop()
