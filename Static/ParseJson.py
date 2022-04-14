import json
import pathlib

from Static.Type.Keys import Keys

bs = pathlib.Path(__file__).parent.joinpath('Json')
__id_parse = ['DB_Clan', "GalaxyMap"]
__items_parse = ["DeviceParameters", "DroidParameters",
              "EngineParameters", "WeaponParameters", "ResourseParameters"]

__ship = ["ShipParameters"]

def _get_path_json(text: str) -> pathlib.Path:
    if text.split('.')[-1] == 'json':
        return bs.joinpath(text)
    else:
        return bs.joinpath(text + '.json')

def item_CN(CN, wear=None):
    for file_name in __items_parse:
        with open(_get_path_json(file_name), 'r', encoding='utf-8-sig') as f:
            res = json.loads(f.read())
            for item in res:
                if item[Keys.class_number] == CN:
                    item[Keys.wear] = wear
                    print("I send", item)
                    return item

def ship_CN(CN):
    for file_name in __ship:
        with open(_get_path_json(file_name), 'r', encoding='utf-8-sig') as f:
            res = json.loads(f.read())
            for item in res:
                if item[Keys.class_number] == CN:
                    return item
