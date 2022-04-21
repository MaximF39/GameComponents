from Vacuum.Game.Components.Inventory._Inventory import _Inventory


class AngarInventory(_Inventory):

    def __iadd__(self, Ship):
        self.inventory.Owner.Ship = Ship
        return super().__iadd__(Ship)
