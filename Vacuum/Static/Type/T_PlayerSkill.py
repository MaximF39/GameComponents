class T_PlayerSkill:
    KineticWeapons: int = 1
    EnergyWeapons: int = 2
    RocketWeapons: int = 3
    Mining: int = 5
    Repairing: int = 6
    Trading: int = 8
    Control: int = 11
    Defending: int = 14
    Attacking: int = 16
    Tactics: int = 17
    Piloting: int = 18
    Targeting: int = 19
    Electronics: int = 20
    Cybernetics: int = 21
    Mechanics: int = 22
    Biocemistry: int = 23


    def __init__(self):
        self.d = []
        for el in self.__dir__():
            if el[:2] == '__' and el[-2:] == '__':
                continue
            self.d.append(el)

    def get(self, value):
        for el in self.d:
            if getattr(self, el) == value:
                return el