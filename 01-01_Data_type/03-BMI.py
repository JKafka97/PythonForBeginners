#vytvoř BMI kalkulačku 

vyska = int(input("jak jsi vysoky"))
vaha = int(input("kolik vážíš"))
vyska_v_metrech = vyska/100
vypocet = vaha/(vyska_v_metrech*vyska_v_metrech)

print(vypocet,"je tvoje BMI")