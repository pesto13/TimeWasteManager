from dataclasses import dataclass
import time


@dataclass
class Info():
    name: str
    cathegory: str
    start_time: time.time
    delta_time: int