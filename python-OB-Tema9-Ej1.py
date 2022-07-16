listaPaises = []
cantidadDePaises = int(input('Diga cuantos países ingresara: '))

for i in range(cantidadDePaises):
    pais = input('Ingrese el pais: ')
    listaPaises.append(pais)
    i = i + 1

listaSinDuplicados = set(listaPaises)

listaPaisesOrdenada = sorted(listaSinDuplicados)

listaFinal = ', '.join(listaPaisesOrdenada)

print(listaFinal)
