from core import keybindings

from .state_object import StateObject


class Screen(StateObject):
    def __init__(self, state, title="", description=""):
        super().__init__(state)

        self.title = title
        self.description = description

    def identity(self):
        if self.description:
            return f"{self.title}. {self.description}"

        return self.title

    def open(self):
        self.speak(self.identity())

    def resume(self):
        pass

    def update(self, dt):
        pass

    def close(self):
        pass

    def handle_input(self, event):
        if event.type != keybindings.KEYDOWN:
            return

        if event.key in keybindings.BACK_KEYS:
            if self.screens.count > 1:
                self.screens.pop()
            else:
                self.game.quit()


class ControlScreen(Screen):
    def __init__(self, state, title="", description=""):
        super().__init__(
            state,
            title,
            description,
        )

        self.controls = []
        self.focus_index = 0

    def open(self):
        super().open()
        self.announce()

    def resume(self):
        self.announce()

    def announce(self):
        if self.current_control:
            self.current_control.announce_self()

    @property
    def current_control(self):
        if not self.controls:
            return None

        return self.controls[self.focus_index]

    def add_control(self, control):
        control.announce_callback = self.speak
        self.controls.append(control)

    def add_controls(self, *controls):
        for control in controls:
            control.announce_callback = self.speak
            self.controls.append(control)

    def move_next(self):
        if not self.controls:
            return

        self.focus_index = (self.focus_index + 1) % len(self.controls)

        self.announce()

    def move_previous(self):
        if not self.controls:
            return

        self.focus_index = (self.focus_index - 1) % len(self.controls)

        self.announce()

    def activate_current(self):
        if not self.current_control:
            return None

        return self.current_control.activate()

    def handle_input(self, event):
        if event.type != keybindings.KEYDOWN:
            return

        if self.current_control and getattr(
            self.current_control,
            "capturing_input",
            False,
        ):
            self.current_control.handle_input(event)
            return

        if event.key in keybindings.UP:
            self.move_previous()
            return

        if event.key in keybindings.DOWN:
            self.move_next()
            return

        if event.key in keybindings.LEFT:
            if self.current_control:
                self.current_control.left()

            return

        if event.key in keybindings.RIGHT:
            if self.current_control:
                self.current_control.right()

            return

        if event.key in keybindings.ACTIVATE_KEYS:
            self.activate_current()
            return

        super().handle_input(event)
