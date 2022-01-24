#pomocí vlastních metod nadefinuj kroky na cestu do lesa (def + while)
pocet_kroku = 0

def cesta_do_lesa(pocet_kroku):
    while pocet_kroku < 10:
        print('Ušel jsem', pocet_kroku, 'kroky rovně.')
        pocet_kroku += 1
    

cesta_do_lesa(pocet_kroku)