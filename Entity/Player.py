from Entity.Components.Cash import Cash
from Entity.Components.EXP_STAT import Experience, Status
from Entity._Entity import _Entity
from Packages.PackageCollector import PackageCollector


class Player(_Entity):

    def __init__(self):
        super().__init__()
        self.cash = Cash(0, Player=self)
        self.exp = Experience(100)
        self.status = Status(100)
        self.Pack = PackageCollector()
