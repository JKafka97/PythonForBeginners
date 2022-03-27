# vymysli kombinace pro hezkeho/ošklivého/hloupého/chytrého 
def main():
    krasa = otazka_krasa()
    inteligence = otazka_inteligence()
    shrnuti(krasa, inteligence)

def otazka_krasa():
    return input("Je princezna krasná? ")

def otazka_inteligence():
    return input("Je princezna chytrá? ")

def shrnuti(krasa, inteligence):
    if krasa=="ano" and inteligence=="ano":
        print("Okeeeey lets go!!")
    elif krasa=="ano" and inteligence=="ne":
        print("Klasika čichna")
    elif krasa=="ne" and inteligence=="ano":
        print("FIZI")
    elif krasa=="ne" and inteligence=="ne":
        print("Asi Charbulka idk")

main()


