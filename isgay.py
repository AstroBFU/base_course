male,female = list(), list()
def isgay(*args):
    mf = 0
    for i in args:
        if i in male:
            mf += 1
    if mf / len(args) > 0.5:
        return True
    return False