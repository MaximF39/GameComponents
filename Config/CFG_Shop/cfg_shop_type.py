from python.Config.CFG_Shop.ships import weak_system, medium_system, strong_system
from python.Static.Type.SpaceObject.T_Shop import T_Shop

default_shop = [*weak_system, *medium_system, *strong_system] # system

default_type = [T_Shop.InventoryShop, T_Shop.ShipFactory]

repository = [T_Shop.Repository, T_Shop.Angar, T_Shop.ClanRepository]

improve_resources = [118]
improve_ship = [93]
ginetic_lab_planet_id = [92]
