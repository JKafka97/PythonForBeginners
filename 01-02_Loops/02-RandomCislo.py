#Typni si číslo od 1 do 5! (while + random)
#hra si jednou tipne číslo, opakovaně se na číslo bude ptát

from  random import  randint

def main():
    odpoved_uzivatel = otazka_na_cislo()
    tip_pocitac = tip()
    while odpoved_uzivatel != tip_pocitac:
        continue

def otazka_na_cislo():
    return input("jaké je to číslo")

def tip():
    return randint(1, 5)

main()