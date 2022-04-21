class MyInt(int):

    def __new__(cls, value, **kwargs):
        return super().__new__(cls, value)

    def __init__(self, value, **kwargs):
        self.__dict__.update(kwargs)
        self.kwargs = kwargs

    def __iadd__(self, other):
        return type(self).__call__(self + other, **self.kwargs)

    def __isub__(self, other):
        return  type(self).__call__(self - other, **self.kwargs)
