from Vacuum.Game.Utils.MyInt import MyInt


class Health(MyInt):

    def __iadd__(self, other):
        if self == self.max:
            return self
        elif self + other > self.max:
            res = self.max
        else:
            res = self + other

        return type(self).__call__(res, **self.kwargs)

    def __isub__(self, other):
        if self - other > 0:
            res = self - other
        else:
            res = 0
            self.death()
        return type(self).__call__(res, **self.kwargs)

class Energy(MyInt):

    def __iadd__(self, other):
        if self == self.max:
            return self
        elif self + other > self.max:
            res = self.max
        else:
            res = self + other

        return type(self).__call__(res, **self.kwargs)

    def __isub__(self, other):
        if self - other > 0:
            res = self - other
        else:
            res = 0
        return type(self).__call__(res, **self.kwargs)