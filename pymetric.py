i = 0
hi = ["", "k", "M", "G", "T", "P", "E", "Z", "Y"]
low = ["", "m", "μ", "p", "f", "a"]


def atto(x, y=0):
    temp = x * 1000000000000000000
    x = str(round_Num(temp, y)) + "a"
    return x


def femto(x, y=0):
    temp = x * 1000000000000000
    x = str(round_Num(temp, y)) + "f"
    return x


def pico(x, y=0):
    temp = x * 1000000000000
    x = str(round_Num(temp, y)) + "p"
    return x


def nano(x, y=0):
    temp = x * 1000000000
    x = str(round_Num(temp, y)) + "n"
    return x


def micro(x, y=0):
    temp = x * 1000000
    x = str(round_Num(temp, y)) + "μ"
    return x


def milli(x, y=0):
    temp = x * 1000
    x = str(round_Num(temp, y)) + "m"
    return x


def kilo(x, y=0):
    temp = x / 1000
    x = str(round_Num(temp, y)) + "k"
    return x


def mega(x, y=0):
    temp = x / 1000000
    x = str(round_Num(temp, y)) + "M"
    return x


def giga(x, y=0):
    temp = x / 1000000000
    x = str(round_Num(temp, y)) + "G"
    return x


def tera(x, y=0):
    temp = x / 1000000000000
    x = str(round_Num(temp, y)) + "T"
    return x


def peta(x, y=0):
    temp = x / 1000000000000000
    x = str(round_Num(temp, y)) + "P"
    return x


def exa(x, y=0):
    temp = x / 1000000000000000000
    x = str(round_Num(temp, y)) + "E"
    return x


def zetta(x, y=0):
    temp = x / 1000000000000000000000
    x = str(round_Num(temp, y)) + "Z"
    return x


def yotta(x, y=0):
    temp = x / 1000000000000000000000000
    x = str(round_Num(temp, y)) + "Y"
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


def round_Num(
    x, y
):  # this function to see if the user wants to round the results or not
    if y == 0:
        th = str(x)
    else:
        th = str(round(x, y))

    return th
