def masini():
    fisier = open("masini.in","r")
    linie = fisier.readline().strip().split('')
    n = linie[0]
    T = linie[1]
    timp_de_lucru = fisier.readline().strip().split('')
    fisier.close()
    n = int(n)
    T = int(T)
    timp_de_lucru.sort()
    nr_masini = 0
    i = 0
    for j in range(len(timp_de_lucru)):
        if T - int(timp_de_lucru[j]) >= 0:
            T -= int(timp_de_lucru[j])
            nr_masini += 1
        else:
            break
    scriere_fisier = open("masini.out","w")
    scriere_fisier.write(str(nr_masini))
    scriere_fisier.close()


    if __name__=="__main__":
        masini()
        #specs = list()
        #n = int(input("Numar Spectacole:"))
        # for i in range(n):
        #          oi = int(intput("Ora in."))
        #          os = int(input("Ora sf."))
        #          specs.append([oi, os])
        # specs = [(1,8], [8.10], [8,12]. [12,13], [15,17], [18,20], [17,21]]
        # spectacol(specs)