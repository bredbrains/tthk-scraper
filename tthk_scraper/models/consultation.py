from datetime import time


class Consultation:
    def __init__(self,
                 weekday: int,
                 start_time: time,
                 end_time: time,
                 additional_data: str = None):
        self.weekday = weekday
        self.start_time = start_time
        self.end_time = end_time
        self.additional_data = additional_data
