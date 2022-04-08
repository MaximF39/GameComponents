from Components.MovableSpaceObject import MovableSpaceObject
from Components.Heal_A_Energ import Energy, Health
from Inventory.ShipInventory import ShipInventory


class Ship(MovableSpaceObject):

    def __init__(self, Owner, x, y, speed):
        self.OwnerShip = Owner
        super().__init__(x, y, speed)
        self.inventory = ShipInventory(self)
        self.base = self.get_base()
        self.health = Health(self.base['Health'], Owner=self)
        self.energy = Energy(self.base['Energy'], Owner=self)

    @staticmethod
    def get_base():
        return {}