import threading
import time

from Vacuum.Game.Components.DropHealth import DropHealth
from Vacuum.Game.Components.Heal_A_Energ import Energy


class HealthShip(DropHealth):
    shields:int
    armor:int

    def __init__(self, value, **kwargs):
        super().__init__(value, **kwargs)
        threading.Timer(1, self.update).start()

    def update(self):
        self += 10

    def weapon_damage(self, damage, type_):
        sub_damage = 0.01 * self.shields * damage
        match type_:
            case 'kinet':
                sub_damage = 0.1 * sub_damage + self.armor
            case 'Rocket':
                sub_damage = sub_damage + self.armor
        damage -= sub_damage
        if damage <= 0:     damage = 1
        self -= damage

    def death(self):
        super().death()

    def drop(self):
        pass

    def device_damage(self, damage):
        self -= damage

class EnergyShip(Energy):
    def __init__(self, value, **kwargs):
        super().__init__(value, **kwargs)
        threading.Timer(1, self.update).start()

    def update(self):
        self += 10


