from Entity.Player import Player
from SpaceObjects.Components.EntityStorage import EntityStorage
from Static.Type.Package.T_ServerRequest import T_ServerRequest


class BigObject(EntityStorage):

    def set(self, Whom):
        super().set(Whom)
        if isinstance(Whom, Player):
            for p in self.players:
                p.Pack += T_ServerRequest.LOCATION_PLANET

    def remove(self, Whom):
        super().remove(Whom)
        Whom.Pack += T_ServerRequest.LOCATION_SYSTEM
        if isinstance(Whom, Player):
            for p in self.players:
                p.Pack += T_ServerRequest.LOCATION_PLANET