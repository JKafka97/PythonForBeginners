#lečo (paprika, rajče, žádný vkus) boloňka (rajče, maso, dobrý vkus) topinka (maso, paprika, vkus tak na půl)

prvni = input('Koupil jsi papirku? ')
druha = input('A rajče? ')
treti = input ('Maso? ')
ctvrta = input('A jaký máš vkus? Dobrý? Žádný? Nebo tak na půl? ')
if prvni == 'ano' and druha == 'ano' and treti == 'ne' and ctvrta == 'žádný':
    print('Takže budeš vařit lečo...Fuj')
elif prvni == 'ne' and druha == 'ano' and treti == 'ano' and ctvrta == 'dobrý':
    print('Jdeš se vrhnout na boloňskou omáčku, zajímavé.')
elif prvni == 'ano' and druha == 'ne'and treti == 'ano' and ctvrta == 'tak na půl':
    print('Topinka? To ujde.')
else:
    print('Blbče, máš se držet seznamu!')