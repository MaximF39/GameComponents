from Vacuum.Game.Entity._Back.Components.Ship import Ship


class __Entity:
    inventory: object

    def __init__(self, data):
        self.__dict__.update(data)
        self.Ship = Ship(self, data['CN_Ship'], 0, 0)
        self.droids = []
        self.SpaceObject = None
        self.Battle = None

    def entry(self):
        self.Location.set(self)
        if self.SpaceObject:
            self.SpaceObject.set(self)

    def set_system(self, system_id):
        next_location = getattr(self.Game, f"Location_{system_id}")
        self.Ship.setTarget(next_location)
