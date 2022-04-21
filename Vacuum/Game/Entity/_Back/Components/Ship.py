from Vacuum.Game.Components.MovableSpaceObject import MovableSpaceObject
from Vacuum.Game.Components.Heal_A_Energ import Energy, Health
from Vacuum.Game.Components.SHeal_A_SEnergy import HealthShip, EnergyShip
from Vacuum.Game.Entity._Back.Components.Effect import Effect
from Vacuum.Game.Items.Item import Item
from Vacuum.Static.ParseJson import ship_CN
from Vacuum.Static.Type.Package.T_ServerRequest import T_ServerRequest
from Vacuum.Static.Type.Package.T_UpdateValue import T_UpdateValue


class Ship(MovableSpaceObject):

    def __init__(self, Owner, CN_Ship, x, y):
        self.OwnerShip = Owner
        self.class_number = CN_Ship
        self.base = self.get_base(CN_Ship)
        self.__dict__.update(self.base)
        self.health = HealthShip(self.base['max_health'], max=self.base['max_health'])
        self.energy = EnergyShip(self.base['max_energy'], max=self.base['max_energy'])
        self.speed = self.max_speed
        self.cpu_used = 0
        super().__init__(x, y)

        self.effects = Effect(Ship=self)
        self.cnt_active_device = 0
        self.cnt_active_weapon = 0
        self.active_weapons = []
        self.active_devices = []
        self.droids = []

    def init(self):
        self.engine = Engine(self)
        item = Item(4, 1000, inUsing=True)
        self.activeWeapons = [item]
        self.OwnerShip.inventory += item

    @staticmethod
    def get_base(CN):
        return ship_CN(CN)

    def leaveLocation(self):
        if self.OwnerShip.SpaceObject:
            self.OwnerShip.SpaceObject.remove(self.OwnerShip)
        elif self.OwnerShip.Location:
            self.OwnerShip.Location.remove(self.OwnerShip)

class Engine:

    def __init__(self, Owner, item=None):
        self.Owner = Owner
        if item is None:
            item = Item(57, 500, inUsing=True)
            self.Owner.OwnerShip.inventory += item
        self.engine = item
        self.Owner.OwnerShip.Pack += {T_ServerRequest.UPDATE_VALUE: T_UpdateValue.HyperRadius}

    def replace(self, item):
        self.engine.unuse()
        self.engine = item
        self.Owner.OwnerShip.Pack += ({T_ServerRequest.UPDATE_VALUE: T_UpdateValue.HyperRadius},
                                        {T_ServerRequest.UPDATE_VALUE: T_UpdateValue.HyperCost})
