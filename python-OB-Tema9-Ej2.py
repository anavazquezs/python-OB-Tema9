from functools import reduce

lista = [25, 4, 87, 96, 25, 4, 6, 1, 74]

def funciónImpares(x):
    if x % 2 == 0:
        return False
    return True

listaImpares = filter(funciónImpares, lista)


def sumaImpares(a, b):
    return a + b

sumaImpares = reduce(sumaImpares, listaImpares)

print(sumaImpares)



