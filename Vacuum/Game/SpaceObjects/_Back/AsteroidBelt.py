from Vacuum.Packages.PackageCollector import T_def_set
from Vacuum.Static.Type.Package.T_ServerRequest import T_ServerRequest
from .Asteroid import Asteroid
from ._Components.Battle import Battle
from ._Components.SetSO import SetSO


class AsteroidBelt(Battle, SetSO):
    id: int
    max_asteroid_id = 0
    asteroids = []
    entry_count_asteroid = 60
    # cnt_asteroid: int

    def __init__(self, data: dict):
        super().__init__(data)
        SetSO.__init__(self, data['x'], data['y'])
        self.id = data['id']
        self.create_asteroid()

    def create_asteroid(self, cnt=60):
        for i in range(cnt):
            self.max_asteroid_id += 1
            data = {"AsteroidBelt": self, "id":self.max_asteroid_id}
            self.asteroids.append(Asteroid(data))


    def set(self, Whom):
        Battle.set(self, Whom)
        Whom.Pack.change_default_set(T_def_set.T_AsteroidBelt)
        Whom.Location.remove(Whom)
        Whom.Location = self
        Whom.return_space_object = Whom.Ship.target_obj
        Whom.Ship.setTarget()
        Whom.Pack += T_ServerRequest.LOCATION_BATTLE

    def remove(self, Whom):
        Battle.remove(self, Whom)
        Whom.Ship.setTarget(Whom.return_space_object.V2D)
        Whom.Location = None
        Whom.return_space_object.Location.set(Whom)

    def remove_asteroid(self, AsteroidClass):
        for Aster in self.asteroids:
            if Aster == AsteroidClass:
                self.asteroids.remove(AsteroidClass)
                # self.create_asteroid(1)


