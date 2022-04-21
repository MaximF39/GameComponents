from Vacuum.Game.Entity._Back.Player import Player
from Vacuum.Game.SpaceObjects._Back._Components.PlayerStorage import PlayerStorage
from Vacuum.Static.Type.Package.T_ServerRequest import T_ServerRequest


class Battle(PlayerStorage):

    def __init__(self, data):
        super().__init__()
        self.__dict__.update(data)
