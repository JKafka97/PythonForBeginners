#lečo (paprika, rajče, žádný vkus) boloňka (rajče, maso, dobrý vkus) topinka (maso, paprika, vkus tak na půl)

#(if a metody)

def main():
    vkus = otazka_vkus()
    maso = otazka_maso()
    paprika = otazka_paprika()
    rajce = otazka_rajce()
    recept(vkus, maso, paprika, rajce)

def otazka_paprika():
    return input("Máš papriku? ")

def otazka_rajce():
    return input("Máš rajče? ")

def otazka_maso():
    return input("Máš maso? ")

def otazka_vkus():
    return input("Jaký máš vkus? ")
    
def recept(vkus, maso, paprika, rajce):
    if maso=="ano" and paprika=="ano" and vkus=="tak napůl":
        print("Udělej topinec! ")
    elif maso=="ano" and rajce=="ano" and vkus=="dobrý":
        print("Boloňka jen pro tebe!")
    elif paprika=="ano" and rajce=="ano" and vkus=="žádný":
        print("Je mi tě líto, ale musíš si dát lečo :( ")
    else:
        print("Tak tady ani bůh nepomůže")
        
main()
