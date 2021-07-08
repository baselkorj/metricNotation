i = 0
hi = ["", "k", "M", "G", "T", "P", "E", "Z", "Y"]
low = ["", "m", "μ", "p", "f", "a"]


def atto(x):
    temp = x * 1000000000000000000
    x = str(temp) + "a"
    return x


def femto(x):
    temp = x * 1000000000000000
    x = str(temp) + "f"
    return x


def pico(x):
    temp = x * 1000000000000
    x = str(temp) + "p"
    return x


def nano(x):
    temp = x * 1000000000
    x = str(temp) + "n"
    return x


def micro(x):
    temp = x * 1000000
    x = str(temp) + "μ"
    return x


def mili(x):
    temp = x * 1000
    x = str(temp) + "m"
    return x


def kilo(x):
    temp = x / 1000
    x = str(temp) + "k"
    return x


def mega(x):
    temp = x / 1000000
    x = str(temp) + "M"
    return x


def giga(x):
    temp = x / 1000000000
    x = str(temp) + "G"
    return x


def tera(x):
    temp = x / 1000000000000
    x = str(temp) + "T"
    return x


def peta(x):
    temp = x / 1000000000000000
    x = str(temp) + "P"
    return x


def exa(x):
    temp = x / 1000000000000000000
    x = str(temp) + "E"
    return x


def zetta(x):
    temp = x / 1000000000000000000000
    x = str(temp) + "Z"
    return x


def yotta(x):
    temp = x / 1000000000000000000000000
    x = str(temp) + "Y"
    return x


def auto(x, y=0):
    x = float(x)
    if x > 1000:
        div_num(x, y)
    else:
        mul_num(x, y)


def div_num(x, y):
    i = 0
    while x > 1000:
        x = x / 1000
        i = i + 1

    if y == 0:
        temp = str(x) + hi[i]
    else:
        temp = str(round(x, y)) + hi[i]

    print(temp)
    return temp


def mul_num(x, y):
    i = 0
    while x < 1:
        x = x * 1000
        i = i + 1

    if y == 0:
        temp = str(x) + low[i]
    else:
        temp = str(round(x, y)) + low[i]

    print(temp)
    return temp


def help():  # this is not needed
    print("This is a help function.")  # this is not needed


def lisence():  # this is not needed
    print("This is the lisence.")  # this is not needed
