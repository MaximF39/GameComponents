from Vacuum.Game.Entity.T_Entity import T_Entity
from ._Back.Mob import Mob
from ._Back.Player import Player


def Entity(entity_id, data):
    match entity_id:
        case T_Entity.T_Player:
            return Player(data)
        case T_Entity.T_Mob:
            return Mob(data)