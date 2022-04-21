import uuid

from Vacuum.Game.Entity._Back.Player import Player
from Vacuum.Game.Components.Inventory import _Inventory


def test_PlanetInventory():
    player = Player(1000)

    i1 = Item(
        {"guid": uuid.uuid4(), 'class_number': 10, "stack": True, "wear": 900, "inUsing": False, "satisfying": False,
         "size": 5, "cost": 10})
    planet = Planet()

    planet.inventory += i1

    assert player.cash == 1000
    planet.inventory.send_item(player, item_=i1, wear=30)
    assert player.cash == 1000 - 30 * 10

    assert planet.inventory.__len__() == 1
    assert player.inventory.__len__() == 1

    for _, v in player.inventory.copy().items():
        player.inventory.send_item(Whom=planet, item_=v)
    assert player.inventory.__len__() == 0
    assert player.cash == 1000

    player = Player(1000)

    i1 = Item(
        {"guid": uuid.uuid4(), 'class_number': 10, "stack": False, "wear": 90, "inUsing": False, "satisfying": False,
         "size": 5, "cost": 10})
    planet = Planet()

    planet.inventory += i1

    assert player.cash == 1000
    planet.inventory.send_item(player, item_=i1)
    assert player.cash == 990

test_hold_EntityInventory()
exit()
""" TEST """
def test_invt():
    class Owner:
        def __init__(self):
            self.inventory = _Inventory(self)

    """ ADD ITEM """
    p1 = Owner()
    p2 = Owner()

    i1 = Item(
        {"guid": uuid.uuid4(), 'class_number': 10, "stack": True, "wear": 90, "inUsing": False, "satisfying": False, 'size':0.1})
    i2 = Item(
        {"guid": uuid.uuid4(), 'class_number': 10, "stack": True, "wear": 90, "inUsing": False, "satisfying": False, 'size':0.1})
    i3 = Item(
        {"guid": uuid.uuid4(), 'class_number': 12, "stack": False, "wear": 90, "inUsing": False, "satisfying": False, 'size':0.1})
    i4 = Item(
        {"guid": uuid.uuid4(), 'class_number': 12, "stack": False, "wear": 90, "inUsing": False, "satisfying": False, 'size':0.1})

    p2.inventory += i1
    p1.inventory += i1

    assert p1.inventory[i1.guid] == i1
    assert p2.inventory.__len__() == 0

    p1.inventory += i2
    assert p1.inventory[i1.guid].wear == 180

    p1.inventory += i3
    assert p1.inventory[i3.guid].wear == 90

    p1.inventory += i4
    assert p1.inventory[i4.guid].wear == 90

    assert p1.inventory.__len__() == 3

    """ REMOVE ITEM """
    p = Owner()
    i1 = Item(
        {"guid": uuid.uuid4(), 'class_number': 10, "stack": True, "wear": 180, "inUsing": False, "satisfying": False, 'size':0.1})

    p.inventory += i1
    item_ = p.inventory[i1.guid] - 80

    assert item_.guid != i1.guid
    assert p.inventory[i1.guid].wear == 100

    item_2 = p.inventory[i1.guid] - 100

    assert p.inventory.__len__() == 0
    assert item_.wear == 80
    assert item_2.wear == 100

    """ SEND ITEM """

    p1 = Owner()
    p2 = Owner()

    i1 = Item(
        {"guid": uuid.uuid4(), 'class_number': 12, "stack": False, "wear": 90, "inUsing": False, "satisfying": False, 'size':0.1})
    p1.inventory += i1
    assert p1.inventory[i1.guid] == i1

    p1.inventory.send_item(p2, guid=p1.inventory[i1.guid].guid)

    assert p1.inventory.__len__() == 0
    assert p2.inventory[i1.guid] == i1

    ii2 = Item(
        {"guid": uuid.uuid4(), 'class_number': 10, "stack": True, "wear": 80, "inUsing": False, "satisfying": False, 'size':0.1})

    p1 = Owner()
    p2 = Owner()

    p1.inventory += ii2
    p1.inventory.send_item(p2, guid=ii2.guid, wear=70)


    for k, v in p1.inventory.items():
        assert v.wear == 10

    for k, v in p2.inventory.items():
        assert v.wear == 70

    p1 = Owner()
    ii2 = Item(
        {"guid": uuid.uuid4(), 'class_number': 10, "stack": True, "wear": 80, "inUsing": False, "satisfying": False, 'size':0.1})
    ii4 = Item(
        {"guid": uuid.uuid4(), 'class_number': 12, "stack": False, "wear": 80, "inUsing": False, "satisfying": False, 'size':0.1})

    p1.inventory += ii2
    p1.inventory -= ii2
    assert p1.inventory.__len__() == 0

    p1.inventory += ii4
    p1.inventory -= ii4
    assert p1.inventory.__len__() == 0

    p1 = Owner()
    p2 = Owner()
    g = uuid.uuid4()
    o1 = Item({"guid": g, 'class_number': 10, "stack": True, "wear": 80, "inUsing": False, "satisfying": False, 'size':0.1})
    p1.inventory += o1
    p1.inventory.send_item(p2, guid=g, wear=50)

    for _, v in p1.inventory.items():
        assert p1.inventory[v.guid].wear == 30

    for _, v in p2.inventory.items():
        assert p2.inventory[v.guid].wear == 50

    """ CRASH TEST """

    i1 = Item(
        {"guid": uuid.uuid4(), 'class_number': 10, "stack": True, "wear": 90, "inUsing": False, "satisfying": False, 'size':0.1})
    p = Owner()
    p2 = Owner()
    p.inventory += i1

    p.inventory.send_item(p2, guid=i1.guid, wear=20)

    for _, v in p.inventory.items():
        assert p.inventory[v.guid].wear == 70

    p.inventory += i1
    for _, v in p.inventory.items():
        assert p.inventory[v.guid].wear == 70

    for _, v in p2.inventory.items():
        assert p2.inventory[v.guid].wear == 20

    """ ITEM - WEAR """

    p1 = Owner()
    i1 = Item(
        {"guid": uuid.uuid4(), 'class_number': 10, "stack": False, "wear": 90, "inUsing": False, "satisfying": False, 'size':0.1})
    p1.inventory += i1
    p1.inventory[i1.guid] - 30
    assert p1.inventory[i1.guid].wear == 60

    p1 = Owner()
    i1 = Item(
        {"guid": uuid.uuid4(), 'class_number': 10, "stack": False, "wear": 90, "inUsing": False, "satisfying": False, 'size':0.1})
    p1.inventory += i1 - 30

    assert p1.inventory[i1.guid].wear == 60

    print("Good end test_invt! SUCCESSFUL")


