def inlocuire():
    sir=input()
    sirnou = ""
    for caracter in sir:
        if caracter in 'aeoiu':
            sirnou += caracter.upper()
            print(caracter.upper())
        else:
            sirnou += caracter
            print(caracter)
    print(sirnou)

def scimbarecuvint():
    cuvint = input()
    index = 0
    cuvintnou = ""
    for caracter in cuvint:
        if index == 0:
            cuvintnou += caracter.upper()
            print(caracter.upper(), "Am gasit primul element", index)
        else:
            if index == len(cuvint)-1:
           cuvintnou += caracter.upper()
           print(caracter.upper(), "Am gasit ultimul element", index)
    else:
           cuvintnou += caracter
           print(caracter, index)

    index += 1
    print(cuvintnou)

def helsfort():
    lista = [34, 0, 2, 5, 3, 300, 56]
    print(lista)
    jumatate = len(lista)// 2
    print(len(lista), jumatate)
    list1 = lista[:jumatate:]
    print(list1)
    list1.sort()
    print(list1)
    list2 = lista[jumatate::]
    print(list2)
    list2.sort(reverse=True)
    print(list2)
    lista.sort()
    print(lista)
    lista.append(33)
    print(lista)
    print(lista.pop())
    print(lista)


if __name__ == "__main__":
   halfsort()
