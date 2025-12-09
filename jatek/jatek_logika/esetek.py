from jatek.beallitas.tarol import jatekos_nev
from jatek.helyszinek import bejarat
from jatek.targyak.kulcs_targyak import kulcsok
import jatek.targyak.kulcs_targyak

def eset1():
    print("{:^120}".format("Elrabolták a legjobb barátodat. Készen állsz megmenteni?"))

    jatekos = input("Hogy szólíthatunk? ")

    szoveg = (f"Ez egy magánterület, {jatekos}. Biztos vagy a belépésben?\n"
              f"Vállalod, hogy kísérletezzenek rajtad?")

    for sor in szoveg.split("\n"):
        print("{:^120}".format(sor))

    bejarat.bejarat = True

def eset2():
    print("{:^120}".format("Most már kinyithatod az ajtót"))
    konyha = True

def eset3():
    print(f"\n")
    print("{:^120}".format("Nem tudsz bemenni a házba, keresd meg a kulcsot"))
    print("{:^120}".format("keresés a lábtörlő alatt/kopogj az ajtón: 1/2"))
    valasztas = int(input("válassz: "))
    while valasztas != 1 and valasztas != 2:
        valasztas = int(input("válassz: "))
    if valasztas == 1:
        print(f"\n")
        print("{:^120}".format("Megtaláltad a kulcsot!"))
        jatek.targyak.kulcs_targyak.kulcsok = True
        eset2()
    else:
        print(f"\n")
        print("{:^120}".format("Senki nem nyitott ajtót. Megnézed a lábtörlőt."))
        print("{:^120}".format("Megtaláltad a kulcsot!"))
        jatek.targyak.kulcs_targyak.kulcsok = True
        eset2()


def eset4():
    pass

def eset5():
    pass

def eset6():
    print(f"\n")
    print("{:^120}".format("Belépsz a konyhába."))

def eset7():
    pass

def eset8():
    pass

def eset9():
    pass
