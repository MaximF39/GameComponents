from Vacuum.Game.Components.Inventory._Inventory import _Inventory
from Vacuum.Static.Type.Package.T_ServerRequest import T_ServerRequest


class LocationInventory(_Inventory):

    def __iadd__(self, other):
        super().__iadd__(other)
        for player in self.Owner.players:
            if player.SpaceObject is None:
                player.Pack += T_ServerRequest.ITEMS

    def __isub__(self, other):
        super().__isub__(other)
        for player in self.Owner.players:
            if player.SpaceObject is None:
                player.Pack += T_ServerRequest.ITEMS

    def send_item(self, Whom, guid=None, wear=None, item_=None):
        super().send_item(Whom, guid, wear, item_)
        for player in self.Owner.players:
            if player.SpaceObject is None:
                player.Pack += T_ServerRequest.ITEMS
