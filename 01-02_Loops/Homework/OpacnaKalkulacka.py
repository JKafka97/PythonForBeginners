#vyrob kalkulacku, která každé číslo vypíše zrcadlove (123 => 321) (index + while)





x = int(input("Zadejte 1. číslo : "))
znamenko = input("Zadejte znaménko : ")
y = int(input("Zadejte 2. číslo : "))

if znamenko == "+" :
    vysledek1 = x + y
    print(str(vysledek1)[::-1])
elif znamenko == "-" :
    vysledek2 = x - y
    print(str(vysledek2)[::-1])
elif znamenko == "*" :
    vysledek3 = (x * y)
    print(str(vysledek3)[::-1])
elif znamenko == "/" :
    vysledek4 = x / y
    print(str(vysledek4)[::-1])
