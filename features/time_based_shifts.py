# features/time_based_shifts.py
from datetime import datetime

class TimeBasedShifts:
    """Manages personality shifts based on time of day."""
    
    def __init__(self, day_mode="normal_mode", night_mode="dark_magic_mode", 
                 day_start=6, night_start=18):
        """
        Initialize the TimeBasedShifts feature.
        
        Args:
            day_mode (str): Personality mode during daytime hours
            night_mode (str): Personality mode during nighttime hours
            day_start (int): Hour when day mode begins (0-23)
            night_start (int): Hour when night mode begins (0-23)
        """
        self.day_mode = day_mode
        self.night_mode = night_mode
        self.day_start = day_start
        self.night_start = night_start

    def get_current_personality(self):
        """
        Determine the current personality mode based on time of day.
        
        Returns:
            str: Current personality mode name
        """
        current_hour = datetime.now().hour
        if self.day_start <= current_hour < self.night_start:
            return self.day_mode
        else:
            return self.night_mode
    
    def get_next_shift_time(self):
        """
        Calculate when the next personality shift will occur.
        
        Returns:
            datetime: Next shift time
        """
        now = datetime.now()
        current_hour = now.hour
        
        if self.day_start <= current_hour < self.night_start:
            # Currently in day mode, next shift is to night mode
            next_shift = now.replace(hour=self.night_start, minute=0, second=0, microsecond=0)
        else:
            # Currently in night mode, next shift is to day mode
            if current_hour >= self.night_start:
                # If it's after night start, the next day mode is tomorrow
                next_shift = now.replace(hour=self.day_start, minute=0, second=0, microsecond=0)
                next_shift = next_shift.replace(day=next_shift.day + 1)
            else:
                # If it's before day start, the next day mode is today
                next_shift = now.replace(hour=self.day_start, minute=0, second=0, microsecond=0)
                
        return next_shift
