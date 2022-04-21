import json
import pathlib

from Vacuum.Static.Type.Keys import Keys

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

def item_CN(CN, wear=None, const=False, level = 0, inUsing=False):
    for file_name in __items_parse:
        with open(_get_path_json(file_name), 'r', encoding='utf-8-sig') as f:
            res = json.loads(f.read())
            for data_item in res:
                if data_item[Keys.class_number] == CN:
                    data_item[Keys.wear] = wear
                    data_item["const"] = const
                    data_item["level"] = level
                    data_item["inUsing"] = inUsing

                    return data_item

def ship_CN(CN):
    for file_name in __ship:
        with open(_get_path_json(file_name), 'r', encoding='utf-8-sig') as f:
            res = json.loads(f.read())
            for data_item in res:
                if data_item[Keys.class_number] == CN:
                    return data_item
