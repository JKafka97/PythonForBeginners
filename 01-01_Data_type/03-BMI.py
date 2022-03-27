#vytvoř BMI kalkulačku 

def main():
    vaha = otazka_vaha()
    vyska = otazka_vyska()
    vypocet(vaha, vyska)

def otazka_vaha():
    a = int(input("Jaká je tvoje váha? "))
    return a

def otazka_vyska():
    return float(input("Jaká je tvoje výška? "))

def vypocet(vaha, vyska):
    print(vaha/vyska**2)

main()