# krávy a býci 
# random 4 ciferné číslo
# ptaní se uživatele na 4 ciferné číslo
# procházení čísla, když je na správném místě, tak je to býk. Když se tam vůbec nachází, tak je kráva
# vysledek(parametr) jsou 4 býci
# random.cislo   , proměné (krávy a bíci) budou slovník,   while(4býci),  for na projití všech číslovek,  indexování(+=1)    

from random import random, randint    

print('''Vítej u zábavné a všemi oblíbené hry KRAVY A BÝCI!
Tvým úkolem bude uhádnout čtyř místné číslo, které vygeneruje počítač. ''')

dobytek = {"kráva" : 0, "býk" : 0}

def main():
    hodnota_pc = cislo_pc()
    while dobytek["býk"] != 4:
        odhad = typni_si()
        if hodnota_pc == odhad:
            print("Vyhrál jsi.")
            break
        else:
            i = 0
            for jednotlivy_clen in odhad:
                if jednotlivy_clen == hodnota_pc[i]:
                    dobytek["býk"]+=1
                elif jednotlivy_clen in hodnota_pc:
                    dobytek["kráva"]+=1
                i +=1
            print("Máš", dobytek["kráva"], "krav a", dobytek["býk"], "býků")

def typni_si():
    cislo_uzivatel = ""
    while len(cislo_uzivatel) < 4:
        cislo = input("Jaký je tvůj typ? Zadávej jednociferná čísla: ")
        if len(cislo) > 1:
            print("Seš dement")
        else:
            if cislo in cislo_uzivatel:
                print('Fuck you! Zadej jiné číslo')
            elif cislo not in cislo_uzivatel:
                cislo_uzivatel += cislo
    return cislo_uzivatel
        
def cislo_pc():
    cislo_pc = set()
    while len(cislo_pc) < 4:
        cislo_pc.add(randint(0,9))
    cislo_str = ""
    for jednotliva_cisla in cislo_pc:
        cislo_str += str(jednotliva_cisla)
    return cislo_str

main()

