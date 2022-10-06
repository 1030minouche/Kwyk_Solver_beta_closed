import time as t
from cmath import sqrt


def solve():
    delta = 0
    print("Une equation du second degré")
    t.sleep(0.2)
    print("Est sous la forme ax**2+bx+c")
    a = int(input("Que vaut a ? "))
    b = int(input("Que vaut b ? "))
    c = int(input("Que vaut c ? "))
        #calcul delta
    delta = (b**2)-(4*a*c)
    if delta > 0:
        x1 = (-b-sqrt(delta))/(2*a)
        x2 = (-b+sqrt(delta))/(2*a)
        print ("X1 = ",x1)
        print ("X2 = ",x2)

    if delta == 0:
        x1 = -b/2*a
        print("L'uniqye solustion est, x = ",x1)

    if delta < 0:
        print("Il n'a pas de solution à ton equation !")