


def main():
    try:
        strana = int(otazka())
        obsah = strana * strana
        print('Obsah tvého čtverce je', obsah, 'cm2')
    except:
        main()


def otazka():
    return input('Zadej velikost strany čtverce v centimetrech: ')


main()