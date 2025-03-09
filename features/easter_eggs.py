# features/easter_eggs.py
import re

class EasterEggs:
    """
    Handles discovering and responding to easter eggs in user input.
    Provides fun responses when secret phrases are found.
    """
    
    def __init__(self):
        """Initialize with a dictionary of easter eggs and their responses."""
        # Use more specific phrase patterns to avoid accidental triggers
        self.easter_eggs = {
            r"\bsecret_phrase_1\b": "You found an easter egg! Here's a joke: Why don't programmers like nature? It has too many bugs.",
            r"\bsecret_phrase_2\b": "You found another easter egg! Here's a fun fact: The first computer mouse was made of wood.",
            r"\bkonami_code\b": "⬆️⬆️⬇️⬇️⬅️➡️⬅️➡️🅱️🅰️ START! You unlocked unlimited power! (Not really, but nice reference!)",
            r"\bhello world\b": "The classic first program says hi back!",
            r"\bcoffee[\s]*overflow\b": "Error: Coffee cup stack overflow. Time for a refill!",
            r"\b42\b": "Yes, that is indeed the answer to the ultimate question of life, the universe, and everything.",
            r"\brecursion\b": "Did you mean: recursion? (Google joke easter egg)",
        }
        
        # Track which easter eggs have been found in this session
        self.found_eggs = set()
        
    def check_easter_egg(self, prompt):
        """
        Check if the prompt contains any easter egg phrases.
        
        Args:
            prompt (str): The user input to check for easter eggs
            
        Returns:
            str or None: The easter egg response if found, None otherwise
        """
        if not prompt or not isinstance(prompt, str):
            return None
            
        # Convert to lowercase for case-insensitive matching
        prompt_lower = prompt.lower()
        
        for pattern, response in self.easter_eggs.items():
            if re.search(pattern, prompt_lower):
                # Keep track of found easter eggs
                self.found_eggs.add(pattern)
                return response
                
        return None
        
    def get_found_count(self):
        """
        Get the number of unique easter eggs found.
        
        Returns:
            int: Count of unique easter eggs found
        """
        return len(self.found_eggs)
        
    def get_total_count(self):
        """
        Get the total number of available easter eggs.
        
        Returns:
            int: Total number of easter eggs
        """
        return len(self.easter_eggs)
        
    def reset_found_eggs(self):
        """Reset the collection of found easter eggs."""
        self.found_eggs.clear()
        
    def add_easter_egg(self, pattern, response):
        """
        Add a new easter egg to the collection.
        
        Args:
            pattern (str): Regular expression pattern to match
            response (str): Response when the pattern is found
        """
        self.easter_eggs[pattern] = response
