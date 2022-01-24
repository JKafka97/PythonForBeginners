# pomocí listu udělej kámen nužky papir (list + while)

from random import choice

seznam_moznosti = ['kámen', 'nůžky', 'papír']

def main():
    tip = tip_stroje()
    while True:    
        otazka_uzivateli()
        tip_stroje()
        porovnani(odpoved_uzivatele, tip_stroje)                      #všechny def napsat sem

def otazka_uzivateli():
    return input('Naval odpoveď. ') 

def porovnani(odpoved_uzivatele, tip_stroje):
    odpoved_uzivatele = otazka_uzivateli()
    if odpoved_uzivatele == tip_stroje:
        print('Plichta, ještě jednou.')
    elif odpoved_uzivatele == 'kámen' and tip_stroje == 'papír' or odpoved_uzivatele == 'papír' and tip_stroje == 'nůžky' or odpoved_uzivatele== 'nůžky' and tip_stroje == 'kámen':
        print('Prohrál jsi.')
    elif odpoved_uzivatele == 'kámen' and tip_stroje == 'nůžky'or odpoved_uzivatele == 'papír' and tip_stroje == 'kámen' or odpoved_uzivatele == 'nůžky' and tip_stroje == 'papír':
        print('Vyhrál jsi.')
     

def tip_stroje():
    return choice(seznam_moznosti)


main()
