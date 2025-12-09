from jatek.helyszinek import bejarat, posta, konyha, borton, lepcso_fordulo
import jatek.targyak.kulcs_targyak as kt
from jatek.targyak import fogyaszthato as etel
import jatek.jatek_logika.esetek as esetek

def jatekmenet():

    esetek.eset1()

    #bejarat
    if bejarat.ott_vagyunk:
        esetek.eset3()
        if kt.kulcs.megvan:
            esetek.eset2()

    #posta
    if posta.ott_vagyunk:
        esetek.eset4()

    #konyha
    if konyha.ott_vagyunk:
        if kt.level.megvan:
            esetek.eset5()
        elif etel.sult_hus:
            esetek.eset9()
        else:
            esetek.eset6()

    #borton
    if borton.ott_vagyunk:
        esetek.eset7()

    #lepcso
    if lepcso_fordulo.ott_vagyunk:
        esetek.eset8()
