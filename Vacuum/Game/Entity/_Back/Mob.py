from Vacuum.Game.Entity._Back.__Entity import __Entity
from Vacuum.Game.Components.Inventory import EntityInventory


class Mob(__Entity):

    def __init__(self, data):
        super().__init__(data)
        self.inventory = EntityInventory(self.Ship)