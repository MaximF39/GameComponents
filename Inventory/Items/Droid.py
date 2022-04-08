from Inventory.Items.Item import Item


class Droid(Item):

    def use(self):
        super().use()
        self['inventory'].Owner.ship.droids += self


    def unuse(self):
        super().unuse()
        self['inventory'].Owner.ship.droids -= self