def test_const_item():
    from Vacuum.Game.Components.Inventory import _Inventory
    class Owner:
        def __init__(self):
            self.inventory = _Inventory(self)

    i1 = Item(
        {"guid": uuid.uuid4(), 'class_number': 10, "stack": False, "wear": 90, "inUsing": False, "satisfying": False,
         'size': 0.1, 'const':True})

    i1 - 20
    assert i1.wear == 90
    i1 + 20
    assert i1.wear == 90
    i1 += 20
    assert i1.wear == 90
    i1 -= 20
    assert i1.wear == 90


    p1 = Owner()
    p2 = Owner()
    p3 = Owner()
    p1.inventory += i1
    p1.inventory.send_item(p2, guid=i1.guid)

    assert len(p1.inventory) == 1
    assert p2.inventory.__len__() == 1

    for _, item_ in p2.inventory.items():
        s = item_
        assert item_.guid != i1.guid

    p2.inventory.send_item(p3, item_=s)

    assert p2.inventory.__len__() == 0
    assert p3.inventory.__len__() == 1

test_const_item()


def test_item():

    def test_stack_F():
        i1 = Item(
            {"guid": uuid.uuid4(), 'class_number': 10, "stack": False, "wear": 90, "inUsing": False, "satisfying": False, 'size':0.1})

        i1 += 100
        assert i1.wear == 190
        i1 -= 100
        assert i1.wear == 90
        i1 + 100
        assert i1.wear == 190
        i1 - 100
        assert i1.wear == 90

    def test_stack_T():
        i1 = Item(
            {"guid": uuid.uuid4(), 'class_number': 10, "stack": True, "wear": 90, "inUsing": False, "satisfying": False,
             'size': 0.1})

        i1 += 100
        assert i1.wear == 190

        i1 -= 100
        assert i1.wear == 90
        i1 + 100
        assert i1.wear == 190
        i1 - 100
        assert i1.wear == 90

        i2 = i1 - 30
        assert i2.wear == 30
        assert i1.wear == 60

        assert i1.guid != i2.guid

    test_stack_F()
    test_stack_T()



""" TEST """
def test_temporary_effect():
    class Player:
        def __init__(self):
            self.ship = Ship()

    class Ship:
        def __init__(self):
            self.effects = Effects(Owner=self)
            self.speed = 50
            self.basespeed = 50

        def __repr__(self):
            return self.__class__.__name__

    def test_sub_effect():
        p = Player()
        p.ship.effects[1] = 5
        assert p.ship.speed == 100
        p.ship.effects[1] = -3
        time.sleep(2.1)
        assert p.ship.speed == 50

        p = Player()
        p.ship.effects[1] = 5
        assert p.ship.speed == 100
        p.ship.effects[1] = -10
        assert p.ship.speed == 50

    test_sub_effect()

    def test_add_effect():
        P = Player() # default 50 speed
        assert P.ship.speed == 50
        P.ship.effects[1] = 2

        assert P.ship.speed == 100

        time.sleep(2.1)
        assert P.ship.speed == 50

    def test_sum_effect():
        P = Player()
        P.ship.effects[1] = 2
        P.ship.effects[1] = 2

        assert P.ship.speed == 100

        time.sleep(3)
        assert P.ship.speed == 100

        time.sleep(1.1)
        assert P.ship.speed == 50

    test_add_effect()
    test_sum_effect()

def test_const_effect():
    class Player:
        def __init__(self):
            self.ship = Ship()

    class Ship:
        def __init__(self):
            self.effects = Effects(Owner=self)
            self.speed = 50
            self.basespeed = 50

        def __repr__(self):
            return self.__class__.__name__
    """ CONST EFFECT """
    def test_add_effect():
        P = Player()
        P.ship.effects[1] = "const"
        assert P.ship.speed == 100

    def test_remove_effect():
        P = Player()

        P.ship.effects[1] = "const"
        assert P.ship.speed == 100

        P.ship.effects[-1] = "const"
        assert P.ship.speed == 50

    test_add_effect()
    test_remove_effect()

if __name__ == '__main__':
    import threading
    threading.Thread(target=test_temporary_effect).start()
    threading.Thread(target=test_const_effect).start()

