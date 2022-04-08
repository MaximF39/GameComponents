from Utils.MyInt import MyInt


class Cash(MyInt):
    def __new__(cls, cash, **kwargs):
        print('send pack')
        return super().__new__(cls, cash)