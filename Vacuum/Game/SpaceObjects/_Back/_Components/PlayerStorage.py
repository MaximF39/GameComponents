from Vacuum.Game.Entity._Back.Player import Player


class PlayerStorage:

    def __init__(self):
        self.players = []

    def set(self, Whom):
        if isinstance(Whom, Player):
            self.players.append(Whom)

    def remove(self, Entity):
        if isinstance(Entity, Player):
            self.players.remove(Entity)

    def landable(self, Player):
        return self.aliance == Player.aliance | self.id in [128, ]