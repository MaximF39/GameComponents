import uuid
import copy


class B_Inventory(dict):
    """
    B_Inventory += Item
    B_Inventory -= Item # remove Item
    B_Inventory.send_item(Whom, guid, wear=None)
    """

    def __init__(self, Owner):
        self.Owner = Owner
        super().__init__()

    def __find_item_stack(self, item_) -> "item":
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

    def __iadd__(self, item_: "Item"):
        self.__set_inventory_item(item_)
        my_item = self.__find_item_stack(item_)
        if my_item:
            my_item += item_
            return self
        self[item_['guid']] = item_
        return self

    def __isub__(self, item_):
        if not isinstance(item_, Item):
            raise NotImplementedError("inventory only -= item")
        my_item = self.__find_item_stack(item_)
        if my_item:
            my_item -= item_['wear']
            return self

        if 'inventory' in item_:
            del item_['inventory']
        del self[item_['guid']]
        return self

    def _get_item(self, guid, item_):
        if not guid and not item_:
            raise NotImplementedError("No found guid or item_")
        if item_:
            return item_
        return self[guid]

    def send_item(self, Whom, guid=None, wear=None, item_=None):
        item_ = self._get_item(guid, item_)
        if wear is None:
            Whom.inventory += item_
        elif item_['stack']:
            Whom_item = item_ - wear
            Whom.inventory += Whom_item
        else:
            raise NotImplementedError('передано stack=False, wear=')

class Item(dict):
    """
    Item += Item
    """
    __slots__ = ('guid', 'classNumber', "stack", "wear", "inUsing", "satisfying", 'size', 'const')

    def __init__(self, seq=None, **kwargs):
        if 'const' in seq:  self.const = seq
        else:   self.const = False

        for need in self.__slots__:
            if not need in seq:
                if need == 'const':
                    continue
                raise AttributeError(f"{self.__class__.__name__} hasn't attribute %s" % need)
        super().__init__(seq, **kwargs)

    def __iadd__(self, item_: "Item"):
        return self.__add__(item_)

    def __add__(self, item_):
        if isinstance(item_, Item):
            self['wear'] += item_['wear']
            return self

        if isinstance(item_, int):
            self['wear'] += item_
            return self

    def __isub__(self, other):
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
        if self['stack']:   return self.my_copy_D_invt(wear=other)
        return self

    def get_size(self, wear=None):
        if self['stack']:   return self['size'] * (wear or self['wear'])
        else:               return self['size']

    def get_cost(self, wear=None):
        if self['stack']:   return self['cost'] * (wear or self['wear'])
        else:               return self['cost']

    def copy(self, /, wear=None):
        item_ = copy.copy(self)
        item_['guid'] = uuid.uuid4()
        if wear:    item_['wear'] = wear
        return item_

    def my_copy_D_invt(self, /, **kwargs):
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

""" TEST """

def test_item():

    def test_stack_F():
        i1 = Item(
            {"guid": uuid.uuid4(), 'classNumber': 10, "stack": False, "wear": 90, "inUsing": False, "satisfying": False, 'size':0.1})

        i1 += 100
        assert i1['wear'] == 190
        i1 -= 100
        assert i1['wear'] == 90
        i1 + 100
        assert i1['wear'] == 190
        i1 - 100
        assert i1['wear'] == 90

    def test_stack_T():
        i1 = Item(
            {"guid": uuid.uuid4(), 'classNumber': 10, "stack": True, "wear": 90, "inUsing": False, "satisfying": False,
             'size': 0.1})

        i1 += 100
        assert i1['wear'] == 190

        i1 -= 100
        assert i1['wear'] == 90
        i1 + 100
        assert i1['wear'] == 190
        i1 - 100
        assert i1['wear'] == 90

        i2 = i1 - 30
        assert i2['wear'] == 30
        assert i1['wear'] == 60

        assert i1['guid'] != i2['guid']

    test_stack_F()
    test_stack_T()

