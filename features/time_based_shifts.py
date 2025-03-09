from datetime import datetime
import pytz

class TimeBasedShifts:
    def __init__(self, timezone='UTC'):
        self.timezone = pytz.timezone(timezone)
        self.personalities = {
            'normal_mode': {'start': 6, 'end': 18},
            'dark_magic_mode': {'start': 18, 'end': 6}
        }
    
    def get_current_personality(self):
        try:
            current_time = datetime.now(self.timezone)
            current_hour = current_time.hour
            
            if 6 <= current_hour < 18:
                return "normal_mode"
            else:
                return "dark_magic_mode"
        except Exception as e:
            # Fallback to normal_mode in case of errors
            logging.error(f"Error determining personality: {str(e)}")
            return "normal_mode"
    
    def set_personality_hours(self, personality, start_hour, end_hour):
        """Configure custom hours for personality shifts"""
        if not (0 <= start_hour <= 23 and 0 <= end_hour <= 23):
            raise ValueError("Hours must be between 0 and 23")
        self.personalities[personality] = {'start': start_hour, 'end': end_hour}
