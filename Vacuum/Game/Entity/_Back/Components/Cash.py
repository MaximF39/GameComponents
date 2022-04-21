from Vacuum.Game.Utils.MyInt import MyInt
from Vacuum.Static.Type.Package.T_ServerRequest import T_ServerRequest
from Vacuum.Static.Type.Package.T_UpdateValue import T_UpdateValue


class Cash(MyInt):
    def __new__(cls, cash, **kwargs):
        kwargs['Player'].Pack += {T_ServerRequest.UPDATE_VALUE: T_UpdateValue.PlayerCash}
        return super().__new__(cls, cash)