from Vacuum.Game.Components.Inventory._Inventory import _Inventory
from Vacuum.Static.Type.Package.T_ServerRequest import T_ServerRequest


class EntityInventory(_Inventory):
    Hold: object

    def __init__(self, Player):
        super().__init__(Player)
        self.Player = Player
        self.Ship = Player.Ship
        self.Hold = Hold(0, max=self.Ship.base["size"], Player=Player)

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


class Hold(int):
    max: int

    def __new__(cls, value, **kwargs):
        kwargs['Player'].Pack += T_ServerRequest.UPDATE_HOLD
        return super().__new__(cls, value)

    def __init__(self, value, **kwargs):
        super().__init__()
        self.max = kwargs['max']
        self.Player = kwargs['Player']

    def __iadd__(self, other):
        return Hold(super().__add__(other), max=self.max, Player=self.Player)

    def __isub__(self, other):
        return Hold(super().__sub__(other), max=self.max, Player=self.Player)