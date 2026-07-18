import pygame


class Control:
    def __init__(self, label, announce=None):
        self.label = label
        self.announce_callback = announce

    @property
    def capturing_input(self):
        return False

    def announce(self):
        return self.label

    def speak(self, text):
        if self.announce_callback:
            self.announce_callback(text)

    def announce_self(self):
        self.speak(self.announce())

    def activate(self):
        pass

    def left(self):
        pass

    def right(self):
        pass

    def handle_input(self, event):
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
        self.index = index if options else 0
        self.highlight = self.index
        self.expanded = False

        self.on_changed = on_changed

    @property
    def capturing_input(self):
        return self.expanded

    @property
    def value(self):
        if not self.options:
            return ""
        return self.options[self.index]

    def set_options(self, options):
        self.options = list(options)
        self.index = 0
        self.highlight = 0
        self.expanded = False
        self.announce_self()

    def set_value(self, value):
        if value not in self.options:
            return

        self.index = self.options.index(value)
        self.highlight = self.index

        if self.on_changed:
            self.on_changed(self.value)

        self.announce_self()

    def announce(self):
        if not self.options:
            return f"{self.label}. No options available."

        if self.expanded:
            return (
                f"{self.label}. "
                f"Selecting. "
                f"{self.options[self.highlight]}. "
                f"{self.highlight + 1} of {len(self.options)}."
            )

        return f"{self.label}. {self.value}"

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

        if self.on_changed:
            self.on_changed(self.value)

        self.expanded = False
        self.announce_self()

    def handle_input(self, event):
        if event.type != pygame.KEYDOWN:
            return

        match event.key:
            case pygame.K_UP:
                if self.options:
                    self.highlight = (self.highlight - 1) % len(self.options)
                    self.speak(self.options[self.highlight])

            case pygame.K_DOWN:
                if self.options:
                    self.highlight = (self.highlight + 1) % len(self.options)
                    self.speak(self.options[self.highlight])

            case pygame.K_HOME:
                if self.options:
                    self.highlight = 0
                    self.speak(self.options[self.highlight])

            case pygame.K_END:
                if self.options:
                    self.highlight = len(self.options) - 1
                    self.speak(self.options[self.highlight])

            case pygame.K_RETURN | pygame.K_KP_ENTER:
                self.activate()

            case pygame.K_ESCAPE:
                self.expanded = False
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

        self.speak(self.value[self.cursor])

    def activate(self):
        if not self.editing:
            self.original_value = self.value
            self.cursor = len(self.value)
            self.editing = True
            self.speak(f"Editing {self.label}.")
            self.speak(self.value if self.value else self.placeholder)
            return

        self.editing = False

        if self.on_changed:
            self.on_changed(self.value)

        self.announce_self()

    def insert(self, character):
        if len(self.value) >= self.max_length:
            self.speak("Maximum length reached.")
            return

        self.value = self.value[: self.cursor] + character + self.value[self.cursor :]

        self.cursor += len(character)

        self.speak(character)

    def backspace(self):
        if self.cursor == 0:
            self.speak("Beginning of text.")
            return

        deleted = self.value[self.cursor - 1]

        self.value = self.value[: self.cursor - 1] + self.value[self.cursor :]

        self.cursor -= 1

        self.speak(f"Deleted {deleted}")

    def delete(self):
        if self.cursor >= len(self.value):
            self.speak("End of text.")
            return

        deleted = self.value[self.cursor]

        self.value = self.value[: self.cursor] + self.value[self.cursor + 1 :]

        self.speak(f"Deleted {deleted}")

    def left(self):
        if self.cursor > 0:
            self.cursor -= 1

        self.announce_cursor()

    def right(self):
        if self.cursor < len(self.value):
            self.cursor += 1

        self.announce_cursor()

    def home(self):
        self.cursor = 0
        self.speak("Beginning of text.")

    def end(self):
        self.cursor = len(self.value)
        self.speak("End of text.")

    def handle_input(self, event):
        if event.type != pygame.KEYDOWN:
            return

        match event.key:
            case pygame.K_RETURN | pygame.K_KP_ENTER:
                self.activate()

            case pygame.K_ESCAPE:
                self.value = self.original_value
                self.cursor = len(self.value)
                self.editing = False
                self.speak("Changes discarded.")
                self.announce_self()

            case pygame.K_BACKSPACE:
                self.backspace()

            case pygame.K_DELETE:
                self.delete()

            case pygame.K_LEFT:
                self.left()

            case pygame.K_RIGHT:
                self.right()

            case pygame.K_HOME:
                self.home()

            case pygame.K_END:
                self.end()

            case _:
                if event.unicode and event.unicode.isprintable():
                    self.insert(event.unicode)


class LabelField(Control):
    def __init__(
        self,
        label,
        value="",
        announce=None,
    ):
        super().__init__(label, announce)
        self.value = value

    def announce(self):
        return f"{self.label}. {self.value}"

    def set_value(self, value):
        self.value = value

    def activate(self):
        self.announce_self()
