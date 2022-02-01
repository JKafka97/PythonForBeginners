# kolik procent koláče chceš sežrat?

# rozdíl if a elif

kolac = int(input("kolik procent kolace chces sezrat"))

if kolac < 15:
    print("to je v pohodě")

elif kolac < 50:
    print("tak akorát")


elif kolac < 70:
    print("to už je dost")


elif kolac < 100:
    print("prase")

else:
    print("nechápu")