import random
import threading

from Vacuum.Game.Components.Heal_A_Energ import Health
from Vacuum.Game.Components.MovableSpaceObject import MovableSpaceObject
from Vacuum.Game.Utils.Vector2d import Vector2D


class Asteroid(MovableSpaceObject):
    IronOre: int = 49
    TitanOre: int = 51
    GoldOre: int = 53
    OsmiumOre: int = 55
    Minerals: int = 131
    Organic: int = 132
    R = 3000
    coef = {
        49: 1,
        51: 0.45,
        53: 0.2,
        55: 0.1,
        131: 0.3,
        132: 0.2
    }

    def __init__(self, data):
        self.__dict__.update(data)

        self.health = Health(random.randint(600, 3000))
        self.speed = 60 - self.health // 100
        super().__init__(0, 0)
        self.V2D.setMembersByRA(self.R, random.randint(0, 360))
        self.T_V2D = Vector2D()
        self.T_V2D.setMembersByRA(self.R, random.randint(0, 360))
        threading.Timer(self.V2D.distance(self.T_V2D) / self.speed, self.AsteroidBelt.remove_asteroid, args=(self,)).start()

    def get_coord(self):
        pass

    def drop(self, PlayerKill):
        item_dict = {}
        item_dict['count'] = int(self.size * self.coef[self.type_ore] * (random.randint(90, 110) / 100) * ((100 + PlayerKill.skills['Mining'] ** 1.2) / 100))
        ore = item()

        PacMan = PackagesManager(PlayerKill.id, self.Game)
        PacMan.locationBattle()
        PacMan.items()

    def end_target(self):
        self.AsteroidsBelt.remove_asteroid(self)

    def get_damage(self, damage):
        self.size -= damage
        if 0 >= self.size:
            # self.drop()
            print('kill asteroid')
