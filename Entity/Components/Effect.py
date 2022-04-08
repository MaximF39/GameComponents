import datetime
import threading
import time

class Effects(dict):
    """
    P.ship.effects[1] = 2 # + effect(type=1, time=2) time = 2 second
    P.ship.effects[1] = 2 # + effect(type=1, time=2) time = 2 second

    Если добавить эффекты с одинаковыми типами, то их время сложится
    P.ship.effects[1] = 4 s

    P.ship.effects[1] = "const" # + effect(type=1, time=навсегда) time = навсегда
    P.ship.effects[-1] = "const" # - effect(type=1, time=навсегда) time = навсегда
    """
    __slots__ = ("Owner",)

    def __init__(self, seq=(), **kwargs):
        super().__init__(seq)
        self.__dict__.update(kwargs)

    def _change_effect(self, type_, plus:bool):
        if plus:    mod = 1
        else:       mod = -1

        if type_ == 1:
            self.Owner.speed += 50 * mod

        if not plus:
            if type_ in self:
                del self[type_]

    def _add_effects(self, type_):
        self._change_effect(type_, True)

    def _remove_effect(self, type_):
        self._change_effect(type_, False)

    def __setitem__(self, type_, time_):
        if time_ == "const":
            if type_ > 0:
                self._add_effects(type_)
            else:
                self._remove_effect(-type_)
            return
        else:
            t = datetime.datetime.now() + datetime.timedelta(seconds=time_)
            if type_ in self:
                t += self[type_]
                super().__getitem__(type_)['thread'].cancel()
                self._remove_effect(type_)
            time_ = {'time': t,
                     'thread':threading.Timer((t - datetime.datetime.now()).total_seconds(), self._remove_effect, args=(type_,))}
            time_['thread'].start()
            super().__setitem__(type_, time_)
            self._add_effects(type_)

    def __getitem__(self, item):
        return super().__getitem__(item)['time'] - datetime.datetime.now()

