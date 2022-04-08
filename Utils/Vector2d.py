import math

class Vector2D:
    DIGREE_TO_RADIAN: float = 57.2957795130823
    x: float
    y: float

    def __init__(self, param1: float = float(), param2: float = float(), speed:float=float()):
        self.setMembers(param1, param2)

    @property
    def length(self) -> float:
        return self.calculateLength(self.x, self.y)

    @property
    def length2(self) -> float:
        return self.calculateLength2(self.x, self.y)

    def calculateLength2(self, param1: float, param2: float) -> float:
        return param1 * param1 + param2 * param2

    def calculateLength(self, param1: float, param2: float) -> float:
        return math.sqrt(self.calculateLength2(param1, param2))

    def validateAngle(self, param1: float) -> float:
        while param1 < -math.pi:
            param1 = param1 + math.pi * 2
        while param1 > math.pi:
            param1 = param1 - math.pi * 2
        return param1

    def validateAngleInDegrees(self, param1: float) -> float:
        while param1 < -180:
            param1 = param1 + 180 * 2
        while param1 > 180:
            param1 = param1 - 180 * 2
        return param1

    def getSectorAngle(self, param1: float, param2: float) -> float:
        return param2 / param1

    def radianToDegree(self, param1: float) -> float:
        return param1 * self.DIGREE_TO_RADIAN

    def degreeToRadian(self, param1: float) -> float:
        return param1 / self.DIGREE_TO_RADIAN

    def distance(self, param2: "Vector2D") -> float:
        _loc3_: "Vector2D" = Vector2D(self.x - param2.x, self.y - param2.y)
        return _loc3_.length

    def setMembersByVector(self, param1: "Vector2D") -> None:
        self.x = param1.x
        self.y = param1.y

    def clone(self) -> "Vector2D":
        return Vector2D(self.x, self.y)

    def setMembers(self, param1: float, param2: float) -> None:
        self.x = param1
        self.y = param2

    def addVector(self, param1: "Vector2D") -> None:
        self.x = self.x + param1.x
        self.y = self.y + param1.y

    def add(self, param1: float, param2: float) -> None:
        self.x = self.x + param1
        self.y = self.y + param2

    def substractVector(self, param1: "Vector2D") -> None:
        self.x = self.x - param1.x
        self.y = self.y - param1.y

    def substract(self, param1: float, param2: float) -> None:
        self.x = self.x - param1
        self.y = self.y - param2

    def multiplyVector(self, param1: "Vector2D") -> None:
        self.x = self.x * param1.x
        self.y = self.y * param1.y

    def multiply(self, param1: float) -> None:
        self.x = self.x * param1
        self.y = self.y * param1

    def addVectorC(self, param1: "Vector2D") -> "Vector2D":
        return Vector2D(self.x + param1.x, self.y + param1.y)

    def substractVectorC(self, param1: "Vector2D") -> "Vector2D":
        return Vector2D(self.x - param1.x, self.y - param1.y)

    def multiplyC(self, param1: float) -> "Vector2D":
        return Vector2D(self.x * param1, self.y * param1)

    def vectorProjectionOnto(self, param1: "Vector2D") -> "Vector2D":
        _loc2_: "Vector2D" = param1.getUnitVector()
        _loc2_.multiply(self.scalarProjectionOnto(param1))
        return _loc2_

    def getUnitVector(self) -> "Vector2D":
        _loc1_: float = self.length
        if _loc1_:
            return Vector2D(self.x / _loc1_, self.y / _loc1_)
        return Vector2D(self.x, self.y)

    def scalarProjectionOnto(self, param1: "Vector2D") -> float:
        return ((self.x * param1.x + self.y * param1.y) / param1.length)

    def getNormale(self) -> "Vector2D":
        return Vector2D(-1 * self.y, self.x)

    def getOpositeToNormale(self) -> "Vector2D":
        return Vector2D(self.y, -1 * self.x)

    def getAngle(self) -> float:
        _loc1_: float = math.atan2(self.y, self.x) + math.pi / 2
        return self.validateAngle(_loc1_)

    def getAngleBetween(self, param1: "Vector2D") -> float:
        _loc2_: float = param1.getAngle() - self.getAngle()
        return self.validateAngle(_loc2_)

    def getAngleInDegrees(self) -> float:
        return self.radianToDegree(self.getAngle())

    def setMembersByRA(self, param1: float, param2: float) -> None:
        self.setMembersByRAC(param1, param2, 0, 0)

    def rotateTo(self, param1: float) -> None:
        self.setMembersByRAC(self.length, self.getAngle() + param1, 0, 0)

    def rotateToDegrees(self, param1: float) -> None:
        self.setMembersByRAC(self.length, self.getAngle() + self.degreeToRadian(param1), 0, 0)

    def setMembersByRAC(self, param1: float, param2: float, param3: float, param4: float) -> None:
        param2 = param2 - math.pi / 2
        self.x = param1 * math.cos(param2) + param3
        self.y = param1 * math.sin(param2) + param4


