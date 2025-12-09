from jatek.beallitas.tarol import jatekos_nev
from jatek.helyszinek import bejarat

WIDTH = 120

def eset1():
    print("{:^120}".format("Elrabolták a legjobb barátodat. Készen állsz megmenteni?"))

    jatekos = input("Hogy szólíthatunk? ")

    szoveg = (f"Ez egy magánterület, {jatekos}. Biztos vagy a belépésben?\n"
              f"Vállalod, hogy kísérletezzenek rajtad?")

    for sor in szoveg.split("\n"):
        print("{:^120}".format(sor))

    bejarat.ott_vagyunk = True


def eset3():
    print("anyád")