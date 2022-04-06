import datetime
import threading
import time

class Effects(dict):
    """
    P.ship.effects[1] = 2 # + effect(type=1, time=2) time = 2 second
    P.ship.effects[1] = 2 # + effect(type=1, time=2) time = 2 second

    Если добавить эффекты с одинаковыми типами, то их время сложится
    P.ship.effects[1] = 4 s

    P.ship.effects[1] = -1 # + effect(type=1, time=навсегда) time = навсегда
    P.ship.effects[-1] = -1 # - effect(type=1, time=навсегда) time = навсегда
    """

    def _change_effect(self, type_, plus:bool):
        if plus:mod = 1
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

    def __new__(cls, Owner, *args, **kwargs):
        cls.Owner = Owner
        return super().__new__(cls, *args, **kwargs)

    def __setitem__(self, type_, time_):
        if time_ == -1:
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

class Player:
    def __init__(self):
        self.ship = Ship()

class Ship:
    def __init__(self):
        self.effects = Effects(Owner=self)
        self.speed = 50
        self.basespeed = 50

    def __repr__(self):
        return self.__class__.__name__


""" TEST """
def test_temporary_effect():

    def test_add_effect():
        P = Player() # default 50 speed
        assert P.ship.speed == 50
        P.ship.effects[1] = 2

        assert P.ship.speed == 100

        time.sleep(2.1)
        assert P.ship.speed == 50

    def test_sum_effect():
        P = Player()
        P.ship.effects[1] = 2
        P.ship.effects[1] = 2

        assert P.ship.speed == 100

        time.sleep(3)
        assert P.ship.speed == 100

        time.sleep(1.1)
        assert P.ship.speed == 50

    test_add_effect()
    test_sum_effect()

def test_const_effect():
    """ CONST EFFECT """
    def test_add_effect():
        P = Player()
        P.ship.effects[1] = -1
        assert P.ship.speed == 100

    def test_remove_effect():
        P = Player()

        P.ship.effects[1] = -1
        assert P.ship.speed == 100

        P.ship.effects[-1] = -1
        assert P.ship.speed == 50

    test_add_effect()
    test_remove_effect()

if __name__ == '__main__':
    test_temporary_effect()
    test_const_effect()