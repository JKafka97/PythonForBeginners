#vytvořím si počitadlo bodů
# bereš si každé kole kartu s hodnotou random mezi 2-10
# na konci kola si chci rozhodnot jestli chci další kartu a nebo ne
# když bude výsledek menší než 21 => vyopíšu kolik chybělo 
# když přesně => vypíšu že vyhrál
# když víc => vypíšu o kolik a že prohrál

#(while + random)

from random import randrange

def main():
    cislo_kasino()
    cislo_uzivatel()
    vypocet()

def cislo_kasino():
    return randrange(2, 10)

def cislo_uzivatel():
    return randrange(2, 10)

def vypocet():
    kasino = cislo_kasino()
    uzivatel = cislo_uzivatel()
    while uzivatel < 21:
        dalsi_karta = input('Chceš otočit kartu ano/ne? ')
        if dalsi_karta == 'ano':
            print("Máš", uzivatel, "bodů.")
            print("Krupiér má", kasino, "bodů")
            cislo_uzivatel()
            cislo_kasino()
            uzivatel = uzivatel + cislo_uzivatel()
            kasino = kasino + cislo_kasino()
            if kasino == 21:
                print('Krupiré má 21 bodů. Prohrál jsi. Vyhrává kasino.')
                break
        elif dalsi_karta == 'ne':
            break
        else:
            print('Odpovídej ano/ne')
    if uzivatel == 21:
        print('21, Black Jack. Vyhráváš!')
    elif uzivatel > 21:
        print('Prohrál jsi. Máš', uzivatel,'bodů')
    else:
        print('Chybělo ti', 21- uzivatel, 'bodů')

main()

