class MenuManager:
    def __init__(self, controller):
        self.controller = controller
        self.menus = {}
        self.stack = []

    @property
    def current(self):
        if not self.stack:
            return None

        return self.stack[-1]

    def add_menu(self, name, menu):
        self.menus[name] = menu

    def open(self, name):
        if name not in self.menus:
            raise ValueError(f"Menu '{name}' does not exist.")

        self.stack.append(name)
        self.load_current()

    def back(self):
        if len(self.stack) <= 1:
            return False

        self.stack.pop()
        self.load_current()
        return True

    def load_current(self):
        menu = self.menus[self.current]

        self.controller.load_menu(menu)
