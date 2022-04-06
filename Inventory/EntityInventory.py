import uuid

from Inventory.B_Inventory import B_Inventory, Item

class Hold(int):

    def __new__(cls, *args, **kwargs):
        hold = args[0]
        cls.max = args[1]
        return super().__new__(cls, hold)

    def __new(self, hold):
        if hold > self.max:
            raise NotImplementedError('hold > maxHold')
        return Hold(hold, self.max)

    def __iadd__(self, other):
        return self.__new(self.__add__(other))

    def __isub__(self, other):
        return self.__new(self.__sub__(other))

class EntityInventory(B_Inventory):

    def __init__(self, Owner, maxHold):
        self.hold = Hold(0, maxHold)
        super().__init__(Owner)

    def __iadd__(self, item_):
        self.hold += item_.get_size()
        return super().__iadd__(item_)

    def __isub__(self, item_):
        self.hold -= item_.get_size()
        return super().__isub__(item_)

    def send_item(self, Whom, guid=None, wear=None, item_=None):
        item_ = self._get_item(guid, item_)
        self.hold -= item_.get_size(wear)
        super().send_item(Whom, wear=wear, item_=item_)

def test():
    class Player:

        def __init__(self, maxHold=5000):
            self.inventory = EntityInventory(self, maxHold)

    p1 = Player(maxHold=5000)
    p2 = Player()
    assert p1.inventory.hold.max

    i1 = Item(
        {"guid": uuid.uuid4(), 'classNumber': 10, "stack": True, "wear": 90, "inUsing": False, "satisfying": False, "size": 5})

    p1.inventory += i1
    assert p1.inventory.hold == 450

    p1.inventory.send_item(p2, guid=i1['guid'], wear=40)

    print(p1.inventory.hold)
    assert p1.inventory.hold == 250
    assert p2.inventory.hold == 200

if __name__ == '__main__':
    test()