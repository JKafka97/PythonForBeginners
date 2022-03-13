#vytvoř slovník s otázkou a správnou odpovědí
#pomocí random.shuffle vyber postupně všechny otázky
#napočítej kolik jich bylo dobře odpovězeno a kolik ne

#(for + dic + while)    zamyslet se co dělá for cyklus, stejně jako je v Diva

from random import shuffle

print('Vítej v kvízu o seriálu Simpsons')

hra = {"Všechny postavičky v tomto seriálu mají zvláštní barvu kůže. Jakou?" : "žlutou",
        "Líza ráda hraje na jeden hudební nástroj. Na který?" : "saxofon",
        "V seriálu vystupuje i jeden klaun. Jak se jmenuje?" : "Krusty"}

dobre = 0
spatne = 0

def main(dobre, spatne):
    shuffle(list(hra.keys()))
    for otazka in hra.keys():
        odpoved_uzivatele = otazka_na_uzivatele(otazka)
        if odpoved_uzivatele == hra[otazka]:
            dobre += 1
        elif odpoved_uzivatele != hra[otazka]:
            spatne += 1
    print('Máš tolik správně', dobre , 'a tolik špatně', spatne )

def otazka_na_uzivatele(otazka):
    return input(otazka)
   


main(dobre, spatne)
    
