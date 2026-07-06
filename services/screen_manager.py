class ScreenManager:
    def __init__(self):
        self._stack = []

    @property
    def current(self):
        if not self._stack:
            return None

        return self._stack[-1]

    @property
    def count(self):
        return len(self._stack)

    def push(self, screen):
        self._stack.append(screen)
        screen.open()

    def pop(self):
        if not self._stack:
            return None
        screen = self._stack.pop()
        screen.close()
        if self.current:
            self.current.resume()
        return screen

    def replace(self, screen):
        if self.current:
            self.pop()
        self.push(screen)

    def clear(self):
        while self._stack:
            self.pop()

    def dispatch(self, event):
        if self.current:
            self.current.handle_input(event)

    def update(self):
        if self.current:
            self.current.update()