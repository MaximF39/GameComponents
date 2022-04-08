import copy
import uuid


class Item(dict):
    """
    Item += Item
    """
    __slots__ = ('guid', 'classNumber', "stack", "wear", "inUsing", "satisfying", 'size', 'const')

    def __init__(self, seq=None, **kwargs):
        if 'const' in seq:  self['const'] = seq
        else:   self['const'] = False

        for need in self.__slots__:
            if not need in seq:
                if need == 'const':
                    continue
                raise AttributeError(f"{self.__class__.__name__} hasn't attribute %s" % need)
        super().__init__(seq, **kwargs)

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
        if self['stack']:   return self['size'] * (wear or self['wear'])
        else:               return self['size']

    def get_cost(self, wear=None):
        if self['stack']:   return self['cost'] * (wear or self['wear'])
        else:               return self['cost']

    def copy(self, /, wear=None, const=None) -> "Item":
        item_ = copy.copy(self)
        item_['guid'] = uuid.uuid4()
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
