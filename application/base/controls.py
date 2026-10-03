class Control:
    def __init__(self, label, announce=None):
        self.label = label
        self.announce_callback = announce
        self.verbosity_callback = None

    @property
    def capturing_input(self):
        return False

    @property
    def verbosity(self):
        if self.verbosity_callback:
            return self.verbosity_callback()
        return "NORMAL"

    def announce(self):
        return self.label

    def speak(self, text):
        if self.announce_callback:
            self.announce_callback(text)

    def announce_self(self):
        self.speak(self.announce())

    def activate(self):
        pass

    def previous(self):
        pass

    def next(self):
        pass


class Button(Control):
    def __init__(self, label, action, announce=None):
        super().__init__(label, announce)
        self.action = action

    def activate(self):
        return self.action()


class Toggle(Control):
    def __init__(
        self,
        label,
        value=False,
        on_changed=None,
        announce=None,
    ):
        super().__init__(label, announce)
        self.value = value
        self.on_changed = on_changed

    def announce(self):
        state = "On" if self.value else "Off"
        return f"{self.label}. {state}"

    def toggle(self):
        self.value = not self.value

        if self.on_changed:
            self.on_changed(self.value)

        self.announce_self()

    def activate(self):
        self.toggle()


class ComboBox(Control):
    def __init__(
        self,
        label,
        options,
        index=0,
        on_changed=None,
        announce=None,
    ):
        super().__init__(label, announce)
        self.options = list(options)
        self.on_changed = on_changed

        if self.options:
            self.index = min(max(index, 0), len(self.options) - 1)
        else:
            self.index = 0

        self.highlight = self.index
        self.expanded = False

    @property
    def capturing_input(self):
        return self.expanded

    @property
    def value(self):
        if not self.options:
            return ""

        return self.options[self.index]

    def announce(self):
        if not self.options:
            return self.label

        if self.expanded:
            return (
                f"{self.label}. "
                f"Selecting. "
                f"{self.options[self.highlight]}. "
                f"{self.highlight + 1} of "
                f"{len(self.options)}."
            )

        return f"{self.label}. {self.value}"

    def set_options(self, options):
        self.options = list(options)
        self.index = 0
        self.highlight = 0
        self.expanded = False

        if self.options:
            if self.on_changed:
                self.on_changed(self.value)

            self.announce_self()

    def set_value(self, value):
        if value not in self.options:
            return

        self.index = self.options.index(value)
        self.highlight = self.index

        if self.on_changed:
            self.on_changed(self.value)

        self.announce_self()

    def activate(self):
        if not self.options:
            self.announce_self()
            return

        if not self.expanded:
            self.expanded = True
            self.highlight = self.index
            self.announce_self()
            return

        self.index = self.highlight
        self.expanded = False

        if self.on_changed:
            self.on_changed(self.value)

        self.announce_self()

    def previous(self):
        if not self.expanded:
            return

        self._move_highlight(-1)

    def next(self):
        if not self.expanded:
            return

        self._move_highlight(1)

    def _move_highlight(self, direction):
        if not self.options:
            return

        self.highlight = (self.highlight + direction) % len(self.options)

        self.speak(self.options[self.highlight])


class Slider(Control):
    def __init__(
        self,
        label,
        value=0,
        minimum=0,
        maximum=100,
        step=1,
        on_changed=None,
        announce=None,
    ):
        super().__init__(label, announce)

        if minimum > maximum:
            raise ValueError(
                "Slider minimum cannot be greater than maximum.",
            )

        if step <= 0:
            raise ValueError(
                "Slider step must be greater than zero.",
            )

        self.minimum = minimum
        self.maximum = maximum
        self.step = step
        self.on_changed = on_changed

        self.value = self._normalize(value)

    def _normalize(self, value):
        value = float(value)

        value = min(
            max(
                value,
                self.minimum,
            ),
            self.maximum,
        )

        return round(
            value,
            2,
        )

    def _set_value(self, value):
        value = self._normalize(value)

        if value == self.value:
            self.announce_self()
            return

        self.value = value

        if self.on_changed:
            self.on_changed(self.value)

        self.announce_self()

    def set_value(self, value):
        self.value = self._normalize(value)
        self.announce_self()

    def announce(self):
        value = f"{self.value:.2f}".rstrip("0").rstrip(".")

        return f"{self.label}. {value}"

    def previous(self):
        self._set_value(
            self.value - self.step,
        )

    def next(self):
        self._set_value(
            self.value + self.step,
        )

    def activate(self):
        self.announce_self()


