from Utils.Time import Time
from Utils.Vector2d import Vector2D


class MovableSpaceObject:

    def __init__(self, x, y):
        self.V2D = Vector2D(x, y)
        self.__timer = Time()

    def move(self):
        tick: float = self.__timer.tick()
        if isinstance(self.select, SpaceObject) and self.selected:
            vector = Vector2D(self.V2D.x - self.select.V2D.x, self.V2D.y - self.select.V2D.y).getUnitVector()
            vector.multiply(self.targetRadius)
            self.setTarget((round(self.select.V2D.x + vector.x), round(self.select.V2D.y + vector.y)), True)

        if self.isAbsoluteCoordinate(self.getTarget): return
        vector = Vector2D(self.TargetX - self.x, self.TargetY - self.y).getUnitVector()
        move = tick * self.speed
        dis = self.distance(Vector2D(self.TargetX, self.TargetY))
        vector.multiply(move if move < dis else dis)
        self.addVector(vector)

    def crear(self):
        self.setSelect(None, False, self.getCoordinate)
