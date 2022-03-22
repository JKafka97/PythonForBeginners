#napiš motivační dopis s více použitím prom. pomocí .format()
pozice = "Kvalita provozu"
skola = "Univerzity Kralovy"
vlastnosti = "spolehlivý, pečlivý, pracovitý a dochvělný"
jmeno = "Mgr. Jan Kafka"
dopis = """Vážená paní, vážený pane, 

velice mě zaujala vámi nabízená pozice {0}, na stránce www.jobs.cz.
Rád bych se připojili k vašemu týmu. 

Jsem absolvent {1}, mám dlouho letou praxi v oboru s mnoha kurzy a
certifikacemi. Podrobnosti najdete v mém životopisu.

Rád pracuji v kolektivu a velice mě zajímají nové dovednosti a 
zkušenosti. Jsem velice {2}.
Chtěl bych u vás využít karierního růstu, stále se rozvíjet a 
vylepšovat své znalosti.

Velice se těším na naše setkání, kde bychom mohli probrat mé další
možnosti které mi Vaše firma nabízí.

S pozdravem

{3} """.format(pozice, skola, vlastnosti, jmeno)
print(dopis)