class TextField(Control):
    def __init__(
        self,
        label,
        value="",
        placeholder="",
        max_length=64,
        on_changed=None,
        announce=None,
    ):
        super().__init__(label, announce)

        self.value = value
        self.placeholder = placeholder
        self.max_length = max_length
        self.on_changed = on_changed

        self.cursor = len(value)
        self.editing = False
        self.original_value = value

    @property
    def capturing_input(self):
        return self.editing

    def announce(self):
        text = self.value if self.value else self.placeholder

        if self.editing:
            return f"{self.label}. Editing. {text}"

        return f"{self.label}. {text}"

    def announce_cursor(self):
        if not self.value:
            self.speak("Blank.")
            return

        if self.cursor == 0:
            self.speak("Beginning of text.")
            return

        if self.cursor >= len(self.value):
            self.speak("End of text.")
            return

        character = self.value[self.cursor]

        if character == " ":
            self.speak("Space.")
        else:
            self.speak(character)

    def activate(self):
        if not self.editing:
            self.original_value = self.value
            self.cursor = len(self.value)
            self.editing = True

            self.speak(
                f"Editing {self.label}.",
            )

            if self.value:
                self.speak(self.value)
            else:
                self.speak("Blank.")

            return

        self.editing = False

        if self.on_changed:
            self.on_changed(self.value)

        self.announce_self()

    def cancel(self):
        if not self.editing:
            return

        self.value = self.original_value
        self.cursor = len(self.value)
        self.editing = False

        self.speak("Editing cancelled.")
        self.announce_self()

    def insert(self, character):
        if len(self.value) >= self.max_length:
            self.speak(
                "Maximum length reached.",
            )
            return

        self.value = self.value[: self.cursor] + character + self.value[self.cursor :]

        self.cursor += 1

        if character == " ":
            self.speak("Space.")
        else:
            self.speak(character)

    def backspace(self):
        if self.cursor == 0:
            self.speak(
                "Beginning of text.",
            )
            return

        deleted = self.value[self.cursor - 1]

        self.value = self.value[: self.cursor - 1] + self.value[self.cursor :]

        self.cursor -= 1

        if deleted == " ":
            self.speak(
                "Space deleted.",
            )
        else:
            self.speak(
                f"Character {deleted} deleted.",
            )

    def delete(self):
        if self.cursor >= len(self.value):
            self.speak(
                "End of text.",
            )
            return

        deleted = self.value[self.cursor]

        self.value = self.value[: self.cursor] + self.value[self.cursor + 1 :]

        if deleted == " ":
            self.speak(
                "Space deleted.",
            )
        else:
            self.speak(
                f"Character {deleted} deleted.",
            )

    def previous(self):
        if self.cursor > 0:
            self.cursor -= 1

        self.announce_cursor()

    def next(self):
        if self.cursor < len(self.value):
            self.cursor += 1

        self.announce_cursor()

    def home(self):
        self.cursor = 0
        self.announce_cursor()

    def end(self):
        self.cursor = len(self.value)
        self.announce_cursor()


class TextArea(Control):
    def __init__(self, text, announce=None):
        super().__init__("", announce)

        if isinstance(text, str):
            self.text = [text]
        else:
            self.text = list(text)

        self.index = 0

    def announce(self):
        if not self.text:
            return ""

        return self.text[self.index]

    def previous(self):
        if not self.text:
            return False

        if self.index <= 0:
            self.speak("Beginning of content.")
            return False

        self.index -= 1
        self.announce_self()
        return True

    def next(self):
        if not self.text:
            return False

        if self.index >= len(self.text) - 1:
            self.speak("End of content.")
            return False

        self.index += 1
        self.announce_self()
        return True

    def activate(self):
        self.announce_self()
