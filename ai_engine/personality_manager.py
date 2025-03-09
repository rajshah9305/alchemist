# ai_engine/personality_manager.py
import yaml
import os
import logging
from datetime import datetime
from typing import Dict, Any

logger = logging.getLogger(__name__)

class PersonalityManager:
    """Manager for AI personality settings based on configuration file."""
    
    def __init__(self, config_path=None):
        """
        Initialize the personality manager with the path to the config file.
        
        Args:
            config_path: Path to the YAML configuration file. If None, uses default path.
        """
        # Default personality in case config loading fails
        self.default_personality = {
            'greeting': "Hello! I'm Alchemist, your friendly coding assistant.",
            'system_message': "I'm here to help you with your coding needs."
        }
        
        if config_path is None:
            # Use a default path relative to this file
            self.config_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), 
                'personality_config.yaml'
            )
        else:
            self.config_path = config_path
            
        self.config = {
            'normal_mode': self.default_personality,
            'dark_magic_mode': self.default_personality
        }
        
        self.load_config()

    def load_config(self) -> None:
        """Load personality configuration from YAML file."""
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path, 'r') as f:
                    loaded_config = yaml.safe_load(f)
                    
                # Validate and update config
                if isinstance(loaded_config, dict):
                    # Make sure required modes exist
                    if 'normal_mode' not in loaded_config:
                        loaded_config['normal_mode'] = self.default_personality
                    if 'dark_magic_mode' not in loaded_config:
                        loaded_config['dark_magic_mode'] = self.default_personality
                        
                    self.config = loaded_config
                    logger.info(f"Loaded personality config from {self.config_path}")
            else:
                logger.warning(f"Config file not found at {self.config_path}, using default personalities")
        except Exception as e:
            logger.error(f"Error loading personality config from {self.config_path}: {str(e)}")
            # Keep the default config

    def get_current_personality(self) -> Dict[str, Any]:
        """
        Get the current personality based on time of day.
        
        Returns:
            Dictionary containing personality configuration
        """
        try:
            current_hour = datetime.now().hour
            
            # Use normal mode during day (6am-6pm), dark magic mode at night
            if 6 <= current_hour < 18:
                logger.debug(f"Using normal_mode personality (current hour: {current_hour})")
                return self.config['normal_mode']
            else:
                logger.debug(f"Using dark_magic_mode personality (current hour: {current_hour})")
                return self.config['dark_magic_mode']
        except Exception as e:
            logger.error(f"Error determining personality: {str(e)}")
            return self.default_personality

    def set_personality_mode(self, mode: str) -> bool:
        """
        Manually set the personality mode regardless of time.
        
        Args:
            mode: The mode to set ('normal_mode' or 'dark_magic_mode')
            
        Returns:
            Success status
        """
        if mode in self.config:
            self.current_mode = mode
            return True
        return False
