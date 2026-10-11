from prism import Context


class Speech:
    BACKENDS = {
        "AUTO": "Automatic",
        "NVDA": "NVDA",
        "JAWS": "JAWS",
        "OneCore": "OneCore",
        "SAPI": "SAPI",
        "Orca": "Orca",
        "Speech Dispatcher": "Speech Dispatcher",
    }

    VERBOSITY_LEVELS = (
        "LOW",
        "NORMAL",
        "HIGH",
    )

    DEFAULT_BACKEND = "AUTO"
    DEFAULT_VERBOSITY = "NORMAL"
    DEFAULT_VOLUME = 1.0
    DEFAULT_RATE = 0.5

    def __init__(
        self,
        mode=DEFAULT_BACKEND,
        verbosity=DEFAULT_VERBOSITY,
        volume=DEFAULT_VOLUME,
        rate=DEFAULT_RATE,
    ):
        self.mode = mode
        self.verbosity = verbosity
        self.volume = round(float(volume), 2)
        self.rate = round(float(rate), 2)

        self.ctx = Context()
        self.engine = self._create_engine(self.mode)

        self._apply_settings()

    def _find_backend_id(self, backend_name):
        try:
            for i in range(self.ctx.backends_count):
                backend_id = self.ctx.id_of(i)

                if (
                    self.ctx.name_of(
                        backend_id,
                    ).lower()
                    == backend_name.lower()
                ):
                    return backend_id

        except Exception as error:
            print(
                "Speech backend lookup error:",
                error,
            )

        return None

    def _create_engine(self, mode):
        try:
            if mode != "AUTO":
                backend_id = self._find_backend_id(mode)

                if backend_id is not None:
                    return self.ctx.create(
                        backend_id,
                    )

            return self.ctx.create_best()

        except Exception as error:
            print(
                "Speech engine creation error:",
                error,
            )

        try:
            sapi_id = self._find_backend_id("SAPI")

            if sapi_id is not None:
                return self.ctx.create(
                    sapi_id,
                )

        except Exception as error:
            print(
                "Speech SAPI fallback error:",
                error,
            )

        return self.ctx.create_best()

    def _apply_settings(self):
        self._apply_volume()
        self._apply_rate()

    def _apply_volume(self):
        try:
            if self.supports_volume:
                self.engine.volume = self.volume

        except Exception as error:
            print(
                "Speech volume error:",
                error,
            )

    def _apply_rate(self):
        try:
            if self.supports_rate:
                self.engine.rate = self.rate

        except Exception as error:
            print(
                "Speech rate error:",
                error,
            )

    @property
    def supports_volume(self):
        return self.engine.features.supports_set_volume

    @property
    def supports_rate(self):
        return self.engine.features.supports_set_rate

    def get_available_backends(self):
        backends = ["AUTO"]

        try:
            for i in range(
                self.ctx.backends_count,
            ):
                backend_id = self.ctx.id_of(i)
                name = self.ctx.name_of(
                    backend_id,
                )

                if name in self.BACKENDS and name not in backends:
                    backends.append(name)

        except Exception as error:
            print(
                "Speech backend list error:",
                error,
            )

        return backends

    def set_mode(self, mode):
        if mode not in self.BACKENDS:
            raise ValueError(
                f"Invalid speech backend: {mode}",
            )

        self.mode = mode
        self.engine = self._create_engine(mode)

        self._apply_settings()

    def set_verbosity(self, verbosity):
        if verbosity not in self.VERBOSITY_LEVELS:
            raise ValueError(
                f"Invalid verbosity: {verbosity}",
            )

        self.verbosity = verbosity

    def set_volume(self, volume):
        try:
            volume = round(
                float(volume),
                2,
            )

        except TypeError, ValueError:
            raise ValueError(
                "Speech volume must be a number.",
            ) from None

        self.volume = volume

        if not self.supports_volume:
            return False

        try:
            self.engine.volume = volume

        except Exception as error:
            print(
                "Speech volume error:",
                error,
            )
            return False

        return True

    def set_rate(self, rate):
        try:
            rate = round(
                float(rate),
                2,
            )

        except TypeError, ValueError:
            raise ValueError(
                "Speech rate must be a number.",
            ) from None

        self.rate = rate

        if not self.supports_rate:
            return False

        try:
            self.engine.rate = rate

        except Exception as error:
            print(
                "Speech rate error:",
                error,
            )
            return False

        return True

    def announce(
        self,
        label,
        control_type=None,
        instruction=None,
    ):
        match self.verbosity:
            case "LOW":
                text = label

            case "NORMAL":
                text = label

                if control_type:
                    text += f" {control_type}"

            case "HIGH":
                text = label

                if control_type:
                    text += f" {control_type}"

                if instruction:
                    text += f". {instruction}"

            case _:
                text = label

        self.speak(text)

    @property
    def speaking(self):
        try:
            return self.engine.speaking

        except Exception:
            return None

    def speak(
        self,
        text,
        interrupt=False,
        on_complete=None,
    ):
        try:
            if interrupt and hasattr(
                self.engine,
                "stop",
            ):
                self.engine.stop()

            self.engine.output(text)

            if on_complete:
                on_complete()

        except Exception:
            try:
                sapi_id = self._find_backend_id(
                    "SAPI",
                )

                if sapi_id is not None:
                    fallback = self.ctx.create(
                        sapi_id,
                    )

                    if fallback.features.supports_set_volume:
                        fallback.volume = self.volume

                    if fallback.features.supports_set_rate:
                        fallback.rate = self.rate

                    fallback.output(text)

                    if on_complete:
                        on_complete()

            except Exception as error:
                print(
                    "Speech fallback error:",
                    error,
                )
