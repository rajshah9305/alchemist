# backend/mock_ai_engine.py
"""
Mock implementation of the AI engine components for development and testing.
This file is used when the actual ai_engine package is not available.
"""
import json
import os
import logging
from datetime import datetime
from typing import Dict, Any, List

logger = logging.getLogger(__name__)

class AIModel:
    """Mock AI model for development and testing."""
    
    def __init__(self, model_path="mock_model"):
        self.model_path = model_path
        self.name = "MockCodestralModel"
        logger.info(f"Initialized mock AI model: {self.name}")
        
    def generate_response(self, prompt: str, personality: Dict[str, Any]) -> str:
        """Generate a mock response based on the prompt and personality."""
        system_message = personality.get("system_message", "Standard mode")
        
        # Generate a response based on the personality mode
        if "Normal Mode" in system_message:
            return f"[Normal Mode] Here's a helpful response to your question about: {prompt}"
        elif "Dark Magic Mode" in system_message:
            return f"[Dark Magic] Behold, mortal! The answer to '{prompt}' lies within your grasp!"
        else:
            return f"I've processed your request about '{prompt}' and here's my response."

def load_codestral_model() -> AIModel:
    """Load and return a mock instance of the AI model."""
    logger.info("Loading mock AI model...")
    return AIModel()

class MemorySystem:
    """Mock memory system for development and testing."""
    
    def __init__(self, db_path=None):
        self.memory = []
        logger.info("Initialized mock memory system")
        
    def add_interaction(self, interaction: Dict[str, Any]) -> None:
        """Add an interaction to memory."""
        self.memory.append(interaction)
        logger.debug(f"Added interaction to mock memory, now {len(self.memory)} items")
        
    def get_memory(self) -> List[Dict[str, Any]]:
        """Get all stored interactions."""
        return self.memory
        
    def clear_memory(self) -> None:
        """Clear all stored interactions."""
        self.memory = []
        logger.debug("Cleared mock memory")

class PersonalityManager:
    """Mock personality manager for development and testing."""
    
    def __init__(self, config_path=None):
        self.config = {
            'normal_mode': {
                'greeting': "Hello! I'm the mock Alchemist, your coding assistant.",
                'system_message': "You are in Normal Mode (MOCK). I'm here to help you with your coding needs."
            },
            'dark_magic_mode': {
                'greeting': "Greetings, mortal. I am the mock Alchemist.",
                'system_message': "You are in Dark Magic Mode (MOCK). Expect the unexpected."
            }
        }
        logger.info("Initialized mock personality manager")
    
    def get_current_personality(self) -> Dict[str, Any]:
        """Get the current personality based on time of day."""
        current_hour = datetime.now().hour
        
        if 6 <= current_hour < 18:
            return self.config['normal_mode']
        else:
            return self.config['dark_magic_mode']
