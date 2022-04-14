# pomocí listu udělej kámen nužky papir (list + while)

import random

def main():
    uzivatel = volba_uzivatele()
    pocitac = volba_pocitace()
    vyhodnoceni(uzivatel, pocitac)
    
def volba_pocitace():
    list = ["kámen", "nůžky", "papír"]
    print(random.choice(list))
    
def volba_uzivatele():
    return input("Kámen, nůžky nebo papír? ")

def vyhodnoceni(uzivatel, pocitac):
    if uzivatel == "kámen" and pocitac=="nůžky" or uzivatel == "nůžky" and pocitac == "papír" or uzivatel == "papír" and pocitac == "kámen":
        print("Vyhral jsi!")
    elif uzivatel == "kámen" and pocitac == "kámen" or uzivatel == "nůžky" and pocitac == "nůžky" or uzivatel == "papír" and pocitac == "papír": 
        print("Plichta")
    elif uzivatel == "kámen" and pocitac == "papír" or uzivatel == "nůžky" and pocitac == "kámen" or uzivatel == "papír" and pocitac == "nůžky":
        print("Prohrál jsi")

main()