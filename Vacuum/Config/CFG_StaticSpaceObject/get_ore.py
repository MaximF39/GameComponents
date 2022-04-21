
IronOre: int = 49
TitanOre: int = 51
GoldOre: int = 53
OsmiumOre: int = 55
Minerals: int = 131
Organic: int = 132

iron_ore = [2, 8, 46, 43,]
titan_ore = [3, 6, 45, 30, 39, 104, 102, 103, 101, 47]
gold_ore = [32, 10, 44, 119, 124]
osmium_ore = [10]
minerals = [9, 110, 26]
organic = [116, 5,]


def get_ore(id_location):
    if id_location in iron_ore:
        return IronOre
    if id_location in titan_ore:
        return TitanOre
    if id_location in gold_ore:
        return GoldOre
    if id_location in osmium_ore:
        return OsmiumOre
    if id_location in minerals:
        return Minerals
    if id_location in organic:
        return Organic
