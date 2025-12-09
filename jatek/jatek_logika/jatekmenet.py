from jatek.helyszinek import bejarat, konyha, borton, dolgozo, lepcso_fordulo, kezdokepernyo, posta
from jatek.targyak import kulcs_targyak as kulcs
from jatek.targyak import fogyaszthato as etel
import jatek.jatek_logika.esetek as esetek


def jatekmenet():
    esetek.eset1()
    if bejarat.bejarat and kulcs.kulcs:
        esetek.eset2()
    elif bejarat.bejarat:
            esetek.eset3()

    if posta:
        esetek.eset4()

    if konyha and kulcs.level:
        esetek.eset5()
    elif konyha:
        esetek.eset6()

    if borton:
        esetek.eset7()

    if lepcso_fordulo:
        esetek.eset8()
    elif konyha and etel.sult_hus:
        esetek.eset9()





