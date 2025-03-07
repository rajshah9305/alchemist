# features/time_based_shifts.py
from datetime import datetime

class TimeBasedShifts:
    def get_current_personality(self):
        current_hour = datetime.now().hour
        if 6 <= current_hour < 18:
            return "normal_mode"
        else:
            return "dark_magic_mode"