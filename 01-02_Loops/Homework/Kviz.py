#vytvoř slovník s otázkou a správnou odpovědí
#pomocí random.shuffle vyber postupně všechny otázky
#napočítej kolik jich bylo dobře odpovězeno a kolik ne

#(for + dic + while)    zamyslet se co dělá for cyklus, stejně jako je v Diva


from random import shuffle

print('Vítej v kvízu o seriálu Simpsons')

hra = {"žlutou" : "Všechny postavičky v tomto seriálu mají zvláštní barvu kůže. Jakou?",
        "saxofon" : "Líza ráda hraje na jeden hudební nástroj. Na který?",
        "Krusty" : "V seriálu vystupuje i jeden klaun. Jak se jmenuje?"}

def main():
    odpoved = otazka_na_uzivatele()
    for i in odpoved:
        print(i)

def otazka_na_uzivatele():
    prvni_otazka = input(hra["žlutou"])
    druhá_otázka = input(hra["saxofon"])
    return prvni_otazka, druhá_otázka



main()
    