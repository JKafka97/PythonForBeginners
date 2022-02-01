# vymysli kombinace pro hezkeho/ošklivého/hloupého/chytrého

krasa = input("je princezna hezká (ano/ne)? ")
chytrost = input("je princezna chytrá (ano/ne)? ")

if krasa == "ano" and chytrost == "ano":
    print("dobrá partie")

if krasa == "ano" and chytrost == "ne":
    print("hezká blbka")

if krasa == "ne" and chytrost == "ano":
    print("Ošklivka Betty")

if krasa == "ne" and chytrost == "ne":
    print("ztracený případ")