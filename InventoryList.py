import uuid
import copy

class Owner:
    def __init__(self):
        self.inventory = Inventory()

class Inventory(list):
    def get_item(self, guid:str):
        for item_ in self:
            if item_['guid'] == guid:
                return item_

    def __iadd__(self, item_:"item"):
        if 'Inventory' in item_:
            item_['Inventory'].remove(item_)
        item_['Inventory'] = self
        add = False
        if item_['stack']:
            for my_item in self:
                if my_item['classNumber'] == item_['classNumber']:
                    my_item += item_
                    add = True
        if not add:
            self.extend([item_])
        return self

    def __isub__(self, item_:"item"):
        remove = False
        if item_['stack']:
            for my_item in self:
                if my_item['classNumber'] == item_['classNumber']:
                    my_item -= item_['wear']
                    remove = True
        if not remove:
            if 'Inventory' in item_:
                del item_['Inventory']
            super().remove(item_)
        return self

    def send_item(self, Whom, item_=None, wear=None, guid=None):
        if not item_ and not guid:
            raise NotImplementedError('not guid or item')
        if guid:
            item_ = self.get_item(guid)
        if item_ in self:
            if wear is None:
                Whom.Inventory += item_
                return
            if item_['stack']:
                Whom_item = item_ - wear
                Whom.Inventory += Whom_item


class item(dict):
    __slots__ = ('guid', 'classNumber', "stack", "wear", "inUsing", "satisfying")

    def __init__(self, seq=None, **kwargs):
        for need in self.__slots__:
            if not need in seq:
                raise AttributeError(f"{self.__class__.__name__} hasn't attribute %s" % need)
        super().__init__(seq, **kwargs)

    def __sub__(self, other:int):
        if isinstance(other, int):
            if self['stack']:
                self['wear'] -= other
                if self['wear'] > 0 and not self['stack']:
                    raise Exception("У не стэка отняли часть")
                if self['wear'] >= 0:
                    item_ = copy.copy(self)
                    item_['wear'] = other
                    item_['guid'] = uuid.uuid4()
                    if 'Inventory' in item_:
                        del item_['Inventory']
                    if self['wear'] == 0:
                        if "Inventory" in self:
                            self['Inventory'].remove(self)
                    return item_
            else:
                self['wear'] -= other

    def __iadd__(self, item_:"item"):
        if isinstance(item_, item):
            self['wear'] += item_['wear']
            return self


""" TEST """
def test():
    """ ADD ITEM """
    Player = Owner()
    Player2 = Owner()
    i = uuid.uuid4()
    i1 = item({"guid": i, 'classNumber':10, "stack":True, "wear":90, "inUsing":False, "satisfying":False})
    i2 = item({"guid": uuid.uuid4(), 'classNumber': 10, "stack":True, "wear":90, "inUsing":False, "satisfying":False})
    i3 = item({"guid": uuid.uuid4(), 'classNumber': 12, "stack":False, "wear":90, "inUsing":False, "satisfying":False})
    i4 = item({"guid": uuid.uuid4(), 'classNumber': 12, "stack":False, "wear":90, "inUsing":False, "satisfying":False})

    Player2.inventory += i1
    Player.inventory += i1

    assert Player.inventory[0] == i1
    assert Player2.inventory.__len__() == 0

    Player.inventory += i2
    Player.inventory += i3
    Player.inventory += i4

    assert Player.inventory.get_item(i1['guid'])['wear'] == 180
    assert Player.inventory.get_item(i3['guid'])['wear'] == 90
    assert Player.inventory.get_item(i4['guid'])['wear'] == 90
    assert Player.inventory.__len__() == 3

    """ REMOVE ITEM """

    item_ = Player.inventory.get_item(i1['guid']) - 80
    assert item_['guid'] != i1['guid']
    assert Player.inventory.get_item(i1['guid'])['wear'] == 100
    item_2 = Player.inventory.get_item(i1['guid']) - 100
    assert Player.inventory.get_item(i1['guid']) is None
    assert item_['wear'] == 80
    assert item_2['wear'] == 100
    item_3 = Player.inventory.get_item(i3['guid']) - i3['wear']
    assert Player.inventory.get_item(i3['guid']) is None

    try:
        flag = True
        Player.inventory.get_item(i4['guid']) - (i4['wear'] - 10)
        flag = False
    except Exception as e:
        assert flag

    Player1 = Owner()
    Player2 = Owner()

    i1 = item({"guid": uuid.uuid4(), 'classNumber': 12, "stack": False, "wear": 90, "inUsing": False, "satisfying": False})
    Player1.inventory += i1
    assert Player1.inventory.get_item(i1['guid']) == i1

    Player1.inventory.send_item(Player2, Player1.inventory.get_item(i1['guid']))

    assert Player1.inventory.__len__() == 0
    assert Player2.inventory.get_item(i1['guid']) == i1

    ii2 = item({"guid": uuid.uuid4(), 'classNumber': 10, "stack": True, "wear": 80, "inUsing": False, "satisfying": False})

    Player1 = Owner()
    Player2 = Owner()

    Player1.inventory += ii2
    ii0 = ii2 - 70
    Player2.inventory += ii0

    assert Player1.inventory[0]['wear'] == 10
    assert Player2.inventory[0]['wear'] == 70

    Player1 = Owner()
    ii2 = item({"guid": uuid.uuid4(), 'classNumber': 10, "stack": True, "wear": 80, "inUsing": False, "satisfying": False})
    ii4 = item({"guid": uuid.uuid4(), 'classNumber': 12, "stack": False, "wear": 80, "inUsing": False, "satisfying": False})


    Player1.inventory += ii2
    Player1.inventory -= ii2
    assert Player1.inventory.__len__() == 0

    Player1.inventory += ii4
    Player1.inventory -= ii4
    assert Player1.inventory.__len__() == 0

    """ SEPARATION ITEM """

    Player1 = Owner()
    Player2 = Owner()
    g = uuid.uuid4()
    o1 = item({"guid": g, 'classNumber': 10, "stack": True, "wear": 80, "inUsing": False, "satisfying": False})
    Player1.inventory += o1
    Player1.inventory.send_item(Player2, guid=g, wear=50)

    assert Player1.inventory[0]['wear'] == 30
    assert Player2.inventory[0]['wear'] == 50

    """ CRASH TEST """
    i1 = item({"guid": uuid.uuid4(), 'classNumber': 10, "stack": True, "wear": 90, "inUsing": False, "satisfying": False})

    p = Owner()
    p2 = Owner()

    p.inventory += i1
    p.inventory.send_item(p2, i1, wear=20)

    assert p.inventory[0]['wear'] == 70
    assert p2.inventory[0]['wear'] == 20

    p.inventory += i1

    assert p.inventory[0]['wear'] == 70
    assert p2.inventory[0]['wear'] == 20

    p2.inventory += i1

    assert p.inventory[0]['wear'] == 90
    assert p2.inventory.__len__() == 0

    print("Good end test! SUCCESSFUL")