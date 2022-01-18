#zeptej se uživatele na parametry a vypočítej mu obsah čtvrce i s odpovědí (použíj .Format())

strana = int(input('Zadej délku strany v centimetrech: '))
odpoved = 'Obsah čtverce se stranou {velikost} cm je {vypocet} cm2'
print(odpoved.format(velikost = strana, vypocet = strana * strana))
