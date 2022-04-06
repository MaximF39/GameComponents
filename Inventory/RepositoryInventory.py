import uuid

from Inventory.B_Inventory import B_Inventory, Item


class RepositoryInventory(B_Inventory):

    def send_item(self, Whom, guid=None, wear=None, item_=None):
        item_ = self._get_item(guid, item_)
        Whom.cash -= item_.get_size(wear) * 10
        super().send_item(Whom, item_=item_, wear=wear)
