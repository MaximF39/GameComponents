from Entity.Player import Player
from SpaceObjects.Components.Set import Set
from Static.Type.Package.T_ServerRequest import T_ServerRequest


class EntityStorage(Set):
    players: list

    def __init__(self, data, Location):
        super().__init__(data['x'], data['y'])
        self.Location = Location

    def set(self, Whom):
        Whom.SpaceObject = self
        if isinstance(Whom, Player):
            self.players.append(Whom)

    def remove(self, Whom):
        Whom.SpaceObject = None
        if isinstance(Whom, Player):
            self.players.remove(Whom)


