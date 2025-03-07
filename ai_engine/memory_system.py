# ai_engine/memory_system.py
import json
import os

class MemorySystem:
    def __init__(self, db_path='memory.json'):
        self.db_path = db_path
        self.load_memory()

    def load_memory(self):
        if os.path.exists(self.db_path):
            with open(self.db_path, 'r') as f:
                self.memory = json.load(f)
        else:
            self.memory = []

    def save_memory(self):
        with open(self.db_path, 'w') as f:
            json.dump(self.memory, f)

    def add_interaction(self, interaction):
        self.memory.append(interaction)
        self.save_memory()

    def get_memory(self):
        return self.memory

    def clear_memory(self):
        self.memory = []
        self.save_memory()