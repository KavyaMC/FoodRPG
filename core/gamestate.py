from services.speech import Speech

class GameState:
    def __init__(self, speech):
        self.running = True
        self.speech = Speech(mode="AUTO", enabled=True)

    def speak(self, text, interrupt=False):
        self.speech.speak(text, interrupt)