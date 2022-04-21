import math

from Vacuum.Config.cfg_main import RADIUS_BETWEEN_PLANET
from Vacuum.Game.Components.Inventory.LocationInventory import LocationInventory
from Vacuum.Packages.PackageCollector import T_def_set
from Vacuum.Static.Type.Package.T_ServerRequest import T_ServerRequest
from ._Components.PlayerStorage import PlayerStorage
from ._Components.SetSO import SetSO
from ...Utils.Vector2d import Vector2D


class Location(SetSO, PlayerStorage):

    def __init__(self, data):
        super().__init__(data['map_x'], data['map_y'])
        PlayerStorage.__init__(self)
        self.data = data

        self.id = data['id']
        self.Game = data['Game']
        self.map_x = data['map_x']
        self.map_y = data['map_y']
        self.sector = data['sector']

        self.players = []
        self.Planets = []
        self.StaticSpaceObjects = []

        self.inventory = LocationInventory(self)

        self.create_planets()
        self.create_static_space_objects()

    def set(self, Who):
        PlayerStorage.set(self, Who)
        Ship = Who.Ship
        if Ship.target_obj:
            tv2d = self.V2D.substractVectorC(Who.Ship.T_V2D)
            Who.Ship.energy -= math.ceil(Ship.engine.engine.energy_cost * tv2d.length2)

            Ship.V2D = self.get_v2d_to_target_location(Who=Who)

            Who.Location = self
        Ship.setTarget()

        if Who.Location !=  self and Who.Location:
            Who.Location.remove(Who)
        Who.Location = self
        Who.Pack += T_ServerRequest.LOCATION_SYSTEM
        Who.Pack.change_default_set(T_def_set.T_Location)

    def remove(self, Entity):
        PlayerStorage.remove(self, Entity)
        Entity.Location = None
        from Vacuum.Game.Entity._Back.Player import Player
        if isinstance(Entity, Player):
            for player in self.players:
                player.Pack += T_ServerRequest.LOCATION_SYSTEM

    def get_v2d_to_target_location(self, /, Who):
        v2d:Vector2D = Who.Location.V2D.clone().substractVectorC(Who.Ship.T_V2D).getUnitVector()#  getOpositeToNormale
        v2d.multiply((len(self.Planets) - 1) * RADIUS_BETWEEN_PLANET)
        return v2d

    def create_static_space_objects(self):
        from ..SpaceObject import SpaceObject
        for count, staticSpaceObject_data in enumerate(self.data['staticSpaceObjects']):
            staticSpaceObject_data['x'] = RADIUS_BETWEEN_PLANET // 3 * count - 1000
            staticSpaceObject_data['y'] = RADIUS_BETWEEN_PLANET // 3 * count - 1000
            staticSpaceObject_data['Location'] = self
            SPO = SpaceObject(staticSpaceObject_data['type'], staticSpaceObject_data)
            setattr(self, f"StaticSpaceObject_{staticSpaceObject_data['id']}", SPO)
            self.StaticSpaceObjects.append(SPO)

    def create_planets(self):
        from ..SpaceObject import SpaceObject
        from ..T_SpaceObject import T_SpaceObject
        for count, planet_data in enumerate(self.data['planets']):
            v2d = Vector2D()
            v2d.setMembersByRA(planet_data['Radius'], planet_data['angle'])
            planet_data['x'] = v2d.x
            planet_data['y'] = v2d.y
            planet_data['Location'] = self
            Planet = SpaceObject(T_SpaceObject.T_Planet, planet_data)
            self.Planets.append(Planet)

            setattr(self, f"Planet_{planet_data['id']}", Planet)