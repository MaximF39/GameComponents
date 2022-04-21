from ._Back.Arena import Arena
from ._Back.Asteroid import Asteroid
from ._Back.AsteroidBelt import AsteroidBelt
from ._Back.Hive import Hive
from ._Back.Location import Location
from ._Back.Planet import Planet
from ._Back.PlanetBattle import PlanetBattle
from ._Back.Portal import Portal
from ._Back.RepositoryStation import RepositoryStation
from Vacuum.Game.SpaceObjects.T_SpaceObject import T_SpaceObject


def SpaceObject(T_spaceObject, data):
    match T_spaceObject:
        case T_SpaceObject.T_Location:
            return Location(data)
        case T_SpaceObject.T_Planet:
            return Planet(data)
        case T_SpaceObject.T_RepositoryStation:
            return RepositoryStation(data)
        case T_SpaceObject.T_Portal:
            return Portal(data)
        case T_SpaceObject.T_AsteroidBelt:
            return AsteroidBelt(data)
        case T_SpaceObject.T_Asteroid:
            return Asteroid(data)
        case T_SpaceObject.T_Arena:
            return Arena(data)
        case T_SpaceObject.T_PlanetBattle:
            return PlanetBattle(data)
        case T_SpaceObject.T_Hive:
            return Hive(data)