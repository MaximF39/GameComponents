from Vacuum.Game.Items._Back._Item import _Item


class Engine(_Item):

    def use(self):
        print("seeeeeeeeeeeeeeeeeeeee")
        super().use()
        self.inventory.Owner.Ship.engine.replace(self)

    def unuse(self):
        super().unuse()
        self.inventory.Owner.inventory += self