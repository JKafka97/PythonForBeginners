#pomocí vlastních metod nadefinuj kroky na cestu do lesa (def + while)

def main():
    while True:
        otazka = kam_jit()
        if otazka == "doleva":
            doleva()
        elif otazka == "doprava":
            doprava()
        elif otazka == "dopredu":
            dopredu()
        elif otazka == "konec":
            break
        else:
            print("Jdi v prdel")

def doleva():
    print("Krok doleva")

def doprava():
    print("Krok doprava")

def dopredu():
    print("Krok dopředu")

def kam_jit():
    return input("Kam mám jít? ")

main()
