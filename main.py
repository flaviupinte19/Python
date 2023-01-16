def sumanumere():
    print('Introduceti primul numar, a')
    a = input()
    print('Numarul introdus a=', a)
    print('Introduceti al doilea numar, b')
    b = input()
    print('Numarul introdus b=', b)
    print('a+b=', int(a)+int(b))


def diferentanumere():
    print('Introduceti primul numar, a')
    a = input()
    print('Numarul introdus a=', a)
    print('Introduceti al doilea numar, b')
    b = input()
    print('Numarul introdus b=', b)
    print('a-b=', int(a)-int(b))


def inmultirenumere():
    print('Introduceti primul numar, a')
    a = input()
    print('Numarul introdus a=', a)
    print('Introduceti al doilea numar,b')
    b = input()
    print('Numarul introdus b=', b)
    print('a*b=', int(a)*int(b))


def impartirenumere():
    print('Introduceti primul numar, a')
    a = input()
    print('Numarul introdus a=', a)
    print('Introduceti al doilea numar,b')
    b = input()
    print('Numarul introdus b=', b)
    print('a/b=', int(a) / int(b))


def ariatriunghiului():
    print('Introduceti prima cateta, c1')
    c1 = input()
    print('Prima cateta c1=', c1)
    print('Introduceti al doilea numar, c2')
    c2 = input()
    print('A doua cateta c2=', c2)
    print('Aria trunghiului=', int(c1)*int(c2)/2)


def perimetrultriunghiului():
    print('Introduceti prima latura, ab')
    ab = input()
    print('Prima latura ab=', ab)
    print('Introduceti a doua latura ,bc')
    bc = input()
    print('A doua latura bc=', bc)
    print('Introduceti a treia latura, ac')
    ac = input()
    print('A treia latura ac=', ac)
    print('Perimetrul triunghiului=', int(ab)+int(bc)+int(ac))

if __name__ == "__main__":
   sumanumere()
   diferentanumere()
   inmultirenumere()
   impartirenumere()
   ariatriunghiului()
   perimetrultriunghiului()