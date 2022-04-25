#vyrob kalkulacku, která každé číslo vypíše zrcadlove (123 => 321) (index + while)

def main():
    jednicka = prvni_cislo()
    znaminko = znamenko()
    dvojka = druhe_cislo()
    vysledek = vypocet(jednicka, znaminko, dvojka)
    print(str(vysledek)[::-1])

def prvni_cislo():
    return int(input("První číslo? "))

def znamenko():
    return input("Znaménko? ")

def druhe_cislo():
    return int(input("Druhé číslo? "))

def vypocet(jednicka, znaminko, dvojka):
    if znaminko == "x":
        return jednicka * dvojka
    elif znaminko == ":":
        return jednicka / dvojka
    elif znaminko == "+":
        return jednicka + dvojka
    elif znaminko == "-":
        return jednicka - dvojka

main()