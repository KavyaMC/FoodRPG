class Control:
    control_type = "Control"

    def __init__(self, label):
        self.label = label
        self.state = None

        self.enabled = True
        self.focused = False

    def focus(self):
        self.focused = True

    def blur(self):
        self.focused = False

    def announcement(self, verbose=False):
        text = self.label

        if self.state is not None:
            text += f". {self.state}"

        if verbose:
            text += f". {self.control_type}"

        return text

    def activate(self):
        return None

    def handle_input(self, event):
        pass


class Button(Control):
    control_type = "Button"

    def __init__(self, label, action):
        super().__init__(label)

        self.action = action

    def activate(self):
        return self.action
