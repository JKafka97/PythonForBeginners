# pomocí listu udělej kámen nužky papir (list + while)

from random import choice

seznam_moznosti = ['kámen', 'nůžky', 'papír']

def main():
    tip = tip_stroje()
    tip_uzivatele = odpoved_uzivatele()
    while True:
        porovnani(tip_uzivatele, tip) 
        break
def odpoved_uzivatele():
    return input('Naval odpoveď. ') 
    
def porovnani(odpoved_uzivatele, tip_stroje):
    print(tip_stroje) 
    if odpoved_uzivatele == tip_stroje:
       print('Remíza.')     
    elif ((odpoved_uzivatele == 'kámen' and tip_stroje == 'papír') or 
          (odpoved_uzivatele == 'papír' and tip_stroje == 'nůžky') or 
          (odpoved_uzivatele == 'nůžky' and tip_stroje == 'kámen')):
        print('Prohrál jsi.')
    elif ((odpoved_uzivatele == 'kámen' and tip_stroje == 'nůžky') or
          (odpoved_uzivatele == 'papír' and tip_stroje == 'kámen') or 
          (odpoved_uzivatele == 'nůžky' and tip_stroje == 'papír')):
        print('Vyhrál jsi.')
  
def tip_stroje():
    return choice(seznam_moznosti)
    
main()
