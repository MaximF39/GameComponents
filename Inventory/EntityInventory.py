from Inventory._Inventory import _Inventory
from Utils.MyInt import MyInt


class Hold(int):
    max: int

    def __new__(cls, value, **kwargs):
        return super().__new__(cls, value)

    def __init__(self, value, **kwargs):
        super().__init__()
        self.max = kwargs['max']

    def __iadd__(self, other):
        return Hold(super().__add__(other), max=self.max)

    def __isub__(self, other):
        return Hold(super().__sub__(other), max=self.max)


class EntityInventory(_Inventory):
    Hold: object

    def __init__(self, Ship):
        super().__init__(Ship)
        self.Ship = Ship
        self.Hold = Hold(0, max=self.Ship.base["size"])

    def __iadd__(self, item_):
        self.Hold += item_.get_size()
        return super().__iadd__(item_)

    def __isub__(self, item_):
        self.Hold -= item_.get_size()
        return super().__isub__(item_)

    def send_item(self, Whom, guid=None, wear=None, item_=None):
        item_ = self._get_item(guid, item_)
        self.Hold -= item_.get_size(wear)
        super().send_item(Whom, wear=wear, item_=item_)

    def kill_drop(self):
        for item in self.values():
            match item.__class__.__name__:
                case "Resource":
                    percent = 80
                    self.send_item(self.Ship.Owner.Location, item_=item, wear=(0.01 * percent * item.wear))
