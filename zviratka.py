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
    # # print(hodnota_pc)
    # for i in hodnota_pc:
        


def typni_si():
    return int(input("Jaký je tvůj typ? "))


def cislo_pc():
    return randrange(1000, 9999)





main()

