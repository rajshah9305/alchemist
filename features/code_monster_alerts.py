import logging
from typing import Optional

class CodeMonsterAlerts:
    def __init__(self):
        self.monsters = {
            "Syntaxor": "Syntax error detected! The Syntaxor is nearby.",
            "Cryptovore": "Cryptic error detected! The Cryptovore is nearby.",
            "Loopfiend": "Infinite loop detected! The Loopfiend is nearby.",
            "Nullbyte": "NullPointerException detected! The Nullbyte is nearby.",
            "Recursion": "Stack overflow detected! The Recursion monster is nearby.",
            "MemoryHog": "Memory leak detected! The MemoryHog is nearby.",
        }
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def get_monster_alert(self, error_type: str) -> str:
        """
        Get a monster alert message for a given error type.
        
        Args:
            error_type: The type of error encountered
            
        Returns:
            str: The corresponding monster alert message
        """
        if not isinstance(error_type, str):
            raise TypeError("error_type must be a string")
            
        error_type = error_type.strip()
        message = self.monsters.get(error_type)
        
        if message:
            self.logger.info(f"Monster alert triggered: {error_type}")
            return message
        else:
            self.logger.warning(f"Unknown error type encountered: {error_type}")
            return "Unknown error detected! A mysterious monster is nearby."
    
    def add_monster(self, monster_name: str, message: str) -> None:
        """Add a new monster to the alert system"""
        if not monster_name or not message:
            raise ValueError("Both monster_name and message must be provided")
        self.monsters[monster_name] = message
        self.logger.info(f"New monster added: {monster_name}")
