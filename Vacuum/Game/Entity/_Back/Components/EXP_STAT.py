from Vacuum.Game.Utils.MyInt import MyInt

lvl ={
    0: 0,
    1: 100,
    2: 2000,
    3: 30000,
}

class Experience(MyInt):

    def __new__(cls, exp, **kwargs):
        return super().__new__(cls, exp)

    def __init__(self, value, **kwargs):
        super().__init__(value, **kwargs)
        self.level = self.get_level()
        self.next = lvl[self.level + 1] - self

    def get_level(self):
        for k, v in lvl.items():
            if v > self:
                return k - 1

class Status(MyInt):

    def __new__(cls, stat, **kwargs):
        return super().__new__(cls, stat)

    def __init__(self, value, **kwargs):
        super().__init__(value, **kwargs)
        self.level = self.get_level()
        self.next = lvl[self.level + 1] - self

    def get_level(self):
        for k, v in lvl.items():
            if v > self:
                return k - 1


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

if __name__ == '__main__':
    test_exp()
    test_stat()