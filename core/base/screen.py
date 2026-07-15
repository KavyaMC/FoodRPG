import pygame

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
        if event.type != pygame.KEYDOWN:
            return

        match event.key:
            case pygame.K_ESCAPE:
                if self.screens.count > 1:
                    self.screens.pop()
                else:
                    self.game.quit()


class ControlScreen(Screen):
    def __init__(self, state, title="", description=""):
        super().__init__(state, title, description)
        self.controls = []
        self.focus_index = 0

    def announce(self):
        if self.current_control:
            self.speak(self.current_control.announce())

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
        if event.type != pygame.KEYDOWN:
            return

        if self.current_control and getattr(self.current_control, "capturing_input", False):
            self.current_control.handle_input(event)
            return

        match event.key:
            case pygame.K_UP:
                self.move_previous()

            case pygame.K_DOWN:
                self.move_next()

            case pygame.K_LEFT:
                if self.current_control:
                    self.current_control.left()

            case pygame.K_RIGHT:
                if self.current_control:
                    self.current_control.right()

            case pygame.K_RETURN | pygame.K_KP_ENTER:
                self.activate_current()

            case _:
                super().handle_input(event)


class TransitionScreen(Screen):
    def __init__(
        self,
        state,
        title="",
        description="",
        on_finish=None,
    ):
        super().__init__(state, title, description)

        self.controller = None
        self.on_finish = on_finish

    def update(self, dt):
        if self.controller:
            self.controller.update(dt)

    def finish(self):
        if self.on_finish:
            self.on_finish()
        else:
            self.screens.pop()
