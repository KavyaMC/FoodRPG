class Screen:
    def __init__(self, state, title="", description=""):
        self.state = state

        self.title = title
        self.description = description

    def identity(self):
        if self.description:
            return f"{self.title}. {self.description}"

        return self.title

    def open(self):
        self.state.speak(self.identity())

    def resume(self):
        pass

    def close(self):
        pass

    def handle_input(self, event):
        pass


class ControlScreen(Screen):
    def __init__(self, state, title="", description=""):
        super().__init__(state, title, description)

        self.controls = []
        self.focus_index = 0

    @property
    def current_control(self):
        if not self.controls:
            return None

        return self.controls[self.focus_index]

    def open(self):
        super().open()
        self.announce()

    def resume(self):
        self.announce()

    def add_control(self, control):
        self.controls.append(control)

    def add_controls(self, *controls):
        self.controls.extend(controls)

    def announce(self):
        if self.current_control:
            self.state.speak(self.current_control.announcement())

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
        pass


class TransitionScreen(Screen):
    def __init__(
        self,
        state,
        title="",
        description="",
        auto_dismiss=False,
        duration=0.0,
        on_finish=None,
    ):
        super().__init__(state, title, description)

        self.auto_dismiss = auto_dismiss
        self.duration = duration
        self.on_finish = on_finish

    def finish(self):
        if self.on_finish:
            self.on_finish()
        else:
            self.state.screen_manager.pop_screen()
