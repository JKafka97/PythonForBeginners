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
    if maso=="ano" and paprika=="ano" and rajce=="ne" and vkus=="tak napůl":
        print("Udělej topinec! ")
    elif maso=="ano" and rajce=="ano" and paprika=="ne" and vkus=="dobrý":
        print("Bloňka jen pro tebe!")
    elif maso=="ne" and paprika=="ano" and rajce=="ano" and vkus=="žádný":
        print("Je mi tě líto, ale musíš si dát lečo :( ")
    elif maso=="ne" and rajce=="ne" and paprika=="ne" and vkus=="žádný" or vkus=="tak napůl" or vkus=="dobrý":
        print("Tak tady ani bůh nepomůže")
    elif maso=="ano" and rajce=="ne" and paprika=="ne" and vkus=="žádný" or vkus=="tak napůl" or vkus=="dobrý":
        print("Tak tady ani bůh nepomůže")
    elif maso=="ne" and rajce=="ano" and paprika=="ne" and vkus=="žádný" or vkus=="tak napůl" or vkus=="dobrý":
        print("Tak tady ani bůh nepomůže")
    elif maso=="ne" and rajce=="ne" and paprika=="ano" and vkus=="žádný" or vkus=="tak napůl" or vkus=="dobrý":
        print("Tak tady ani bůh nepomůže")
    elif maso=="ano" and rajce=="ano" and paprika=="ano" and vkus=="dobrý":
        print("Doporučuji Boloňku")
    elif maso=="ano" and rajce=="ano" and paprika=="ano" and vkus=="tak napůl":
        print("Udělej si topinec!")
    elif maso=="ano" and rajce=="ano" and paprika=="ano" and vkus=="žádný":
        print("Udělej si lečo ty barbare bez vkusu")
    

main()