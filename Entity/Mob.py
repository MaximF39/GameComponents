from Entity._Entity import _Entity
from Inventory.EntityInventory import EntityInventory


class Mob(_Entity):

    def __init__(self, CN_Ship):
        super().__init__(CN_Ship)
        self.inventory = EntityInventory(self.Ship)