from Vacuum.Game.Components.Inventory._Inventory import _Inventory


class RepositoryInventory(_Inventory):

    def send_item(self, Whom, guid=None, wear=None, item_=None):
        item_ = self._get_item(guid, item_)
        Whom.cash -= item_.get_size(wear) * 10
        super().send_item(Whom, item_=item_, wear=wear)
