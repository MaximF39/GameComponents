import datetime
import threading
import time

class Effect(dict):
    """
    P.Ship.effects[1] = 2 # + effect(type=1, time=2) time = 2 second
    P.Ship.effects[1] = 2 # + effect(type=1, time=2) time = 2 second

    Если добавить эффекты с одинаковыми типами, то их время сложится
    P.Ship.effects[1] = 4 s

    P.Ship.effects[1] = "const" # + effect(type=1, time=навсегда) time = навсегда
    P.Ship.effects[-1] = "const" # - effect(type=1, time=навсегда) time = навсегда
    """

    def __init__(self, seq=(), **kwargs):
        super().__init__(seq)
        self.__dict__.update(kwargs)

    def _change_effect(self, type_, plus:bool):
        print(type_)
        if plus:    mod = 1
        else:       mod = -1

        match type_:
            case 1:
                self.Ship.damage += 0.5 * mod
            case 12:
                self.Ship.agly = mod
            case 16:
                for i in range(3):
                    self.Ship.energy += 50 * mod
                    time.sleep(1)
            case 18:
                self.Ship.AttackSelf = mod
            case 21:
                damage = 500

            case 22:
                for Entity in self.Ship.OwnerShip.Location.entities:
                    R = self.Ship.V2D.distance(Entity.Ship.V2D)
                    if 300 >= R:
                        Entity.Ship.health -= 400
            case 29:
                self.Ship.health += 300



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

