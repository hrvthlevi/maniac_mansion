import jatek.helyszinek as hely
from jatek.targyak import kulcs_targyak as kulcs
import jatek.jatek_logika.esetek as esetek

def jatekmenet():
    esetek.eset1()
    if hely.bejarat and kulcs.kulcs:
        esetek.eset2()
    elif hely.bejarat:
            esetek.eset3()

    if hely.postalada:
        esetek.eset4()

    if hely.konyha and kulcs.level:
        esetek.eset5()
    elif hely.konyha:
        esetek.eset6()

    if hely.borton:
        esetek.eset7()

    if hely.lepcso:
        esetek.eset8()
    elif hely.konyha and kulcs.sult_hus:
        esetek.eset9()





