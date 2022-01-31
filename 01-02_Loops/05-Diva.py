# vypismenkuj všechna slova od uživatele (for + list)

def main():
    odpoved = pozadavek()
    for i in odpoved:           # procházecí cyklus, projde všechny prvky té dané věci
        print(i+ 'a')

def pozadavek():
    return input('Co chceš? ')


main()