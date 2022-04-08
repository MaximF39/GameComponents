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

def parse_xml(file_name) -> list:
    with open(_get_path_json(file_name), 'r', encoding='utf-8-sig') as f:
        res = json.loads(f.read())
        return res

def item_id(id_, wear=None):
    for file_name in __items_parse:
        with open(_get_path_json(file_name), 'r', encoding='utf-8-sig') as f:
            res = json.loads(f.read())
            for item in res:
                if item[Keys.class_number] == id_:
                    item[Keys.wear] = wear
                    return item

def ship_id(id_):
    for file_name in __ship:
        with open(_get_path_json(file_name), 'r', encoding='utf-8-sig') as f:
            res = json.loads(f.read())
            for item in res:
                if item[Keys.class_number] == id_:
                    return item
