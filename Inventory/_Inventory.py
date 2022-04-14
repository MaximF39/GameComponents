import sys
import uuid
import copy


class _Inventory(dict):
    """
    _Inventory += Item
    _Inventory -= Item # remove Item
    _Inventory.send_item(Whom, guid, wear=__None)
    """

    def __init__(self, Owner):
        self.Owner = Owner
        super().__init__()

    def __iadd__(self, item_: "Item"):
        self.__set_inventory_item(item_)
        my_item = self.__find_item_stack(item_)
        if my_item:
            my_item += item_
            return self
        self[item_['guid']] = item_
        return self

    def __isub__(self, item_):
        # if not isinstance(item_, Item):
        #     raise NotImplementedError("inventory only -= item")
        my_item = self.__find_item_stack(item_)
        if my_item:
            my_item -= item_['wear']
            return self

        if 'inventory' in item_:
            del item_['inventory']
        del self[item_['guid']]
        return self


    def send_item(self, Whom, guid=None, wear=None, item_=None):
        item_:"Item" = self._get_item(guid, item_)
        if item_['const']:
            item_ = item_.my_copy_D_invt(wear=wear, const=False)
        if wear is None:
            Whom.inventory += item_
        elif item_['stack']:
            Whom_item = item_ - wear
            Whom.inventory += Whom_item

    def __find_item_stack(self, item_) -> "Item":
        """ get self.item['CN'] == item_['CN'] """
        if item_['stack']:
            for _, my_item in self.items():
                if my_item['classNumber'] == item_['classNumber']:
                    return my_item

    @staticmethod
    def __del_inventory_item(item_):
        if 'inventory' in item_:
            del item_['inventory'][item_['guid']]

    def __set_inventory_item(self, item_):
        self.__del_inventory_item(item_)
        item_['inventory'] = self


    def _get_item(self, guid, item_):
        if not guid and not item_:
            raise NotImplementedError("No found guid or item_")
        if item_:
            return item_
        return self[guid]
