# features/__init__.py
"""
Features package for enhancing code editor experience with fun, interactive elements.

This package contains classes that provide:
- Easter eggs triggered by specific phrases
- Time-based personality shifts
- Code error alerts with monster themes
"""

from .easter_eggs import EasterEggs
from .time_based_shifts import TimeBasedShifts
from .code_monster_alerts import CodeMonsterAlerts

__all__ = ["EasterEggs", "TimeBasedShifts", "CodeMonsterAlerts"]

# Package version
__version__ = "0.1.0"
