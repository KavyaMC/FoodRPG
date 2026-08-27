from application import keybindings

from .controls import Button
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

        return self.controls[self.focus.index]

    def add_control(self, control):
        control.announce_callback = self.speak
        control.verbosity_callback = lambda: self.verbosity
        self.controls.append(control)

    def add_controls(self, *controls):
        for control in controls:
            control.announce_callback = self.speak
            control.verbosity_callback = lambda: self.verbosity
            self.controls.append(control)

    def move_next(self):
        if not self.controls:
            return

        self.focus.index = (self.focus.index + 1) % len(self.controls)

        self.announce()

    def move_previous(self):
        if not self.controls:
            return

        self.focus.index = (self.focus.index - 1) % len(self.controls)

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


class InteractionScreen(ControlScreen):
    def __init__(
        self,
        state,
        title,
        description,
    ):
        super().__init__(
            state,
            title=title,
            description=title,
        )

        self.description = description
        self.description_focus = Focus()

        self.add_controls(
            Button(
                "Previous",
                self.previous,
            ),
            Button(
                "Next",
                self.next,
            ),
        )

    def identity(self):
        return self.title

    @property
    def current_description(self):
        return self.description[self.description_focus.index]

    def open(self):
        super().open()
        self.announce_focus()

    def announce_focus(self):
        self.speak(self.current_description)

    def next(self):
        if self.description_focus.index >= len(self.description) - 1:
            self.speak("End of content.")
            return

        self.description_focus.index += 1
        self.announce_focus()

    def previous(self):
        if self.description_focus.index <= 0:
            self.speak("Beginning of content.")
            return

        self.description_focus.index -= 1
        self.announce_focus()
