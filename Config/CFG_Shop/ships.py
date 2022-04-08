from python.Static.Type.Item.T_Ship import T_Ship

weak_system = [2, 9, 6, 8, 5, 43, 30, 46, 105, 106, 107, 108, 109, 120, 114, 115, 125, 111, 112, 113]
medium_system = [7, 38, 1, 4]
strong_system = [68, 69, 70, 71]


def weak_ship(race):
    pref = f'{race - 1}0'
    return [
    int(pref + str(T_Ship.OTransport)),
    # (хз корвет),
    int(pref + str(T_Ship.OIntercepter)),
    int(pref + str(T_Ship.OFregat)),
    int(pref + str(T_Ship.OSience)),
    int(pref + str(T_Ship.OLMiner))
    ]

def medium_ship(race):
    pref = f'{race - 1}0'
    return  [
    int(pref + str(T_Ship.OCruiser)),
    int(pref + str(T_Ship.OLinkor)),
    int(pref + str(T_Ship.OIntercepterHavy)),
    int(pref + str(T_Ship.OFregatArmored)),
    int(pref + str(T_Ship.OFregatAssault)),
    int(pref + str(T_Ship.OFregatAssaultM1)),
    int(pref + str(T_Ship.OScout)),
]

def strong_ship(race):
    pref = f'{race - 1}0'
    return [
    int(pref + str(T_Ship.OBrig)),
    int(pref + str(T_Ship.OPalaven)),
]


