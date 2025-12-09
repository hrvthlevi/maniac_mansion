from jatek.beallitas.tarol import jatekos_nev
from jatek.helyszinek import bejarat
from jatek.targyak import kulcs_targyak as kulcs

def eset1():
    print("{:^120}".format("Elrabolták a legjobb barátodat. Készen állsz megmenteni?"))

    jatekos = input("Hogy szólíthatunk? ")

    szoveg = (f"Ez egy magánterület, {jatekos}. Biztos vagy a belépésben?\n"
              f"Vállalod, hogy kísérletezzenek rajtad?")

    for sor in szoveg.split("\n"):
        print("{:^120}".format(sor))

    bejarat.bejarat = True

def eset2():
    print("Most már kinyithatod az ajtót")
    konyha = True

def eset3():
    print("Nem tudsz bemenni a házba, keresd meg a kulcsot")
    print("keresés a lábtörlő alatt/kopogj az ajtón: 1/2")
    valasztas = int(input("válassz: "))
    while valasztas != 1 or valasztas != 2:
        valasztas = int(input("válassz: "))
    if valasztas == 1:
        print("Megtaláltad a kulcsot!")
        kulcs.kulcs == True
    else:
        print("Senki nem nyitott ajtót. Megnézed a lábtörlőt.")
        print("Megtaláltad a kulcsot!")
        kulcs.kulcs == True

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