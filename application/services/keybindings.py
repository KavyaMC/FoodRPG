import pygame


class KeyBindings:
    def __init__(self):
        self.up_keys = (pygame.K_UP,)
        self.down_keys = (pygame.K_DOWN,)
        self.left_keys = (pygame.K_LEFT,)
        self.right_keys = (pygame.K_RIGHT,)
        self.activate_keys = (pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_SPACE)
        self.back_keys = (pygame.K_ESCAPE,)

    def is_keydown(self, event):
        return event.type == pygame.KEYDOWN

    def get_action(self, event):
        if event.key in self.up_keys:
            return "UP"

        if event.key in self.down_keys:
            return "DOWN"

        if event.key in self.left_keys:
            return "LEFT"

        if event.key in self.right_keys:
            return "RIGHT"

        if event.key in self.activate_keys:
            return "ACTIVATE"

        if event.key in self.back_keys:
            return "BACK"

        return None
