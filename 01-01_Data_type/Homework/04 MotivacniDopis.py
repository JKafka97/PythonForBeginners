
dopis = 'Vážená paní / Vážený pane, obracím se na Vás s žádostí o zaměstnání u Vaší společnosti {spolecnost} na pracovní pozici {poz}.'
kecy_1 = 'V současné době pracuji jako bordel mama. Získala jsem zde mnohé zkušenosti, které bych ráda přenesla do Vaší společnosti a byla pro vás co největším přínosem.Jsem zvyklá pracovat profesionálně a svědomitě. Dokážu řídit tým lidí, naladit je na pozitivní energii a nastavit pracovní plán tak, aby se splnily všechny vytyčené cíle.'
kecy_2 = 'Podrobné údaje o mém vzdělání a pracovních zkušenostech uvádím v přiloženém životopise.V případě Vašeho zájmu prosím zašlete odpověď na výše uvedenou adresu nebo mne kontaktujte na výše uvedeném telefonním čísle.'
kecy_3 = 'Děkuji a těším se na možnou spolupráci s Vámi.'

kecy_4 = 'V Brně 19.1.2038'
kecy_5 = 'S úctou'

kecy_6 = '{podpis}'

firma = input('Název společnosti: ')
pozice = input('Pozice? ')
jmeno = input('Jméno? ')
print(dopis.format( spolecnost = firma, poz = pozice))
print(kecy_1)
print(kecy_2)
print(kecy_3)
print(kecy_4)
print(kecy_5)
print(kecy_6.format( podpis = jmeno))
