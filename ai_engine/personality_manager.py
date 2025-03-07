# ai_engine/personality_manager.py
import yaml
import os
from datetime import datetime

class PersonalityManager:
    def __init__(self, config_path='personality_config.yaml'):
        self.config_path = config_path
        self.load_config()

    def load_config(self):
        with open(self.config_path, 'r') as f:
            self.config = yaml.safe_load(f)

    def get_current_personality(self):
        current_hour = datetime.now().hour
        if 6 <= current_hour < 18:
            return self.config['normal_mode']
        else:
            return self.config['dark_magic_mode']