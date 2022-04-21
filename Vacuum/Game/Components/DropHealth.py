from Vacuum.Game.Components.Heal_A_Energ import Health


class DropHealth(Health):

    def death(self):
        self.drop()

    def drop(self):
        raise NotImplementedError()