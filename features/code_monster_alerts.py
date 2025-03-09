# features/code_monster_alerts.py
class CodeMonsterAlerts:
    """
    Provides fun, monster-themed alerts for different code errors.
    Each error type corresponds to a specific coding monster.
    """
    
    def __init__(self):
        """Initialize with a collection of code monsters and their alert messages."""
        self.monsters = {
            # Syntax errors
            "SyntaxError": "Syntaxor",
            "IndentationError": "Indentasaur",
            "TabError": "Tabogre",
            
            # Runtime errors
            "TypeError": "Typezilla",
            "ValueError": "Valueviper",
            "IndexError": "Indexling",
            "KeyError": "Keytroll",
            "AttributeError": "Attributank",
            "NameError": "Namewalker",
            "ZeroDivisionError": "Zerothrok",
            
            # Logic errors (these would need to be detected by your code)
            "InfiniteLoop": "Loopfiend",
            "MemoryLeak": "Memorax",
            "Cryptic": "Cryptovore",
        }
        
        self.monster_descriptions = {
            "Syntaxor": "A punctuation-obsessed beast that feeds on misplaced semicolons and brackets.",
            "Indentasaur": "A prehistoric creature that gets enraged by inconsistent indentation.",
            "Tabogre": "A grumpy monster that mixes tabs and spaces with malicious intent.",
            "Typezilla": "A giant lizard that breathes fire when types don't match.",
            "Valueviper": "A sneaky snake that replaces your expected values with nonsense.",
            "Indexling": "A tiny imp that moves array indices just out of reach.",
            "Keytroll": "A troll that hides dictionary keys under bridges of code.",
            "Attributank": "A heavily armored beast that blocks access to object attributes.",
            "Namewalker": "An undead variable that wasn't properly defined before use.",
            "Zerothrok": "A cosmic horror that creates black holes by dividing by zero.",
            "Loopfiend": "A demon that traps coders in endless loops of frustration.",
            "Memorax": "A ghostly entity that consumes memory until none remains.",
            "Cryptovore": "A shadowy creature that obscures error messages and logs."
        }

    def get_monster_for_error(self, error_type):
        """
        Get the monster associated with a specific error type.
        
        Args:
            error_type (str): The Python error type or custom error category
            
        Returns:
            str: The name of the associated monster
        """
        return self.monsters.get(error_type, "Unknown")
        
    def get_monster_alert(self, error_type):
        """
        Get a fun alert message for the specified error type.
        
        Args:
            error_type (str): The Python error type or custom error category
            
        Returns:
            str: A monster-themed alert message
        """
        monster = self.get_monster_for_error(error_type)
        
        if monster == "Unknown":
            return "Unknown error detected! A mysterious monster is nearby."
            
        description = self.monster_descriptions.get(monster, "")
        return f"{error_type} detected! The {monster} is nearby. {description}"
    
    def get_all_monsters(self):
        """
        Get a list of all monsters and their descriptions.
        
        Returns:
            dict: A dictionary mapping monster names to their descriptions
        """
        return self.monster_descriptions
