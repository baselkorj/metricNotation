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


def centi(x):
    temp = x * 100
    x = str(temp) + "c"
    return x


def deci(x):
    temp = x * 10
    x = str(temp) + "d"
    return x


def deka(x):
    temp = x / 10
    x = str(temp) + "da"
    return x


def hecto(x):
    temp = x / 100
    x = str(temp) + "h"
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


def help():
    print("This is a help function.")


def lisence():
    print("This is the lisence.")
