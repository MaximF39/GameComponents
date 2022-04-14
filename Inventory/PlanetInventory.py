from Inventory._Inventory import _Inventory


class PlanetInventory(_Inventory):

    def __init__(self, Owner, items:tuple=None):
        super().__init__(Owner)
        for item in items:
            self += item

    def __iadd__(self, item_):
        if 'inventory' in item_:
            item_['inventory'].Owner.Cash += item_.get_cost()
        super().__iadd__(item_)
        return self

    def send_item(self, Whom, guid=None, wear=None, item_=None):
        item_ = self._get_item(guid, item_)
        Whom.Cash -= item_.get_cost(wear)
        super().send_item(Whom, item_=item_, wear=wear)