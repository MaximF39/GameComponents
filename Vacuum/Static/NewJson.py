import json
import pathlib

# from python.Utils.DotMap import DotMap
import random

from Vacuum.Config.cfg_main import RADIUS_BETWEEN_PLANET

bs = pathlib.Path(__file__).parent.joinpath('Json')
id_parse = ["GalaxyMap"]
guid_parse = ['AmmoParameters', "DeviceParameters", "DroidParameters",
              "EngineParameters", "ShipParameters", "WeaponParameters", "ResourseParameters"]


def _get_path_json(text: str) -> pathlib.Path:
    if text.split('.')[-1] == 'json':
        return bs.joinpath(text)
    else:
        return bs.joinpath(text + '.json')


def new_items():
    guid_parse2 = {"DeviceParameters":4, "DroidParameters": 2, "ResourseParameters":1,
              "EngineParameters":5, "ShipParameters":6, "WeaponParameters":3, "AmmoParameters":3}
    for key, value in guid_parse2.items():
        with open(_get_path_json(key), 'r', encoding='utf-8-sig') as f:
            res = json.loads(f.read())
            for dict_ in res:
                dict_["type"] = value

        with open(_get_path_json(key), 'w', encoding='utf-8-sig') as f:
            json.dump(res, f)

new_items()
def X_sector():
    file_name  = "GalaxyMap"
    with open(_get_path_json(file_name), "r", encoding='utf-8-sig') as f:
        res = json.load(f)


    for d in res:
        count = 0
        for SSO in d['planets']:
            if SSO["class_number"] <= 5:
                SSO.size = random.randint(20000, 30000)
                SSO['Radius'] = 0
                SSO['angle'] = 0
            else:
                count += 1
                SSO['angle'] = random.randint(-4, 12)
                SSO.size = random.randint(8000, 12000)
                SSO['Radius'] = RADIUS_BETWEEN_PLANET * count

    with open(_get_path_json(file_name), "w", encoding='utf-8-sig') as f:
        json.dump(res, f, ensure_ascii=False)

# X_sector()


