import pygame

from application.controllers.main_menu_controller import (
    MainMenuController,
)

from .gamestate import GameState


class Game:
    def __init__(self):
        pygame.init()

        self._init_window()
        self._init_state()

        controller = MainMenuController(self.state)
        controller.open()

    def _init_window(self):
        self.name = "Food RPG"
        self.version = "v0.2.0"

        self.screen = pygame.display.set_mode(
            (800, 600),
        )

        pygame.display.set_caption(
            f"{self.name} {self.version}",
        )

        self.clock = pygame.time.Clock()

    def _init_state(self):
        self.state = GameState(self)

    def run(self):
        while self.state.running:
            self.clock.tick(60)
            self.handle_events()
            pygame.display.flip()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
                return

            self.state.screen_manager.dispatch(event)

    def return_to_main_menu(self):
        self.state.screen_manager.clear()

        controller = MainMenuController(self.state)
        controller.open()

    def quit(self):
        self.state.running = False
