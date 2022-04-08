from Utils import MyInt

lvl ={
    0: 0,
    1: 100,
    2: 2000,
    3: 30000,
}

class Experience(MyInt):

    def __new__(cls, exp, **kwargs):
        print("i send packs")
        return super().__new__(cls, exp, **kwargs)

    def __init__(self, value):
        self.level = self.get_level()

    def get_level(self):
        for k, v in lvl.items():
            if v > self:
                return k - 1

class Status(MyInt):

    def __new__(cls, stat, **kwargs):
        print("i send packs")
        return super().__new__(cls, stat, **kwargs)

    def __init__(self, value):
        self.level = self.get_level()

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