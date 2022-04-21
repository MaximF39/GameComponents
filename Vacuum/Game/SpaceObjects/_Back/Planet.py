from ._Components.BigObject import BigObject
from ._Components.SetMSO import SetMSO
from ._Components.Shop import Shop


class Planet(BigObject, SetMSO):

    def __init__(self, data):
        super().__init__(data)
        SetMSO.__init__(self, data['x'], data['y'])
        self.shop = Shop(data)
        self.clan_id = 0

    def move(self):
        pass