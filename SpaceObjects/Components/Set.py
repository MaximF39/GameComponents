from abc import ABC

from Components.MovableSpaceObject import MovableSpaceObject


class Set(MovableSpaceObject, metaclass=ABC):

    def __init__(self, x, y):
        super().__init__(x, y)

    def set(self, Whom):
        raise NotImplementedError("sss")