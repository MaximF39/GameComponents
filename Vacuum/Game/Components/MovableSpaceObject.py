import threading
import time

from Vacuum.Game.Utils.Time import Time
from Vacuum.Game.Utils.Vector2d import Vector2D


class MovableSpaceObject:
    all = []

    def __init__(self, x, y):
        self.all.append(self)
        self.V2D = Vector2D(x, y)
        self.__timer = Time()
        self.T_V2D = self.V2D
        self.target_obj = None
        self.targetRadius = 0

    def move(self):
        tick: float = self.__timer.tick()

        if self.target_obj:
            vector = self.V2D.substractVectorC(self.T_V2D).getUnitVector()
            vector.multiply(self.targetRadius)
            self.setTarget(self.V2D.addVectorC(vector))

        if self.T_V2D.coord == self.V2D.coord:
            if self.target_obj:
                self.target_obj.set(self.OwnerShip)
            return

        vector = self.T_V2D.substractVectorC(self.V2D).getUnitVector()
        move = tick * self.speed / 1000
        dis = self.V2D.distance(self.T_V2D)
        self.V2D.addVector(vector.multiplyC(move if move < dis else dis))



    def setTarget(self, V2D=None):
        if V2D is None:
            self.T_V2D = self.V2D
            self.target_obj = None
        else:
            from Vacuum.Game.SpaceObjects._Back._Components.Set import Set
            if isinstance(V2D, Set):
                self.target_obj = V2D
                from Vacuum.Game.SpaceObjects._Back.Location import Location
                if isinstance(V2D, Location):
                    self.T_V2D = self.target_obj.get_v2d_to_target_location(Who=self.OwnerShip).getNormale()
                else:
                    self.T_V2D = self.target_obj.V2D
            if isinstance(V2D, Vector2D):
                self.T_V2D = V2D

    def crear(self):
        self.target_obj = None
        self.setTarget()
