from .state_object import StateObject


class Focus:
    def __init__(self):
        self.index = 0


class Screen(StateObject):
    def __init__(self, state, title="", description=""):
        super().__init__(state)

        self.title = title
        self.description = description

        self.focus = Focus()
        self.controls = []
        self.controller = None

    @property
    def current_control(self):
        if not self.controls:
            return None

        return self.controls[self.focus.index]

    def identity(self):
        if self.description:
            return f"{self.title}. {self.description}"

        return self.title

    def open(self):
        self.speak(self.identity())
        self.announce()

    def resume(self):
        self.announce()

    def update(self, dt):
        pass

    def close(self):
        pass

    def handle_input(self, event):
        if not self.keybindings.is_keydown(event):
            return

        action = self.keybindings.get_action(event)
        control = self.current_control

        if control and control.capturing_input:
            match action:
                case "LEFT":
                    control.previous()

                case "RIGHT":
                    control.next()

                case "HOME":
                    if hasattr(control, "home"):
                        control.home()

                case "END":
                    if hasattr(control, "end"):
                        control.end()

                case "ACTIVATE":
                    control.activate()

                case "BACK":
                    if hasattr(control, "cancel"):
                        control.cancel()

                case "BACKSPACE":
                    if hasattr(control, "backspace"):
                        control.backspace()

                case "DELETE":
                    if hasattr(control, "delete"):
                        control.delete()

                case "TEXT":
                    if hasattr(control, "insert"):
                        control.insert(event.unicode)

            return

        match action:
            case "UP":
                self.previous_control()

            case "DOWN":
                self.next_control()

            case "LEFT":
                if control:
                    control.previous()

            case "RIGHT":
                if control:
                    control.next()

            case "ACTIVATE":
                self.activate_current()

            case "BACK":
                if self.controller:
                    self.controller.back()

    def announce(self):
        if self.current_control:
            self.current_control.announce_self()

    def add_control(self, control):
        control.announce_callback = self.speak
        control.verbosity_callback = lambda: self.verbosity

        self.controls.append(control)

    def add_controls(self, *controls):
        for control in controls:
            self.add_control(control)

    def clear_controls(self):
        self.controls.clear()
        self.focus.index = 0

    def next_control(self):
        if not self.controls:
            return

        self.focus.index = (self.focus.index + 1) % len(self.controls)

        self.announce()

    def previous_control(self):
        if not self.controls:
            return

        self.focus.index = (self.focus.index - 1) % len(self.controls)

        self.announce()

    def activate_current(self):
        if self.current_control:
            self.current_control.activate()

    def go_back(self):
        if self.screens.count > 1:
            self.screens.pop()
        else:
            self.game.quit()
