from Inventory._Inventory import _Inventory


class AngarInventory(_Inventory):

    def __iadd__(self, Ship):
        if isinstance(Ship, "ShipItem"):pass
        self['inventory'].Owner.Ship = Ship
        return super().__iadd__(Ship)
