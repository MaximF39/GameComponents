from Inventory.Items.Item import Item


class Droid(Item):

    def use(self):
        super().use()
        self['inventory'].Owner.Ship.droids += self


    def unuse(self):
        super().unuse()
        self['inventory'].Owner.Ship.droids -= self



