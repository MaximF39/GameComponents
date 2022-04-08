from Entity.Components.Ship import Ship


class _Entity:

    def __init__(self):
        self.ship = Ship(self, 0, 0, 100)
