from ._Components.Set import Set
from ._Components.SetSO import SetSO


class Portal(SetSO):

    def __init__(self, data):
        super().__init__(data['x'], data['y'])
        self.__dict__.update(data)

    def set(self, Whom):
        pass

    def landable(self):
        return True

    def get_v2d_to_target_location(self):
        return self.x, self.y