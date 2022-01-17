princ_hezky = input('Je princ hezký?')
princ_chytry = input('Je princ chytrý?')
if princ_hezky == 'ano' and princ_chytry == 'ne':
    print('Fajn')
elif princ_hezky == 'ano' and princ_chytry == 'ano':
    print('Dobře pro tebe.')
elif princ_hezky == 'ne' and princ_chytry == 'ano':
    print('Cool')
elif princ_hezky == 'ne' and princ_chytry == 'ne':
    print('To je mi tě líto')
else:
    print('Ne to tvoje máma')
