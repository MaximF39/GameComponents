from Vacuum.Game.Items._Back._Item import _Item


class Droid(_Item):

    def use(self):
        super().use()
        self.inventory.Owner.Ship.droids += self


    def unuse(self):
        super().unuse()
        self.inventory.Owner.Ship.droids -= self



