import pygame


class KeyBindings:
    @staticmethod
    def is_next_panel(event):
        return (
            event.type == pygame.KEYDOWN
            and event.key == pygame.K_F6
            and not (event.mod & pygame.KMOD_RSHIFT)
        )

    @staticmethod
    def is_previous_panel(event):
        return (
            event.type == pygame.KEYDOWN
            and event.key == pygame.K_F6
            and (event.mod & pygame.KMOD_RSHIFT)
        )
