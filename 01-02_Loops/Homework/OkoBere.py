#vytvořím si počitadlo bodů
# bereš si každé kole kartu s hodnotou random mezi 2-10
# na konci kola si chci rozhodnot jestli chci další kartu a nebo ne
# když bude výsledek menší než 21 => vyopíšu kolik chybělo 
# když přesně => vypíšu že vyhrál
# když víc => vypíšu o kolik a že prohrál

#(while + random)

from random import randint

def main():
  otoceni = "ano"
  hrac, pocitac = 0,0
  while hrac < 21 and otoceni == "ano":
    hrac += otaceni_karty()
    pocitac += otaceni_karty()
    print("Ty máš", hrac, "Počítač má", pocitac)
    otoceni = otazka_otoceni_karty()
   
  if hrac == 21:
    print("Jsi výherce.")
  elif hrac > 21:
    print("Prohra.")
  elif pocitac > 21:
    print("Výhra.")
  else:
    if hrac > pocitac:
      print("Výhra.")
    elif pocitac > hrac:
      print("Prohra.")
    else:
      print("Vyrovnané.")
   
def otaceni_karty():
  return randint(2, 10)

def otazka_otoceni_karty():
  return input("Chceš otočit další kartu? ")

main()