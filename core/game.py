import pygame

from .gamestate import GameState
from services.speech import Speech


class Game:
    def __init__(self):
        pygame.init()

        self._init_window()
        self._init_services()
        self._init_state()

    def _init_window(self):
        self.name = "Food RPG"
        self.version = "v0.1.0"

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption(f"{self.name} {self.version}")

        self.clock = pygame.time.Clock()

    def _init_services(self):
        self.speech = Speech()

    def _init_state(self):
        self.state = GameState(
            speech=self.speech,
        )

    def run(self):
        while self.state.running:
            self.handle_events()

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

    def quit(self):
        self.state.running = False