import pickle
import pickle

class MyInt(int):
    def __iadd__(self, other):
        return self.__new__(type(self), self.__add__(other))

    def __isub__(self, other):
        return self.__new__(type(self), self.__sub__(other))

class Health(MyInt):
    pass


exit()
class T:
    s = 0

def get_class():
    file = open('../important', 'rb')

    # dump information to that file
    data = pickle.load(file)

    # close the file
    file.close()
    print(data[0].s)
get_class()

def to_class():
    data = []

    class T:
        s = 0
    e = T()

    e.s = 22
    data.append(e)

    file = open('../important', 'wb')

    pickle.dump(data, file)

    # close the file
    file.close()
exit()
def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class Test:
  ...

assert id(Test()) == id(Test())

exit()
class Employee(object):
    def __new__(cls,*args, **kwargs):
        if not hasattr(cls,'_inst'):
            # cls._inst = super(Employee, cls).__new__(cls)
            # если запустить код написаный ниже в Python3, он выдаст ошибку «TypeError: object() takes no parameters»
            cls._inst = super(Employee, cls).__new__(cls, *args,**kwargs)
        return cls._inst

assert id(Employee()) == id(Employee())
exit()
class SingletonMeta(type):
    _instances = {}


    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            _instances = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls.instances[cls]


class Singleton(metaclass=SingletonMeta):
    pass

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

if id(s1) == id(s2):
    print('Success')
else:
    print("Bad")


"""
instance
"""