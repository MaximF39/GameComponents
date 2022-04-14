from datetime import datetime
import time


class Time:
    LastTime: float

    def tick(self) -> float:
        if hasattr(self, "LastTime"):
            self.LastTime = Time.Hash()
        OldLastTime = self.LastTime
        self.LastTime = Time.Hash()
        return self.LastTime - OldLastTime

    @staticmethod
    def Hash() -> float:
        return (datetime.now() - datetime(1, 1, 1)).total_seconds()