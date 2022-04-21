from Vacuum.Game.Items.T_Item import T_Item
from ._Back.Device import Device
from ._Back.Droid import Droid
from ._Back.Engine import Engine
from ._Back.Resource import Resource
from ._Back.Ship import Ship
from ._Back.Weapon import Weapon
from ...Static.ParseJson import item_CN, ship_CN


def Item(CN, wear=1000, const=False, level=0, isShip=False, inUsing=False):
    if isShip:
        data = ship_CN(CN)
        return Ship(data)

    data = item_CN(CN, wear, const, level, inUsing)
    match data["type"]:
        case T_Item.Resource_id | T_Item.Ammo_id:
            return Resource(data)
        case T_Item.Droid_id:
            return Droid(data)
        case T_Item.Weapon_id:
            return Weapon(data)
        case T_Item.Device_id:
            return Device(data)
        case T_Item.Engine_id:
            return Engine(data)



