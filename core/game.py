import pygame

from UI.main_menu import MainMenuScreen

from .gamestate import GameState


class Game:
    def __init__(self):
        pygame.init()

        self._init_window()
        self._init_state()
        self.state.screen_manager.push(MainMenuScreen(self.state))

    def _init_window(self):
        self.name = "Food RPG"
        self.version = "v0.1.0"

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption(f"{self.name} {self.version}")

        self.clock = pygame.time.Clock()

    def _init_state(self):
        self.state = GameState(self)

    def run(self):
        while self.state.running:
            self.clock.tick(30)
            self.handle_events()
            pygame.display.flip()
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
                return
            self.state.screen_manager.dispatch(event)

    def quit(self):
        self.state.running = False
