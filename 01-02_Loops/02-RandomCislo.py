#Typni si číslo od 1 do 5! (while + random)
#hra si jednou tipne číslo, opakovaně se na číslo bude ptát

from random import randint

def main():
    uzivatel_tip = cislo_uzivatel()
    pocitac_tip = cislo_pocitac()
    while uzivatel_tip != pocitac_tip:
        print("Špatný tip zkus znovu.")
        uzivatel_tip = cislo_uzivatel()
    print("Supr")

def cislo_uzivatel():
    return int(input("Tipni si číslo: "))

def cislo_pocitac():
    return randint(1, 5)

main()
