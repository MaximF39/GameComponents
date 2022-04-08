class Funnel(object):
    stack: list
    max_stack = 15

    def __init__(self):
        pass

    def fill(self, *args):
        if self.max_stack > len(self.stack):
            if len(self.stack) + len(args) > self.max_stack:
                count = self.max_stack - len(self.stack)
                self.stack.extend(args[:count])
                return
            self.stack.extend(args)

    def drip(self):
        return self.stack.pop()

    def get_stack(self):
        # stack = ()
        # for i in range(5):
        #     i * 2 + 1
        return

    def __str__(self):
        txt = ''
        for i in range(1, 5):
            size = i * 2 + 1
            # if len(self.stack) >
            min_index = sum(i for i in range(i))
            max_index = sum(i for i in range(i)) + i

            txt_stack = " ".join(list(map(str, self.stack[min_index:max_index])))

            txt += str(f"\\{txt_stack}/").center(size)
        return txt


e = Funnel()
print(e)
