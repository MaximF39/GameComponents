class a:
    s = 2

    def __init__(self, s):
        self.s = s


s = {10:a(10), 11:a(11), 12:a(12), }

s[10].s = 22

print(s[10].s)
