from Entity.Components.Ship import Ship


class _Entity:
    inventory: object

    def __init__(self, CN_Ship):
        self.Ship = Ship(self, CN_Ship, 0, 0, 100)
