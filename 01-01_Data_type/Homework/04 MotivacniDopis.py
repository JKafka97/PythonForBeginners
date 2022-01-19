firma = input('Název společnosti: ')
pozice = input('Pozice? ')
jmeno = input('Jméno? ')
motivacni_dopis = '''Vážená paní / Vážený pane, obracím se na Vás s žádostí o zaměstnání u Vaší společnosti {spolecnost} na pracovní pozici {prace}.
V současné době pracuji jako bordel mama. Získala jsem zde mnohé zkušenosti, které bych ráda přenesla do Vaší společnosti a byla pro vás co největším přínosem.Jsem zvyklá pracovat profesionálně a svědomitě. Dokážu řídit tým lidí, naladit je na pozitivní energii a nastavit pracovní plán tak, aby se splnily všechny vytyčené cíle.
Podrobné údaje o mém vzdělání a pracovních zkušenostech uvádím v přiloženém životopise.V případě Vašeho zájmu prosím zašlete odpověď na výše uvedenou adresu nebo mne kontaktujte na výše uvedeném telefonním čísle.
Děkuji a těším se na možnou spolupráci s Vámi.

V Brně 19.1.2038
S úctou

{podpis}'''.format( spolecnost = firma, prace = pozice, podpis = jmeno)
print(motivacni_dopis)
