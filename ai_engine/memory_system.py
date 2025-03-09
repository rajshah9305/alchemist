# ai_engine/memory_system.py
import json
import os
import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class MemorySystem:
    """System for storing and retrieving conversation memory in a JSON file."""
    
    def __init__(self, db_path=None):
        """
        Initialize the memory system with the path to the memory database.
        
        Args:
            db_path: Path to the JSON file for storing memory. If None, uses default path.
        """
        if db_path is None:
            # Use a default path relative to this file
            self.db_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), 
                'memory.json'
            )
        else:
            self.db_path = db_path
            
        # Directory where the db file will be stored
        self.db_dir = os.path.dirname(self.db_path)
        
        # Create directory if it doesn't exist
        if not os.path.exists(self.db_dir) and self.db_dir:
            try:
                os.makedirs(self.db_dir, exist_ok=True)
            except Exception as e:
                logger.error(f"Error creating memory directory {self.db_dir}: {str(e)}")
        
        # Initialize memory
        self.memory = []
        self.load_memory()

    def load_memory(self) -> None:
        """Load memory from the JSON file."""
        try:
            if os.path.exists(self.db_path):
                with open(self.db_path, 'r') as f:
                    self.memory = json.load(f)
                logger.info(f"Loaded {len(self.memory)} interactions from memory")
            else:
                self.memory = []
                logger.info(f"No memory file found at {self.db_path}, initialized empty memory")
        except Exception as e:
            logger.error(f"Error loading memory from {self.db_path}: {str(e)}")
            self.memory = []

    def save_memory(self) -> None:
        """Save memory to the JSON file."""
        try:
            with open(self.db_path, 'w') as f:
                json.dump(self.memory, f, indent=2)
            logger.info(f"Saved {len(self.memory)} interactions to memory")
        except Exception as e:
            logger.error(f"Error saving memory to {self.db_path}: {str(e)}")

    def add_interaction(self, interaction: Dict[str, Any]) -> None:
        """
        Add an interaction to memory and save.
        
        Args:
            interaction: Dictionary containing interaction data
        """
        self.memory.append(interaction)
        self.save_memory()

    def get_memory(self) -> List[Dict[str, Any]]:
        """
        Get all stored interactions.
        
        Returns:
            List of interaction dictionaries
        """
        return self.memory

    def clear_memory(self) -> None:
        """Clear all stored interactions and save."""
        self.memory = []
        self.save_memory()
