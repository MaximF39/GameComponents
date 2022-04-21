from Vacuum.Game.Entity._Back.Player import Player
from Vacuum.Game.SpaceObjects._Back._Components.PlayerStorage import PlayerStorage
from Vacuum.Packages.PackageCollector import T_def_set
from Vacuum.Static.Type.Package.T_ServerRequest import T_ServerRequest


class BigObject(PlayerStorage):

    def __init__(self, data):
        super().__init__()
        self.__dict__.update(data)

    def set(self, Whom):
        super().set(Whom)
        Whom.SpaceObject = self
        Whom.Ship.setTarget()
        Whom.Pack += T_ServerRequest.LOCATION_PLANET
        Whom.Pack.change_default_set(T_def_set.T_SpaceObject)
        Whom.Location.remove(self)

    def remove(self, Whom):
        super().remove(Whom)
        Whom.SpaceObject = None
        Whom.Pack += T_ServerRequest.LOCATION_SYSTEM
        Whom.Pack.change_default_set(T_def_set.T_Location)


    def get_coord(self):
        return self.x, self.y
