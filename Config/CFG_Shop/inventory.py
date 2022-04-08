from python.Game.Game.SpaceObjects import item
from python.Static.Type.Item.T_Item import T_Item
from python.Static.Type.T_Race import T_Race


def get_default_items(race, OwnerClass, Game):
    return (item(class_number=item_classNumber, Game=Game, wear=wear, OwnerClass=OwnerClass) for item_classNumber in get_shop_by_race[race])

wear = 1000

green_shop_items = (
        T_Item.AnidRezak,
        T_Item.AnidUnzipper,
        T_Item.Turbo,
        T_Item.Processor,
        T_Item.Nitrinium,
        T_Item.AnidEngine,
        T_Item.AnidEngine2,
        T_Item.AnidMiner,
        T_Item.AnidInfantry,
        T_Item.AnidArmored,
        T_Item.ATrash,
    )
blue_shop_items = (
        T_Item.LaserGun,
        T_Item.Battery,
        T_Item.MedramillUnzipper,
        T_Item.Shield,
        T_Item.Energon,
        T_Item.MAntiFazer,
        T_Item.RepairDroid,
        T_Item.MRepair2,
        T_Item.MedramillEngine,
        T_Item.MedramillEngine2,
        T_Item.MedramilMiner,
        T_Item.MedramillInfantry,
        T_Item.MedramillArmored,
        T_Item.MTrash,
    )
red_shop_items = (
        T_Item.OmolenianRezak,
        T_Item.OmolenianUnzipper,
        T_Item.Generator,
        T_Item.Damage,
        T_Item.Armor,
        T_Item.Phaser,
        T_Item.OmolenianEngine,
        T_Item.OmolenianEngine2,
        T_Item.OmolenianEngine3,
        T_Item.OmolenianMiner,
        T_Item.OmolenianInfantry,
        T_Item.OmolenianArmored,
        T_Item.OTrash,
    )
yellow_shop_items = (
        T_Item.Jalo,
        T_Item.IrritianUnzipper,
        T_Item.Aglu,
        T_Item.Repair,
        T_Item.MetaController,
        T_Item.IrritianEngine,
        T_Item.IrritianEngine2,
        T_Item.IrritianMiner,
        T_Item.IrritianInfantry,
        T_Item.IrritianArmored,
        T_Item.ITrash,
)

get_shop_by_race = {
T_Race.OMOLENIAN_ID: red_shop_items, #OMOLENIAN_ID
T_Race.IRRIITIAN_ID: yellow_shop_items, #IRRIITIAN_ID
T_Race.ANID_ID: green_shop_items, #ANID_ID
T_Race.MEDRAMIL_ID: blue_shop_items, #MEDRAMIL_ID
}

