import uuid
import copy

class Owner:
    def __init__(self):
        self.inventory = Inventory()

class Inventory(dict):
    """
    Inventory += item
    Inventory -= item # remove item
    Inventory.send_item(Whom, guid, wear=None)
    """
    def __iadd__(self, item_:"item"):
        if 'Inventory' in item_:
            del item_['Inventory'][item_['guid']]
        item_['Inventory'] = self
        add = False
        if item_['stack']:
            for _, my_item in self.items():
                if my_item['classNumber'] == item_['classNumber']:
                    my_item += item_
                    add = True
        if not add:
            self[item_['guid']] = item_
        return self

    def __isub__(self, item_:"item"=None, guid=None):
        if guid and item_:
            raise NotImplementedError("Get item_ and guid")
        if guid:
            item_ = self[guid]
        remove = False
        if item_['stack']:
            for _, my_item in copy.copy(self).items():
                if my_item['classNumber'] == item_['classNumber']:
                    my_item -= item_['wear']
                    remove = True
        if not remove:
            if 'Inventory' in item_:
                del item_['Inventory']
            del self[item_['guid']]
        return self

    def send_item(self, Whom, guid, wear=None):
        if not guid in self:
            return -1
        item_ = self[guid]

        if wear is None:
            Whom.Inventory += item_
            return
        if item_['stack']:
            Whom_item = item_ - wear
            Whom.Inventory += Whom_item


class item(dict):
    """
    item += item
    """
    __slots__ = ('guid', 'classNumber', "stack", "wear", "inUsing", "satisfying")

    def __init__(self, seq=None, **kwargs):
        for need in self.__slots__:
            if not need in seq:
                raise AttributeError(f"{self.__class__.__name__} hasn't attribute %s" % need)
        super().__init__(seq, **kwargs)

    def __iadd__(self, item_:"item"=None, int_=None):
        if isinstance(item_, item) or int_:
            self['wear'] += item_['wear']
            return self

    def __sub__(self, other:int):
        if isinstance(other, int):
            self['wear'] -= other
            if self['stack']:
                if self['wear'] == 0:
                    self['wear'] = other
                    if "Inventory" in self:
                        del self['Inventory'][self['guid']]
                        del self['Inventory']
                    return self
                if self['wear'] > 0:
                    item_ = copy.copy(self)
                    item_['wear'] = other
                    item_['guid'] = uuid.uuid4()
                    if 'Inventory' in item_:
                        del item_['Inventory']
                    return item_
            else:
                return self

""" TEST """
def test():
    """ ADD ITEM """
    p1 = Owner()
    p2 = Owner()

    i1 = item({"guid": uuid.uuid4(), 'classNumber':10, "stack":True, "wear":90, "inUsing":False, "satisfying":False})
    i2 = item({"guid": uuid.uuid4(), 'classNumber': 10, "stack":True, "wear":90, "inUsing":False, "satisfying":False})
    i3 = item({"guid": uuid.uuid4(), 'classNumber': 12, "stack":False, "wear":90, "inUsing":False, "satisfying":False})
    i4 = item({"guid": uuid.uuid4(), 'classNumber': 12, "stack":False, "wear":90, "inUsing":False, "satisfying":False})

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
    i1 = item({"guid": uuid.uuid4(), 'classNumber':10, "stack":True, "wear":180, "inUsing":False, "satisfying":False})

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

    i1 = item({"guid": uuid.uuid4(), 'classNumber': 12, "stack": False, "wear": 90, "inUsing": False, "satisfying": False})
    p1.inventory += i1
    assert p1.inventory[i1['guid']] == i1

    p1.inventory.send_item(p2, guid=p1.inventory[i1['guid']]['guid'])

    assert p1.inventory.__len__() == 0
    assert p2.inventory[i1['guid']] == i1

    ii2 = item({"guid": uuid.uuid4(), 'classNumber': 10, "stack": True, "wear": 80, "inUsing": False, "satisfying": False})

    p1 = Owner()
    p2 = Owner()

    p1.inventory += ii2
    p1.inventory.send_item(p2, guid=ii2['guid'], wear=70)

    assert p1.inventory[ii2['guid']]['wear'] == 10
    for k, v in p2.inventory.items():
        assert v['wear'] == 70

    p1 = Owner()
    ii2 = item({"guid": uuid.uuid4(), 'classNumber': 10, "stack": True, "wear": 80, "inUsing": False, "satisfying": False})
    ii4 = item({"guid": uuid.uuid4(), 'classNumber': 12, "stack": False, "wear": 80, "inUsing": False, "satisfying": False})


    p1.inventory += ii2
    p1.inventory -= ii2
    assert p1.inventory.__len__() == 0

    p1.inventory += ii4
    p1.inventory -= ii4
    assert p1.inventory.__len__() == 0

    p1 = Owner()
    p2 = Owner()
    g = uuid.uuid4()
    o1 = item({"guid": g, 'classNumber': 10, "stack": True, "wear": 80, "inUsing": False, "satisfying": False})
    p1.inventory += o1
    p1.inventory.send_item(p2, guid=g, wear=50)

    assert p1.inventory[o1['guid']]['wear'] == 30
    for _, v in p2.inventory.items():
        assert p2.inventory[v['guid']]['wear'] == 50

    """ CRASH TEST """

    i1 = item({"guid": uuid.uuid4(), 'classNumber': 10, "stack": True, "wear": 90, "inUsing": False, "satisfying": False})
    p = Owner()
    p2 = Owner()
    p.inventory += i1

    p.inventory.send_item(p2, guid=i1['guid'], wear=20)
    assert p.inventory[i1['guid']]['wear'] == 70

    p.inventory += i1
    assert p.inventory[i1['guid']]['wear'] == 70
    assert p2.inventory[i1['guid']]['wear'] == 20

    """ ITEM - WEAR """

    p1 = Owner()
    i1 = item({"guid": uuid.uuid4(), 'classNumber': 10, "stack": False, "wear": 90, "inUsing": False, "satisfying": False})
    p1.inventory += i1
    p1.inventory[i1['guid']] - 30
    assert p1.inventory[i1['guid']]['wear'] == 60

    p1 = Owner()
    i1 = item({"guid": uuid.uuid4(), 'classNumber': 10, "stack": False, "wear": 90, "inUsing": False, "satisfying": False})
    p1.inventory += i1 - 30
    assert p1.inventory[i1['guid']]['wear'] == 60

    print("Good end test! SUCCESSFUL")

test()