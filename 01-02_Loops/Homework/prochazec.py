# zadam minimálně do proměnné 200 slov(knížka) a on spočítá kolik je tam velkých písmen, malých písmen, čísel, ",", ".","!".
# použiji for, držet to jako slovník
# funkční login (3 uživatele)

slovnik = {"velká" : 0, "malá" : 0, "čísla" : 0, "čárky" : 0, "tečka" : 0, "vykřičník" : 0}

def main():
    text = otazka()
    for i in text:
        if i.isupper():
            slovnik["velká"]+=1
        elif i.islower():
            slovnik["malá"]+=1
        elif i.isnumeric():
            slovnik["čísla"]+=1
        elif i == ",":
            slovnik["čárky"]+=1
        elif i == ".":
            slovnik["tečka"]+=1
        elif i == "!":
            slovnik["vykřičník"]+=1
    print('''Tvůj text obsahuje:
Velká písmena: {velka} 
Malá písmena: {mala}
Čísla: {cisla} 
Čárky: {carka} 
Tečky: {tecka} 
Vykřičníky: {vykricnik}'''.format (velka = slovnik["velká"], mala = slovnik["malá"], cisla = slovnik["čísla"], carka = slovnik["čárky"], tecka = slovnik["tečka"], vykricnik = slovnik["vykřičník"]))
 
def otazka():
    return input("Vložte svůj text: ")

main()

