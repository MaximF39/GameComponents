from Vacuum.Game.Components.Inventory.EntityInventory import EntityInventory


class PlayerInventory(EntityInventory):

    def __init__(self, Player):
        super().__init__(Player)

