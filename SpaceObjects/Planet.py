from SpaceObjects.Components.BigObject import BigObject
from SpaceObjects.Components.Shop import Shop


class Planet(BigObject):

    def __init__(self, data, Location):
        super().__init__(data, Location)
        self.shop = Shop(data, Planet)
