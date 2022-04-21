from Vacuum.Game.Items._Back._Item import _Item
from Vacuum.Static.Type.Package.T_ServerRequest import T_ServerRequest


class Weapon(_Item):

    def use(self):
        super().use()
        for skill in self.restrictions:
            if skill['type'] == 4:
                self.inventory.Owner.Ship.cpu_used += skill['value']
                self.inventory.Owner.Ship.active_weapons.append(self)
                self.inventory.Owner.Ship.cnt_active_weapon += 1
                self.inventory.Owner.Pack += T_ServerRequest.ACTIVE_WEAPONS


    def unuse(self):
        super().unuse()
        for skill in self.restrictions:
            if skill['type'] == 4:
                self.inventory.Owner.Ship.cpu_used -= skill['value']
                self.inventory.Owner.Ship.active_weapons.remove(self)
                self.inventory.Owner.Ship.cnt_active_weapon -= 1
                self.inventory.Owner.Pack += T_ServerRequest.ACTIVE_WEAPONS
