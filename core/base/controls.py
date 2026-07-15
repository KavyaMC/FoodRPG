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

    def announce_self(self):
        if self.announce_callback:
            self.announce_callback(self.announce())

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

        self.options = options
        self.index = index
        self.highlight = index
        self.expanded = False

        self.on_changed = on_changed

    @property
    def capturing_input(self):
        return self.expanded

    @property
    def value(self):
        return self.options[self.index]

    def announce(self):
        if self.expanded:
            return (
                f"{self.label}. "
                f"{self.options[self.highlight]}. "
                f"{self.highlight + 1} of {len(self.options)}."
            )

        return f"{self.label}. {self.value}"

    def activate(self):
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
                self.highlight = (self.highlight - 1) % len(self.options)
                self.announce_self()

            case pygame.K_DOWN:
                self.highlight = (self.highlight + 1) % len(self.options)
                self.announce_self()

            case pygame.K_RETURN | pygame.K_KP_ENTER:
                self.activate()

            case pygame.K_ESCAPE:
                self.expanded = False
                self.announce_self()


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
