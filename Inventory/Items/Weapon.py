from Inventory.Items.Item import Item


class Weapon(Item):

    def use(self):
        super().use()
        self['inventory'].Owner.Ship.cpuUsed += 20

    def unuse(self):
        super().unuse()
        self['inventory'].Owner.Ship.cpuUsed -= 20