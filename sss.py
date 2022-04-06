r = [
".W...",
"...W.",
".W.W.",
"...W.",
"...W."]

i = [0, 0]

def right():
    global r, i
    if r[i[0]][i[1] + 1] == '..':
        i[1] += 1
        if i == [len(r) - 1, len(r[-1]) - 1]:
            print("GOOD")
            exit()
        return True
    return False


def left():
    global r, i
    if r[i[0]][i[1] - 1] == '..':
        i[1] -= 1
        return True
    return False


def up():
    global r, i
    if r[i[0] - 1][i[1]] == '..':
        i[0] -= 1
        return True
    return False


def down():
    global r, i
    if r[i[0] + 1][i[1]] == '..':
        i[0] += 1
        if i == [len(r - 1), len(r[-1] - 1)]:
            print("GOOD")
            exit()
        return True
    return False

while 1:

    def base():
        while right():pass

        while down():pass

    base()
    up()
    left()








