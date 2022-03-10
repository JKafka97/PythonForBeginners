#vyrob kalkulacku, která každé číslo vypíše zrcadlove (123 => 321) (index + while)
# tvoje_mama = '123456789'

# print(tvoje_mama[2])
# print(tvoje_mama[2:6])                  #počáteční 2,sekvence - poslední člen se nepočítá
# print(tvoje_mama[2:8:2])                # třetí číslo je krok o kolik se to posune

# print(tvoje_mama[::-1])


def main():
    prvni_cislo, druhe_cislo = otazka_cislo()
    odpoved = otazka_druh_operace()
    if odpoved == '+':
        print(str(prvni_cislo + druhe_cislo)[::-1])
    elif odpoved == '-':
        print(str(prvni_cislo - druhe_cislo)[::-1])
    elif odpoved == '*':
        print(str(prvni_cislo * druhe_cislo)[::-1])
    elif odpoved == '/':
        print(str(prvni_cislo / druhe_cislo)[::-1])

def otazka_cislo():
    prvni_cislo = int(input('Zadej první číslo: '))
    druhe_cislo = int(input('Zadej druhé číslo: '))
    return prvni_cislo, druhe_cislo

def otazka_druh_operace():
    return input('Co chceš dělat? +, -, *, / ')

main()