#Typni si číslo od 1 do 5! (while + random)
#hra si jednou tipne číslo, opakovaně se na číslo bude ptát

from random import randint

def tipni_cislo():
    return randint(1, 5)
    
def hra():
    tip = tipni_cislo()     
    while True:
        jeho_tip = int(input('Jaký je tip na číslo? '))
        if jeho_tip == tip:
            print('Dobrá práce.')
            break
        else:
            print('Smůla hlupáku.')

hra()       #vyvolat hru!
    