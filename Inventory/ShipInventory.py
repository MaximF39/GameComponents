from Inventory import _Inventory
from Items.Item import Item
from Utils import MyInt


class Hold(int):
    max: int

    def __new__(cls, hold, **kwargs):
        if hold > cls.max:
            raise NotImplementedError('hold > maxHold')
        return super().__new__(cls, hold)

    def __init__(self, value, **kwargs):
        self.__dict__.update(kwargs)

    def __iadd__(self, other):
        return self.__new__(type(self), self.__add__(other), max=self.max)

    def __isub__(self, other):
        return self.__new__(type(self), self.__sub__(other), max=self.max)


class ShipInventory(_Inventory):

    def __init__(self, Ship):
        self.Ship = Ship
        self.hold = Hold(0, max=5000)  # Ship['maxHold'])

    def __iadd__(self, item_):
        self.hold += item_.get_size()
        return super().__iadd__(item_)

    def __isub__(self, item_):
        self.hold -= item_.get_size()
        return super().__isub__(item_)

    def send_item(self, Whom, guid=None, wear=None, item_=None):
        item_ = self._get_item(guid, item_)
        self.hold -= item_.get_size(wear)
        super().send_item(Whom, wear=wear, item_=item_)

    def kill_drop(self):
        for item in self.values():
            match item.__class__.__name__:
                case "Resource":
                    percent = 80
                    self.send_item(self.Ship.Owner.Location, item_=item, wear=(0.01 * percent * item.wear))
