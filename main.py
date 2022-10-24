# This is a sample Python script.
from math import sqrt


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def aria(latura1, latura2,latura3):
    semiperimetru = perimetru(latura1,latura2,latura3)/2
    return sqrt(semiperimetru*(semiperimetru-latura1)*(semiperimetru-latura2)*(semiperimetru-latura3))

def perimetru(latura1, latura2, latura3):
    return latura1+latura2+latura3


if __name__ == '__main__':
    print("introduceti latura1:")
    latura1 = int(input())
    print("introduceti latura2:")
    latura2 = int(input())
    print("introduceti latura3:")
    latura3 = int(input())
    print(perimetru(latura1,latura2,latura3))
    print(aria(latura1,latura2,latura3))




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

