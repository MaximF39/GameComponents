from python.Static.Type.Item.T_Ship import T_Ship
# O, I, A, M
races = ['', '10', '20', '30']

_def = [
    {T_Ship.OIntercepter: T_Ship.OIntercepterHavy},
        {T_Ship.OTransport: T_Ship.OLRTransport},
        {T_Ship.OFregat: T_Ship.OFregatArmored},
        {T_Ship.OIndustrial: T_Ship.OScout}, # в будущем
        {T_Ship.OScout: T_Ship.OSience},
        {T_Ship.OLinkor: T_Ship.OSiegeLinkor},
        {T_Ship.OIntercepterHavy: T_Ship.OIntercepterCorsar},
        {T_Ship.OIntercepterCorsar: T_Ship.PIntercepterCorsar},
        {T_Ship.OFregatArmored: T_Ship.OFregatAssault},
        {T_Ship.OFregatAssault: T_Ship.OFregatAssaultM1},
        {T_Ship.OCarrier: T_Ship.OBrig}, # в будущем
        {T_Ship.OBrig: T_Ship.OShockBrig},
        {T_Ship.OShockBrig: T_Ship.OSiegeBrig},
        {T_Ship.OLRTransport: T_Ship.OFTransport},]

cfg_upgrade ={}

for race in races:
    for dict_ in _def:
        for k, v in dict_.items():
            if v == 8001:
                to_ship = v
            else:
                to_ship = int(f'{race}{v}')
            cfg_upgrade[int(f'{race}{k}')] = to_ship

if __name__ == '__main__':
    print(cfg_upgrade)


