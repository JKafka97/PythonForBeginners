#pomocí vlastních metod nadefinuj kroky na cestu do lesa (def + while)

# def podaniCaje():
#     print("bez pro konev")
#     print("nejsem kreativní")

# podaniCaje()

def main():
    cesta_do_lesa()

def cesta_do_lesa():
    chozeni = "ano"
    while chozeni == "ano":
        chozeni = input("chceš chodit? ")
        print("vyjdi z chaty")
        print("urči si směr")
        print("jdi směrem ke stromům")
        print("jak budes mezi stromama")

main()