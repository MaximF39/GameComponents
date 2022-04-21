import os

from Vacuum.Config.CFG_Entity.CFG_Player.cfg_db_player import default_data_player
from Vacuum.Config.cfg_main import folder_players
from Vacuum.Game.Entity.Entity import Entity
from Vacuum.Game.Entity.T_Entity import T_Entity
from Vacuum.Game.SpaceObjects.SpaceObject import SpaceObject
from Vacuum.Game.SpaceObjects.T_SpaceObject import T_SpaceObject
from Vacuum.Static.ParseJson import parse_xml


class StarWars:
    id_to_conn = {}
    def __init__(self, Server):
        self.Server = Server
        self.__create_game()

    def __create_game(self):
        self.__create_locations()

    def connect_user(self, id_, conn):
        self.id_to_conn[id_] = conn

    def create_player(self, id_, login):
        players_id = tuple(map(int, os.listdir(folder_players)))
        if id_ in players_id:
            import pickle
            with open(folder_players + id_, 'rb') as f:
                Player = pickle.load(f)
                Player.StarWars = self
                setattr(self, f"Player_{id_}", Player)
        else:
            player_ = default_data_player.copy()
            player_['id'] = id_
            player_['Game'] = self
            player_['login'] = login
            setattr(self, f"Player_{id_}", Entity(T_Entity.T_Player, player_))
        return getattr(self, f"Player_{id_}")

    def __create_locations(self):
        for location in parse_xml('GalaxyMap'):
            id_ = location['id']
            location['Game'] = self
            setattr(self, f"Location_{id_}", SpaceObject(T_SpaceObject.T_Location, location))

    def __create_mobs(self):
        """ CREATE KUYNA AND BASS """
        for mob in mobs:
            setattr(self, f"Mob_{mob.id}", Entity(T_Entity.T_Mob, mob))