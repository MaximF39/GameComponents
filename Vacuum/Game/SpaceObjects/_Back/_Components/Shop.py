from Vacuum.Config.CFG_Shop.cfg_shop_type import inventory_shop, update_resources, update_ship, ginetic_lab, \
    repository, ship_factory
from Vacuum.Game.Components.Inventory.PlanetInventory import PlanetInventory
from Vacuum.Game.SpaceObjects._Back.Type.T_Shop import T_Shop


class Shop:

    def __init__(self, data):
        self.type_ = list()
        id_ = data['id']

        if id_ in inventory_shop:
            self.type_.append(T_Shop.InventoryShop)
            self.inventory = PlanetInventory(self)
        if id_ in update_resources:
            self.type_.append(T_Shop.UpdateResources)
        if id_ in update_ship:
            self.type_.append(T_Shop.UpdateShips)
        if id_ in ginetic_lab:
            self.type_.append(T_Shop.GineticLab)
        if id_ in ship_factory:
            self.type_.append(T_Shop.ShipFactory)
        if id_ in repository:
            self.type_.extend([T_Shop.Repository, T_Shop.ClanRepository, T_Shop.Angar])

    def type_entry(self, type_):
        return type_ in self.type_