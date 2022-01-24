#pomocí vlastních metod nadefinuj kroky na cestu do lesa (def + while)
pocet_kroku = 0

def cesta_do_lesa(pocet_kroku):         #definování, do závorek parametry
    while pocet_kroku < 10:             # začátek smyčky
        print('Ušel jsem', pocet_kroku, 'kroky rovně.')
        pocet_kroku += 1                #konec smyčky
    

cesta_do_lesa(pocet_kroku)