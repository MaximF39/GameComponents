import pytest

lvl ={
    0: 0,
    1: 100,
    2: 2000,
    3: 30000,
}

class MyInt(int):

    def _change(self):
        raise NotImplementedError

    def new(self, value):
        raise NotImplementedError

    def __iadd__(self, other):
        self._change()
        return self.new(self.__add__(other))

    def __isub__(self, other):
        self._change()
        return self.new(self.__sub__(other))

class Experience(MyInt):

    def __init__(self, value):
        self.level = self.get_level()

    def get_level(self):
        for k, v in lvl.items():
            if v > self:
                return k - 1

    def new(self, value):
        return Experience(value)

    def _change(self):
        print(self.__class__.__name__)

class Status(MyInt):

    def __init__(self, value):
        self.level = self.get_level()

    def get_level(self):
        for k, v in lvl.items():
            if v > self:
                return k - 1

    def new(self, value):
        return Status(value)

    def _change(self):
        print(self.__class__.__name__)


""" TEST """

def test_exp():
    exp = Experience(2000)
    assert exp.level == 2
    assert exp == 2000
    exp -= 3
    assert exp == 1997
    assert exp.level == 1
    exp += 5
    assert exp == 2002
    assert exp.level == 2

def test_stat():
    exp = Status(2000)
    assert exp.level == 2
    assert exp == 2000
    exp -= 3
    assert exp == 1997
    assert exp.level == 1
    exp += 5
    assert exp == 2002
    assert exp.level == 2
