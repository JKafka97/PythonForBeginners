# zadam minimálně do proměnné 200 slov(knížka) a on spočítá kolik je tam velkých písmen, malých písmen, čísel, ",", ".","!".
# použiji for, držet to jako slovník
# funkční login (3 uživatele)
#

slovnik = {"velká" : 0, "malá" : 0, "čísla" : 0, "čárky" : 0}


def main():
    text = otazka()
    for i in text:
        if i == 'A' or i == 'B':
            slovnik["velká"]+=1
    print('Tvůj text obsahuje: Velká písmena:', slovnik["velká"])


def otazka():
    return input('Vložte svůj text: ')


main()