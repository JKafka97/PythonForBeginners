#zeptej se uživatele na parametry a vypočítej mu obsah čtvrce i s odpovědí (použíj .Format())

strana = int(input('Zadej délku strany v centimetrech: '))
obsah_ctverce = 'Obsah čtverce se stranou {velikost} cm je {vypocet} cm2'.format(velikost = strana, vypocet = strana * strana)
print(obsah_ctverce)