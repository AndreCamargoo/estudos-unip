lista = [int(x) for x in input('Digite os numeros separado por espaço: ').split()]

for l1 in range(len(lista)):
    for l2 in range(l1+1, len(lista)):
        if lista[l1] > lista[l2]:
            lista[l1], lista[l2] = lista[l2], lista[l1]

print(f'Lista ordenada: {lista}')