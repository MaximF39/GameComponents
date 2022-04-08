import random

from python.Static.Type.T_Aliance import T_Aliance
from python.Static.Type.Item.T_Weapon import T_Weapon
from python.Static.Type.Mob.T_Mob import T_Mob
from python.Static.Type.T_Race import T_Race
from python.Static.Type.Item.T_Ship import T_Ship
from python.Static.Type.Item.T_Item import T_Item
from python.Static.Type.T_PlayerSkill import T_PlayerSkill
from python.Static.Type.SpaceObject.SystemsName import systems_name

RADIUS_FROM_CENTER = 1500

name = 'strong mob for Astra'
# 1 - weak, 2 - middle, 3 -strong
# 105, 106, 107 - weak(green)
# 6, 8, 38 - middle(green)
# 68 - strong(green)

ship_weak = [T_Ship.OIntercepter, T_Ship.OTransport, T_Ship.OSience, T_Ship.OIndustrial],
ship_middle = [T_Ship.OCruiser, T_Ship.OLinkor, T_Ship.OFregat, T_Ship.OShockBrig, T_Ship.OSiegeBrig]
ship_strong = [T_Ship.OScout, T_Ship.OSiegeLinkor, T_Ship.OPalaven]

__devices_little = [T_Item.Battery, T_Item.Damage, T_Item.RepairDroid, T_Item.Turbo, T_Item.Shield, T_Item.KEngine],
__devices_middle = [*__devices_little, T_Item.Nitrinium, T_Item.Phaser, T_Item.Energon, T_Item.Armor, T_Item.Absorber, T_Item.SuperioritySphere, ]
__devices_strong = [*__devices_middle, T_Item.Reflector, T_Item.livearmor, T_Item.MetaController, T_Item.VacuumCoreBattery, T_Item.XenoArmor]

mob_devices = {
    T_Mob.weak: [T_Item.Battery, T_Item.Damage, T_Item.RepairDroid, T_Item.Turbo, T_Item.Shield, T_Item.KEngine],
    T_Mob.middle: __devices_middle,
    T_Mob.strong: __devices_strong
}

mob_skills = {
    T_Mob.weak: {
    T_PlayerSkill.Defending: 0,
    T_PlayerSkill.Attacking: 0,
    T_PlayerSkill.Targeting: 0,
    T_PlayerSkill.Repairing: 0,
},
    T_Mob.middle: {
    T_PlayerSkill.Defending: 6,
    T_PlayerSkill.Attacking: 6,
    T_PlayerSkill.Targeting: 6,
    T_PlayerSkill.Repairing: 6,
},
    T_Mob.strong:{
    T_PlayerSkill.Defending:12,
    T_PlayerSkill.Attacking:12,
    T_PlayerSkill.Targeting:12,
    T_PlayerSkill.Repairing:12,
}
}

mob_level = {
    T_Mob.weak: 30,
    T_Mob.middle: 50,
    T_Mob.strong: 80,
}

Location_mobs = {
    systems_name['Неу']: [T_Ship.OCruiser, T_Ship.OCruiser, T_Ship.OLinkor],
}

mob_weapons = {
    T_Ship.OPalaven: [T_Weapon.Desintegrator],
    T_Ship.OCruiser: [T_Weapon.MultiBlaster],
    T_Ship.OLinkor: [T_Weapon.MultiBlaster],
    T_Ship.OFregat: [T_Weapon.Desintegrator],
    T_Ship.OScout: [T_Weapon.Desintegrator],
    T_Ship.OShockBrig: [T_Weapon.Desintegrator],
    T_Ship.OSiegeBrig: [T_Weapon.Desintegrator],
    T_Ship.OSiegeLinkor: [T_Weapon.Desintegrator, T_Weapon.Desintegrator],
    T_Ship.OTransport: [T_Weapon.AutoGun],
    T_Ship.OSience: [T_Weapon.Gun],
    T_Ship.OIndustrial: [T_Weapon.AutoGun],
    T_Ship.OIntercepter: [T_Weapon.MachineGun, T_Weapon.AutoGun],

    T_Ship.GIndustrial: [T_Weapon.Gun],#Gulduc gun
    T_Ship.XIntercepter: [T_Weapon.Xenopulsar],
    T_Ship.KTransport: [T_Weapon.PhotonGun],

    T_Ship.TSience: [
        T_Weapon.Desintegrator, T_Weapon.Desintegrator, T_Weapon.Desintegrator,
        T_Weapon.SplashRocketLauncher, T_Weapon.SplashRocketLauncher, T_Weapon.SplashRocketLauncher,
        T_Weapon.MultiBlaster, T_Weapon.MultiBlaster, T_Weapon.AutoGun
        ],
    T_Ship.KVarm: [
        T_Weapon.Vampire, T_Weapon.Vampire, T_Weapon.Vampire,
        T_Weapon.Vampire, T_Weapon.Vampire, T_Weapon.MultiBlaster,
        T_Weapon.MultiBlaster
        ],
}


def race_to_ship(race):
    pass

def ship_to_race(class_number):
    str_classNumber = str(class_number)
    if len(str_classNumber) == 2:
        return T_Race.OMOLENIAN_ID
    match int(str_classNumber[0]):
        case 1:
            return T_Race.IRRIITIAN_ID
        case 2:
            return T_Race.ANID_ID
        case 3:
            return T_Race.MEDRAMIL_ID
        case 4:
            return T_Race.GULDUC_ID
        case 5:
            return T_Race.KAANIAN_ID
        case 6:
            return T_Race.XENORUIT_ID
        case 7:
            return T_Race.XENORUIT_ID # Киуна
        case 8:
            return T_Race.GULDUC_ID # МК-1

def get_type_mob(CN_ship):
    type_ship = int(str(CN_ship)[-2:])
    if type_ship in ship_weak:
        return T_Mob.weak
    if type_ship in ship_middle:
        return T_Mob.middle
    if type_ship in ship_strong:
        return T_Mob.strong

def get_aliance_by_race(race) -> int:
    match race:
        case 1 | 2:
            return T_Aliance.NeoAliance
        case 3 | 4:
            return T_Aliance.Medan
        case 5:
            return T_Aliance.CorsairBrotherhood
        case 6:
            return T_Aliance.XenoEmpire
        case 7:
            return T_Aliance.SupremeCouncil
        case _:
            raise NotImplementedError("don\'t find this race")

def get_data_mobs():
    index = 0
    for location_id, CN_ship_mobs in Location_mobs.items():
        for CN_ship_mob in CN_ship_mobs:
            index += 1
            race = ship_to_race(CN_ship_mob)
            mob_type = get_type_mob(CN_ship_mob)
            yield {
                "id": -index,
                "locationId": location_id,
                "race": race,
                "aliance": get_aliance_by_race(race),
                "x": random.randint(-RADIUS_FROM_CENTER, RADIUS_FROM_CENTER),
                "y": random.randint(-RADIUS_FROM_CENTER, RADIUS_FROM_CENTER),
                "class_number": CN_ship_mob,
                "level": mob_level[mob_type],
                "status": 2,
                "RADIUS": RADIUS_FROM_CENTER,
                "skills": mob_skills[mob_type],
                "activeWeapons": mob_weapons[int(str(CN_ship_mob)[-2:])],
                "activeDevices": mob_devices[mob_type]
            }
