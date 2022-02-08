# krávy a býci 
# random 4 ciferné číslo
# ptaní se uživatele na 4 ciferné číslo
# procházení čísla, když je na správném místě, tak je to býk. Když se tam vůbec nachází, tak je kráva
# vysledek(parametr) jsou 4 býci
# random.cislo   , proměné (krávy a bíci) budou slovník,   while(4býci),  for na projití všech číslovek,  indexování(+=1)    

from random import randrange

print('''Vítej u zábavné a všemi oblíbené hry KRAVY A BÝCI!
    Tvým úkolem bude uhádnout čtyř místné číslo, které vygeneruje počítač. ''')

dobytek = {"kráva" : 0, "býk" : 0}

def main():
    hodnota_pc = cislo_pc()
    while True:
        odhad = typni_si()
        if hodnota_pc == odhad:
            print("Vyhrál jsi.")
        else:
            for i in odhad:
                if hodnota_pc[i] == hodnota_pc[i]:
                    dobytek["kráva"]+=1
        
                print("Máš", dobytek["kráva"], "krav a", dobytek["býk"], "býků")    #vypíše se hláška na sečtení dobytka
            if dobytek["býk"] == 4:             #ukončí cyklus, jestě musím vymyslet jestli While nebo for
                break


def typni_si():
    return str(input("Jaký je tvůj typ? "))


def cislo_pc():
    return str(randrange(1000, 9999))





main()

