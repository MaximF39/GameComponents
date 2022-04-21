from Vacuum.Game.SpaceObjects._Back._Components.BigObject import BigObject
from Vacuum.Game.SpaceObjects._Back._Components.SetSO import SetSO


class Hive(BigObject, SetSO):
    def __init__(self, data):
        super().__init__(data)
        SetSO.__init__(self,data['x'], data['y'])
        self.class_number = 256 - data['type']
        self.Radius = 0
        self.clan_id = 0
        self.angle = 0
        self.size = 10000