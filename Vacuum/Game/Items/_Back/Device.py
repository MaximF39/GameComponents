import threading

from Vacuum.Game.Items._Back._Item import _Item
from Vacuum.Static.Type.Package.T_ServerRequest import T_ServerRequest


class Device(_Item):

    def __init__(self, data):
        super().__init__(data)
        self.reloaded_time = 0

    def use(self):
        super().use()
        self.inventory.Owner.Ship.active_devices.append(self)
        for effect in self.effects:
            if effect["effect_time"] == 0:
                self.inventory.Owner.Ship.effects[effect["effect_type"]] = "const"
            else:
                self.inventory.Owner.Pack += T_ServerRequest.ACTIVE_DEVICES

    def unuse(self):
        super().unuse()
        self.inventory.Owner.Ship.active_devices.remove(self)
        for effect in self.effects:
            if effect["effect_time"] == 0:
                self.inventory.Owner.Ship.effects[-effect["effect_type"]] = "const"
            else:
                self.inventory.Owner.Pack += T_ServerRequest.ACTIVE_DEVICES

    def click(self, targetId, id_droid, effectType):
        for effect in self.effects:
            if effect["effect_type"] == effectType:
                self.inventory.Owner.Ship.effects[effect["effect_type"]] = effect['effect_time']
                threading.Timer(self.reload_time / 1000, self.reload_device)
                self.inventory.Owner.Ship.cnt_active_device += 1

    def reload_device(self):
        self.inventory.Owner.Ship.cnt_active_device -= 1
