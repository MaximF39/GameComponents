import copy
import uuid

from Vacuum.Static.ParseJson import item_CN
from Vacuum.Static.Type.T_PlayerSkill import T_PlayerSkill


class _Item:
    """
    _Item += _Item
    """

    def __init__(self, data):
        super().__init__()
        self.__dict__.update(data)
        self.guid = self._get_guid()
        self.inUsing = False

    def __iadd__(self, item_: "_Item"):
        return self.__add__(item_)

    def __add__(self, item_):
        if self.const:
            return self

        if isinstance(item_, _Item):
            self.wear += item_.wear
            return self

        if isinstance(item_, int):
            self.wear += item_
            return self

    def __isub__(self, other):
        if self.const:
            return self
        if isinstance(other, int):
            self.wear -= other
            if not self.stack:
                return self
            else:
                if self.wear == 0:
                    self.__del_invt_A_item(wear=other)
                    return self
                elif self.wear > 0:
                    return self.my_copy_D_invt()
                else:
                    raise NotImplementedError("wear -= int; wear < 0")

    def __sub__(self, other: int):
        self.__isub__(other)
        if self.stack:   return self.my_copy_D_invt(wear=other, const=False)
        return self

    def get_size(self, wear=None):
        if self.stack:   return round(self.size * (wear or self.wear))
        else:               return round(self.size)

    def get_cost(self, wear=None):
        if self.stack:   return round(self.cost * (wear or self.wear))
        else:               return round(self.cost)

    def copy(self, /, wear=None, const=None) -> "_Item":
        item_ = copy.copy(self)
        item_.guid = item_._get_guid()
        if not wear is None:    item_.wear = wear
        if not const is None:   item_.const = const
        return item_

    def my_copy_D_invt(self, /, **kwargs) -> "_Item":
        item_ = self.copy(**kwargs)
        if hasattr(item_, 'inventory') :    del item_.inventory
        return item_

    def __del_invt_A_item(self, /, wear=None):
        if hasattr(self, "inventory"):
            del self.inventory[self.guid]
            del self.inventory
        if wear:
            self.wear = wear

    """ Use logic items """

    def use(self):
        self.inUsing= True

    def unuse(self):
        self.inUsing= False

    @staticmethod
    def _get_guid():
        return uuid.uuid4().bytes

    def satisfying(self, Who=None):
        if not hasattr(self, "restrictions"):
            return True
        if Who is None:
            if hasattr(self, "inventory"):
                Who = self.inventory.Player
            else:
                raise NotImplementedError()

        skills = Who.skills
        SkillTypeStr = T_PlayerSkill()
        for skill in self.restrictions:
            match skill["type"]:
                case 2:
                    if skill['value'] > skills[SkillTypeStr.get(skill['value_type'])]:
                        return False
                case 4:
                    if skill['value'] > Who.Ship.cpu - Who.Ship.cpu_used:
                        return False
                case 5:
                    if Who.status.level > skill['value']:  # -3 > -2 пир или коп и ниже тоже
                        return False
                case 6:
                    if Who.status.level < skill['value']:  # 3 < 2 # player < need -> False
                        return False
                case _:
                    print('Не понятный тип', skill['type'])
        return True
