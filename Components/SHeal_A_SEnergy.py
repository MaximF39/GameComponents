from Components.Heal_A_Energ import Health, Energy


class HealthShip(Health):
    shields:int
    armor:int

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

    def device_damage(self, damage):
        self -= damage

class EnergyShip(Energy):
    pass



