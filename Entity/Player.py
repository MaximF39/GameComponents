from Entity.Components.Cash import Cash
from Entity.Components.EXP_STAT import Experience, Status

from Entity._Entity import _Entity
from Inventory.PlayerInventory import PlayerInventory
from Packages.PackageCollector import PackageCollector


class Player(_Entity):

    def __init__(self, CN_Ship):
        super().__init__(CN_Ship)
        self.inventory = PlayerInventory(self.Ship)
        self.cash = Cash(0, Player=self)
        self.exp = Experience(0)
        self.status = Status(0)
        self.Pack = PackageCollector()
