#vyrob kalkulacku, která každé číslo vypíše zrcadlove (123 => 321) (index + while)





x = int(input("Zadejte 1. číslo : "))
znamenko = str(input("Zadejte znaménko : "))
y = int(input("Zadejte 2. číslo : "))

if znamenko == "+" :
    vysledek1 = (int(x + y))
    print(str(vysledek1)[::-1])
elif znamenko == "-" :
    vysledek2 = (int(x - y))
    print(str(vysledek2)[::-1])
elif znamenko == "*" :
    vysledek3 = (int(x * y))
    print(str(vysledek3)[::-1])
elif znamenko == "/" :
    vysledek4 = (int(x / y))
    print(str(vysledek4)[::-1])
