from Components.MovableSpaceObject import MovableSpaceObject
from Components.Heal_A_Energ import Energy, Health
from Inventory.EntityInventory import EntityInventory
from Static.ParseJson import ship_CN


class Ship(MovableSpaceObject):

    def __init__(self, Owner, CN_Ship, x, y, speed):
        self.OwnerShip = Owner
        super().__init__(x, y, speed)
        self.base = self.get_base(CN_Ship)
        self.__dict__.update(self.base)
        self.health = Health(self.base['max_health'], Owner=self)
        self.energy = Energy(self.base['max_energy'], Owner=self)

    @staticmethod
    def get_base(CN):
        return ship_CN(CN)