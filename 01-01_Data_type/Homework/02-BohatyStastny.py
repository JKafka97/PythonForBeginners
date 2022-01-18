#štěstí == bohatství ?

stastny = input('Jsi štastný? ')
bohaty = input('Jsi bohatý? ')
if stastny == 'ano' and bohaty == 'ano':
    print('Tak to jsi štastný člověk')
elif stastny == 'ano' and bohaty == 'ne':
    print('Najdi si lépe placenou práci.')
elif stastny == 'ne' and bohaty == 'ano':
    print('Kup si štěně. To tě rozveselí.')
elif stastny == 'ne' and bohaty == 'ne':
    print('Blbý.')
else:
    print('Máš odpovídat ano/ne, hlupáku.')
