from Vacuum.Packages.PackagesManager import PackagesManager
from Vacuum.Static.Type.Package.T_ServerRequest import T_ServerRequest


class PackageCollector(set):
    all = []
    Player: "Player"

    def __new__(cls, seq=(), **kwargs):
        return super().__new__(cls, seq)

    def __init__(self, seq=(), **kwargs):
        super().__init__(seq)
        self.__dict__.update(kwargs)
        self.all.append(self)
        self.default_set:set = set()
        self.Pack = PackagesManager(self.Player)

    def send(self):
        for PackNumber in self.default_set:
            self.__send_pack((PackNumber,))
        self.clear()

    def change_default_set(self, T_def_set_):
        match T_def_set_:
            case T_def_set.T_AsteroidBelt:
                self.default_set = {T_ServerRequest.SHIPS_STASE, T_ServerRequest.SHIPS_POSITION, T_ServerRequest.ASTEROIDS}
            case T_def_set.T_Battle:
                self.default_set = {T_ServerRequest.SHIPS_STASE, T_ServerRequest.SHIPS_POSITION}
            case T_def_set.T_SpaceObject:
                self.default_set = {T_ServerRequest.SHIPS_STASE,}
            case T_def_set.T_Location:
                self.default_set = {T_ServerRequest.SHIPS_STASE, T_ServerRequest.SHIPS_POSITION}

    def __iadd__(self, PackNumber):
        if isinstance(PackNumber, int | dict):
            self.__default_add(PackNumber)
            return self

        elif isinstance(PackNumber, tuple | list):
            for pack in PackNumber:
                self.__default_add(pack)
            return self
        raise NotImplementedError("PackNumber type", type(PackNumber))

    def __default_add(self, PackNumber):
        if isinstance(PackNumber, int):
            self.__send_pack((PackNumber,))

        if isinstance(PackNumber, dict):
            for k, v in PackNumber.items():
                self.__send_pack((k, v))

    def __send_pack(self, PackNumber):
        self.Pack.processPackages(*PackNumber)

class T_def_set:
    T_AsteroidBelt = 1
    T_Battle = 2
    T_SpaceObject = 3
    T_Location = 4