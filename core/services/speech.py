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

    def __init__(self, mode="AUTO", enabled=True):
        self.mode = mode
        self.enabled = enabled

        self.ctx = Context()
        self.engine = self._create_engine(self.mode)

    def _find_backend_id(self, backend_name):
        try:
            for i in range(self.ctx.backends_count):
                backend_id = self.ctx.id_of(i)

                if self.ctx.name_of(backend_id).lower() == backend_name.lower():
                    return backend_id

        except Exception as e:
            print("Speech backend lookup error:", e)

        return None

    def _create_engine(self, mode):
        try:
            if mode != "AUTO":
                backend_id = self._find_backend_id(mode)

                if backend_id is not None:
                    return self.ctx.create(backend_id)

            return self.ctx.create_best()

        except Exception as e:
            print("Speech engine creation error:", e)

        try:
            sapi_id = self._find_backend_id("SAPI")

            if sapi_id is not None:
                return self.ctx.create(sapi_id)

        except Exception as e:
            print("Speech SAPI fallback error:", e)

        return self.ctx.create_best()

    def get_available_backends(self):
        backends = ["AUTO"]

        try:
            for i in range(self.ctx.backends_count):
                backend_id = self.ctx.id_of(i)
                name = self.ctx.name_of(backend_id)

                if name in self.BACKENDS and name not in backends:
                    backends.append(name)

        except Exception as e:
            print("Speech backend list error:", e)

        return backends

    def set_mode(self, mode):
        self.mode = mode
        self.engine = self._create_engine(mode)

    def set_enabled(self, enabled):
        self.enabled = enabled

    @property
    def speaking(self):
        try:
            return self.engine.speaking

        except Exception:
            return None

    def speak(self, text, interrupt=False, on_complete=None):
        if not self.enabled:
            if on_complete:
                on_complete()
            return

        try:
            if interrupt and hasattr(self.engine, "stop"):
                self.engine.stop()

            self.engine.output(text)

            if on_complete:
                on_complete()

        except Exception:
            try:
                sapi_id = self._find_backend_id("SAPI")

                if sapi_id is not None:
                    fallback = self.ctx.create(sapi_id)
                    fallback.output(text)

                    if on_complete:
                        on_complete()

            except Exception as e:
                print("Speech fallback error:", e)
