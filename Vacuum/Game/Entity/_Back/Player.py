from Vacuum.Config.cfg_main import folder_players
from Vacuum.Game.Components.Inventory.PlayerInventory import PlayerInventory
from Vacuum.Game.Entity._Back.Components.Skills import Skills
from Vacuum.Game.Entity._Back.Components.Cash import Cash
from Vacuum.Game.Entity._Back.Components.EXP_STAT import Experience, Status

from Vacuum.Game.Entity._Back.__Entity import __Entity

from Vacuum.Packages.PackageCollector import PackageCollector
from Vacuum.Static.Type.Package.T_ServerRequest import T_ServerRequest


class Player(__Entity):

    def __init__(self, data):
        super().__init__(data)
        self.Location = getattr(self.Game, f"Location_{self.Location}")
        self.Pack = PackageCollector(Player=self)
        self.inventory = PlayerInventory(self)
        self.clicked = 0
        self.skills = Skills()
        self.cash = Cash(self.cash, Player=self)
        self.exp = Experience(self.exp, Player=self)
        self.status = Status(self.status, Player=self)
        self.Ship.init()
        self.entry()

    def entry(self):
        super().entry()



    def __del__(self):
        import pickle
        with open(folder_players + str(self.id), 'wb') as f:
            pickle.dump(self, f)
        self.Location.remove(self)
        if self.SpaceObject:
            self.SpaceObject.remove(self)
        if self.Battle:
            self.Battle.remove(self)
            self.Battle = None
