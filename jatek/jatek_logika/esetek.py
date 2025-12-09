from jatek.beallitas.tarol import jatekos_nev
from jatek.helyszinek import bejarat

def eset1():
    print("{:^120}".format("Elrabolták a legjobb barátodat. Készen állsz megmenteni?"))

    jatekos = input("Hogy szólíthatunk? ")

    szoveg = (f"Ez egy magánterület, {jatekos}. Biztos vagy a belépésben?\n"
              f"Vállalod, hogy kísérletezzenek rajtad?")

    for sor in szoveg.split("\n"):
        print("{:^120}".format(sor))

    bejarat.ott_vagyunk = True

def eset2():
    pass

def eset3():
    print("anyád")

def eset4():
    pass

def eset5():
    pass

def eset6():
    pass

def eset7():
    pass

def eset8():
    pass

def eset9():
    pass