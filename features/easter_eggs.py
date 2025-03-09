import re
from typing import Optional, Dict
import logging

class EasterEggs:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.easter_eggs: Dict[str, str] = {
            "secret_phrase_1": "You found an easter egg! Here's a joke: Why don't programmers like nature? It has too many bugs.",
            "secret_phrase_2": "You found another easter egg! Here's a fun fact: The first computer mouse was made of wood.",
            "alchemist": "Congratulations! You've discovered the Alchemist's secret laboratory!",
            "code_wizard": "A wild Code Wizard appears! They offer you wisdom: 'Clean code is readable code.'",
            "debug_dance": "You've unlocked the legendary Debug Dance! It's super effective against bugs!"
        }
        # Compile regex patterns for efficient matching
        self.patterns = {
            phrase: re.compile(re.escape(phrase), re.IGNORECASE) 
            for phrase in self.easter_eggs.keys()
        }

    def check_easter_egg(self, prompt: str) -> Optional[str]:
        """
        Check if the prompt contains any easter eggs.
        
        Args:
            prompt: The input text to check for easter eggs
            
        Returns:
            Optional[str]: The easter egg message if found, None otherwise
        """
        if not isinstance(prompt, str):
            raise TypeError("Prompt must be a string")
            
        if not prompt.strip():
            return None
            
        for phrase, pattern in self.patterns.items():
            if pattern.search(prompt):
                self.logger.info(f"Easter egg found: {phrase}")
                return self.easter_eggs[phrase]
        return None

    def add_easter_egg(self, phrase: str, response: str) -> None:
        """Add a new easter egg to the collection"""
        if not phrase or not response:
            raise ValueError("Both phrase and response must be provided")
        self.easter_eggs[phrase] = response
        self.patterns[phrase] = re.compile(re.escape(phrase), re.IGNORECASE)
        self.logger.info(f"New easter egg added for phrase: {phrase}")
