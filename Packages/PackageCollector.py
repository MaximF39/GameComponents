class PackageCollector(set):
    all = []
    Player:"Player"
    default_set:set

    def __new__(cls, seq=()):
        return super().__new__(cls, seq)

    def __init__(self, seq=()):
        super().__init__(seq)
        self.all.append(self)

    def send(self):
        self.default_set = set()
        all_pack = self.default_set | (self or set())
        for PackNumber in all_pack:
            pass
        self.clear()

    def __iadd__(self, PackNumber):
        return self.add(PackNumber)

