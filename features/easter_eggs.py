# features/easter_eggs.py
class EasterEggs:
    def __init__(self):
        self.easter_eggs = {
            "secret_phrase_1": "You found an easter egg! Here's a joke: Why don't programmers like nature? It has too many bugs.",
            "secret_phrase_2": "You found another easter egg! Here's a fun fact: The first computer mouse was made of wood.",
            # Add more easter eggs as needed
        }

    def check_easter_egg(self, prompt):
        for phrase, response in self.easter_eggs.items():
            if phrase in prompt:
                return response
        return None