def test_invt():
    class Owner:
        def __init__(self):
            self.inventory = B_Inventory(self)

    """ ADD ITEM """
    p1 = Owner()
    p2 = Owner()

    i1 = Item(
        {"guid": uuid.uuid4(), 'classNumber': 10, "stack": True, "wear": 90, "inUsing": False, "satisfying": False, 'size':0.1})
    i2 = Item(
        {"guid": uuid.uuid4(), 'classNumber': 10, "stack": True, "wear": 90, "inUsing": False, "satisfying": False, 'size':0.1})
    i3 = Item(
        {"guid": uuid.uuid4(), 'classNumber': 12, "stack": False, "wear": 90, "inUsing": False, "satisfying": False, 'size':0.1})
    i4 = Item(
        {"guid": uuid.uuid4(), 'classNumber': 12, "stack": False, "wear": 90, "inUsing": False, "satisfying": False, 'size':0.1})

    p2.inventory += i1
    p1.inventory += i1

    assert p1.inventory[i1['guid']] == i1
    assert p2.inventory.__len__() == 0

    p1.inventory += i2
    assert p1.inventory[i1['guid']]['wear'] == 180

    p1.inventory += i3
    assert p1.inventory[i3['guid']]['wear'] == 90

    p1.inventory += i4
    assert p1.inventory[i4['guid']]['wear'] == 90

    assert p1.inventory.__len__() == 3

    """ REMOVE ITEM """
    p = Owner()
    i1 = Item(
        {"guid": uuid.uuid4(), 'classNumber': 10, "stack": True, "wear": 180, "inUsing": False, "satisfying": False, 'size':0.1})

    p.inventory += i1
    item_ = p.inventory[i1['guid']] - 80

    assert item_['guid'] != i1['guid']
    assert p.inventory[i1['guid']]['wear'] == 100

    item_2 = p.inventory[i1['guid']] - 100

    assert p.inventory.__len__() == 0
    assert item_['wear'] == 80
    assert item_2['wear'] == 100

    """ SEND ITEM """

    p1 = Owner()
    p2 = Owner()

    i1 = Item(
        {"guid": uuid.uuid4(), 'classNumber': 12, "stack": False, "wear": 90, "inUsing": False, "satisfying": False, 'size':0.1})
    p1.inventory += i1
    assert p1.inventory[i1['guid']] == i1

    p1.inventory.send_item(p2, guid=p1.inventory[i1['guid']]['guid'])

    assert p1.inventory.__len__() == 0
    assert p2.inventory[i1['guid']] == i1

    ii2 = Item(
        {"guid": uuid.uuid4(), 'classNumber': 10, "stack": True, "wear": 80, "inUsing": False, "satisfying": False, 'size':0.1})

    p1 = Owner()
    p2 = Owner()

    p1.inventory += ii2
    p1.inventory.send_item(p2, guid=ii2['guid'], wear=70)


    for k, v in p1.inventory.items():
        assert v['wear'] == 10

    for k, v in p2.inventory.items():
        assert v['wear'] == 70

    p1 = Owner()
    ii2 = Item(
        {"guid": uuid.uuid4(), 'classNumber': 10, "stack": True, "wear": 80, "inUsing": False, "satisfying": False, 'size':0.1})
    ii4 = Item(
        {"guid": uuid.uuid4(), 'classNumber': 12, "stack": False, "wear": 80, "inUsing": False, "satisfying": False, 'size':0.1})

    p1.inventory += ii2
    p1.inventory -= ii2
    assert p1.inventory.__len__() == 0

    p1.inventory += ii4
    p1.inventory -= ii4
    assert p1.inventory.__len__() == 0

    p1 = Owner()
    p2 = Owner()
    g = uuid.uuid4()
    o1 = Item({"guid": g, 'classNumber': 10, "stack": True, "wear": 80, "inUsing": False, "satisfying": False, 'size':0.1})
    p1.inventory += o1
    p1.inventory.send_item(p2, guid=g, wear=50)

    for _, v in p1.inventory.items():
        assert p1.inventory[v['guid']]['wear'] == 30

    for _, v in p2.inventory.items():
        assert p2.inventory[v['guid']]['wear'] == 50

    """ CRASH TEST """

    i1 = Item(
        {"guid": uuid.uuid4(), 'classNumber': 10, "stack": True, "wear": 90, "inUsing": False, "satisfying": False, 'size':0.1})
    p = Owner()
    p2 = Owner()
    p.inventory += i1

    p.inventory.send_item(p2, guid=i1['guid'], wear=20)

    for _, v in p.inventory.items():
        assert p.inventory[v['guid']]['wear'] == 70

    p.inventory += i1
    for _, v in p.inventory.items():
        assert p.inventory[v['guid']]['wear'] == 70

    for _, v in p2.inventory.items():
        assert p2.inventory[v['guid']]['wear'] == 20

    """ ITEM - WEAR """

    p1 = Owner()
    i1 = Item(
        {"guid": uuid.uuid4(), 'classNumber': 10, "stack": False, "wear": 90, "inUsing": False, "satisfying": False, 'size':0.1})
    p1.inventory += i1
    p1.inventory[i1['guid']] - 30
    assert p1.inventory[i1['guid']]['wear'] == 60

    p1 = Owner()
    i1 = Item(
        {"guid": uuid.uuid4(), 'classNumber': 10, "stack": False, "wear": 90, "inUsing": False, "satisfying": False, 'size':0.1})
    p1.inventory += i1 - 30

    assert p1.inventory[i1['guid']]['wear'] == 60

    print("Good end test_invt! SUCCESSFUL")


if __name__ == '__main__':
    test_item()
    test_invt()
    print('test_invt success')