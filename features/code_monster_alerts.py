# features/code_monster_alerts.py
class CodeMonsterAlerts:
    def __init__(self):
        self.monsters = {
            "Syntaxor": "Syntax error detected! The Syntaxor is nearby.",
            "Cryptovore": "Cryptic error detected! The Cryptovore is nearby.",
            # Add more monsters as needed
        }

    def get_monster_alert(self, error_type):
        return self.monsters.get(error_type, "Unknown error detected! A mysterious monster is nearby.")