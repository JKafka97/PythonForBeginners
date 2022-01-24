# pomocí listu udělej kámen nužky papir (list + while)

from random import choice

seznam_moznosti = ['kámen', 'nůžky', 'papír']
def main():
    tip = tip_stroje()
    print(tip)

def otazka_uzivateli():
    return input('Naval odpoveď. ')

def porovnani(odpoved_uzivatele, tip_stroje):
    if odpoved_uzivatele == tip_stroje:
        print('Ještě jednou.')
    elif odpoved_uzivatele == 'kámen' and tip_stroje == 'papír':
        print('Prohrál jsi.')
    

def tip_stroje():
    return choice(seznam_moznosti)


main()




# dokončit doma