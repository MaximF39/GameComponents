from datetime import datetime
import time

from datetime import datetime
import time


class Time:
    DAY: int = 864000000000

    HOUR: int = 36000000000

    MINUTE: int = 600000000

    SECOND: int = 10000000

    MILLISECOND: int = 10000

    LastTime: float

    FPS: float

    def __init__(self, fps: float = 1000):
        self.LastTime = Time.Hash()
        self.FPS = fps

    def tick(self) -> float:
        OldLastTime = self.LastTime
        self.LastTime = Time.Hash()
        return ((self.LastTime - OldLastTime) / self.SECOND) * self.FPS

    @staticmethod
    def Hash() -> float:
        return (datetime.now() - datetime(1, 1, 1)).total_seconds() * Time.SECOND

