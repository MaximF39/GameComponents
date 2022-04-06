import uuid

from Inventory.B_Inventory import B_Inventory, Item
from Inventory.EntityInventory import EntityInventory


class PlanetInventory(B_Inventory):

    def __iadd__(self, item_):
        if 'inventory' in item_:
            item_['inventory'].Owner.cash += item_.get_cost()
        super().__iadd__(item_)
        return self

    def send_item(self, Whom, guid=None, wear=None, item_=None):
        item_ = self._get_item(guid, item_)
        Whom.cash -= item_.get_cost(wear)
        super().send_item(Whom, item_=item_, wear=wear)

    def const_item(self, inventory):
        pass

class ConstInventory(B_Inventory):

    def __isub__(self, item_):
        return super().__isub__(item_)

class Planet:

    def __init__(self):
        self.inventory = PlanetInventory(self)

def test():
    class Player:
        cash = 1000

        def __init__(self, maxHold=10):
            self.inventory = EntityInventory(self, maxHold)

    player = Player(1000)

    i1 = Item(
        {"guid": uuid.uuid4(), 'classNumber': 10, "stack": True, "wear": 900, "inUsing": False, "satisfying": False,
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
        {"guid": uuid.uuid4(), 'classNumber': 10, "stack": False, "wear": 90, "inUsing": False, "satisfying": False,
         "size": 5, "cost": 10})
    planet = Planet()

    planet.inventory += i1

    assert player.cash == 1000
    planet.inventory.send_item(player, item_=i1)
    assert player.cash == 990

if __name__ == '__main__':
    test()