from Utils.Vector2d import Vector2D


class MovableSpaceObject:

    def __new__(cls, *args, **kwargs):
        if cls == MovableSpaceObject:
            raise NotImplementedError("Вы можете использовать этот класс только в качестве наследника")

    def __init__(self, x, y, speed):
        self.Vector2d = Vector2D(x, y, speed)

