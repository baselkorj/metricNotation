from decimal import Decimal


def atto(x):
    temp = x * 1000000000000000000
    x = str(Decimal(temp)) + "a"
    return x


def femto(x):
    temp = x * 1000000000000000
    x = str(Decimal(temp)) + "f"
    return x


def pico(x):
    temp = x * 1000000000000
    x = str(Decimal(temp)) + "p"
    return x


def nano(x):
    temp = x * 1000000000
    x = str(Decimal(temp)) + "n"
    return x


def micro(x):
    temp = x * 1000000
    x = str(Decimal(temp)) + "μ"
    return x


def mili(x):
    temp = x * 1000
    x = str(Decimal(temp)) + "m"
    return x


def centi(x):
    temp = x * 100
    x = str(Decimal(temp)) + "c"
    return x


def deci(x):
    temp = x * 10
    x = str(Decimal(temp)) + "d"
    return x


def deka(x):
    temp = x / 10
    x = str(Decimal(temp)) + "da"
    return x


def hecto(x):
    temp = x / 100
    x = str(Decimal(temp)) + "h"
    return x


def kilo(x):
    temp = x / 1000
    x = str(Decimal(temp)) + "k"
    return x


def mega(x):
    temp = x / 1000000
    x = str(Decimal(temp)) + "M"
    return x


def giga(x):
    temp = x * 1000000000
    x = str(Decimal(temp)) + "G"
    return x


def tera(x):
    temp = x * 1000000000000
    x = str(Decimal(temp)) + "T"
    return x


def peta(x):
    temp = x * 1000000000000000
    x = str(Decimal(temp)) + "P"
    return x


def exa(x):
    temp = x * 1000000000000000000
    x = str(Decimal(temp)) + "E"
    return x


def zetta(x):
    temp = x * 1000000000000000000000
    x = str(Decimal(temp)) + "Z"
    return x


def yotta(x):
    temp = x * 1000000000000000000000000
    x = str(Decimal(temp)) + "Y"
    return x


def help():
    print("This is a help function.")


def lisence():
    print("This is the lisence.")
