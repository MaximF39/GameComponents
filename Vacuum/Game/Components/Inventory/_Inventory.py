import sys
import uuid
import copy


class _Inventory(dict):
    """
    _Inventory += _Item
    _Inventory -= _Item # remove _Item
    _Inventory.send_item(Whom, guid, wear=__None)
    """

    def __init__(self, Owner):
        self.Owner = Owner
        super().__init__()

    def __iadd__(self, item_: "_Item"):
        self.__set_inventory_item(item_)
        my_item = self.__find_item_stack(item_)
        if my_item:
            my_item += item_
            return self
        self[item_.guid] = item_
        return self

    def __isub__(self, item_):
        my_item = self.__find_item_stack(item_)
        if my_item:
            my_item -= item_.wear
            return self

        if hasattr(item_, 'inventory'):
            del item_.inventory
        del self[item_.guid]
        return self


    def send_item(self, Whom, guid=None, wear=None, item_=None):
        item_:"_Item" = self._get_item(guid, item_)
        if item_.const:
            item_ = item_.my_copy_D_invt(wear=wear, const=False)
        if wear is None:
            Whom.inventory += item_
        elif item_.stack:
            Whom_item = item_ - wear
            Whom.inventory += Whom_item

    def __find_item_stack(self, item_) -> "_Item":
        """ get self.item['CN'] == item_['CN'] """
        if item_.stack:
            for _, my_item in self.items():
                if my_item.class_number == item_.class_number:
                    return my_item

    @staticmethod
    def __del_inventory_item(item_):
        if hasattr(item_, 'inventory'):
            del item_.inventory[item_.guid]

    def __set_inventory_item(self, item_):
        self.__del_inventory_item(item_)
        item_.inventory = self


    def _get_item(self, guid, item_):
        if not guid and not item_:
            raise NotImplementedError("No found guid or item_")
        if item_:
            return item_
        return self[guid]

    def use_item(self, guid):
        self[guid].inUsing = True
        self[guid].use()

    def unuse_item(self, guid):
        self[guid].inUsing = False
        self[guid].unuse()
