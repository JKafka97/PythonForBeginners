#vypočti z minutové mzdy tu za měsíc
x = 2               #int
x = 'pondělí'       #str
x = 2.5             #float



# vek = input('Řekni mi kolik je ti let?')
# print(vek)


# print(13%2)     #zbytek po dělení
# print(13//2)    #beze zbytku

mzda_za_minutu = int(input('Kolik vyděláš za minutu?'))
mzda_za_měsíc = mzda_za_minutu * 60 * 8 * 22
print('Tvoje měsíční mzda je', mzda_za_měsíc)
