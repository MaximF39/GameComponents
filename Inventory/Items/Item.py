import copy
import uuid

from Static.ParseJson import item_CN


class Item(dict):
    """
    Item += Item
    """

    def __init__(self, CN:int, wear:int=None, const=False):
        super().__init__()
        self['const'] = const
        self.update(item_CN(CN, wear))
        self['guid'] = self._get_guid()

    def __iadd__(self, item_: "Item"):
        return self.__add__(item_)

    def __add__(self, item_):
        if self['const']:
            return self

        if isinstance(item_, Item):
            self['wear'] += item_['wear']
            return self

        if isinstance(item_, int):
            self['wear'] += item_
            return self

    def __isub__(self, other):
        if self['const']:
            return self
        if isinstance(other, int):
            self['wear'] -= other
            if not self['stack']:
                return self
            else:
                if self['wear'] == 0:
                    self.__del_invt_A_item(wear=other)
                    return self
                elif self['wear'] > 0:
                    return self.my_copy_D_invt()
                else:
                    raise NotImplementedError("wear -= int; wear < 0")

    def __sub__(self, other: int):
        self.__isub__(other)
        if self['stack']:   return self.my_copy_D_invt(wear=other, const=False)
        return self

    def get_size(self, wear=None):
        if self['stack']:   return round(self['size'] * (wear or self['wear']))
        else:               return round(self['size'])

    def get_cost(self, wear=None):
        if self['stack']:   return round(self['cost'] * (wear or self['wear']))
        else:               return round(self['cost'])

    def copy(self, /, wear=None, const=None) -> "Item":
        item_ = copy.copy(self)
        item_['guid'] = item_._get_guid()
        if not wear is None:    item_['wear'] = wear
        if not const is None:   item_['const'] = const
        return item_

    def my_copy_D_invt(self, /, **kwargs) -> "Item":
        item_ = self.copy(**kwargs)
        if 'inventory' in item_:    del item_['inventory']
        return item_

    def __del_invt_A_item(self, /, wear=None):
        if "inventory" in self:
            del self['inventory'][self['guid']]
            del self['inventory']
        if wear:
            self['wear'] = wear

    """ Use logic items """

    def use(self):
        self['inUsing'] = True

    def unuse(self):
        self['inUsing'] = False

    @staticmethod
    def _get_guid():
        return uuid.uuid4()
