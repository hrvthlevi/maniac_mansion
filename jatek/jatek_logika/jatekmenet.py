from jatek.helyszinek import bejarat, konyha, borton, dolgozo, lepcso_fordulo, kezdokepernyo, posta
from jatek.targyak.kulcs_targyak import kulcsok, level
from jatek.targyak import fogyaszthato as etel
import jatek.jatek_logika.esetek as esetek


def jatekmenet():
    esetek.eset1()
    if bejarat.bejarat:
        esetek.eset3()
        if bejarat.bejarat and kulcsok:
            esetek.eset2()

    if posta:
        esetek.eset4()

    if konyha and level:
        esetek.eset5()
    elif konyha:
        esetek.eset6()

    if borton:
        esetek.eset7()

    if lepcso_fordulo:
        esetek.eset8()
    elif konyha and etel.sult_hus:
        esetek.eset9()





