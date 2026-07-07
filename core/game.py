import pygame
from UI.splash_screen import SplashScreen

from .gamestate import GameState


class Game:
    def __init__(self):
        pygame.init()

        self._init_window()
        self._init_state()
        self.starting_up = True
        self.startup_elapsed = 0
        self.startup_duration = 3000
        self.startup()

    def _init_window(self):
        self.name = "Food RPG"
        self.version = "v0.1.0"

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption(f"{self.name} {self.version}")

        self.clock = pygame.time.Clock()

    def _init_state(self):
        self.state = GameState()

    def startup(self):
        self.state.screen_manager.push(SplashScreen(self.state))

    def update_startup(self, dt):
        self.startup_elapsed += dt

        if self.startup_elapsed >= self.startup_duration:
            self.finish_startup()

    def finish_startup(self):
        self.starting_up = False

        self.state.speak("Startup complete.")

    def run(self):
        while self.state.running:
            dt = self.clock.tick(30)
            self.handle_events()
            if self.starting_up:
                self.update_startup(dt)
            else:
                self.state.screen_manager.update(dt)
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
