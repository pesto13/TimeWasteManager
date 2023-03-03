from dataclasses import dataclass
import time
from datetime import date

@dataclass
class Info():
    application_name: str
    category: str
    start_time: time.time
    seconds_used: int
    using_date: date