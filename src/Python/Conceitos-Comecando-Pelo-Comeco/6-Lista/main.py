"""
    Lista: É uma estrutura de dados que armazena elementos de forma sequencial. Cada elemento na lista possui um
    índice que indica sua posição.

            ------------------- Posições ----------------------------
    Valores | 10 | 14 | 20 | 9 | 16 | ANDRÉ | 58 | TRUE | 70 | 102 |
            ---------------------------------------------------
    Índices | 0  |  1 |  2 | 3 |  4 |   5   |  6 |   7   |  8 |  9  |
            ---------------------------------------------------------
"""

# Iniciando uma lista
carros = ['Civic', 'Toro', '328 i', 'Hawal H6', 'EcoSport']
print(carros)

# Adicionando mais um elemento na minha lista
# append(): Adiciona um item ao final da lista.
carros.append('C 300')
print(carros)

# += (concatenação): Adiciona todos os itens de uma lista (ou outro iterável) ao final da lista existente.
carros += ['Ram']
print(carros)

# Adicionando um item em uma posição específica com insert():
# insert(): Adiciona um item em uma posição específica da lista. O primeiro argumento é o índice onde o item
# deve ser inserido, e o segundo argumento é o valor a ser inserido.
carros.insert(3, 'Ranger')
print(carros)

# Você pode adicionar diferentes tipos de dados à mesma lista sem problemas. Ex Boleanos, Float, Strings e etc.
carros.append(True)
print(carros)

# Removendo itens da lista
# O método pop() é usado para remover e retornar um item da lista. Se você não passar nenhum argumento para pop(),
# ele remove e retorna o último item da lista.
carros.pop()
print(carros)

# Removendo o item na posição de índice 3 (quarto item) da lista
# O índice 3 corresponde ao item 'Ranger'
del carros[3]
print(carros)

# O método remove() é usado para remover o primeiro item encontrado com o valor especificado na lista.
# Se o item não estiver na lista, ele levantará um erro ValueError:
# O valor tem que ser exato e é case-sensitive. Isso significa que a correspondência é feita exatamente como o item
# aparece na lista, incluindo maiúsculas e minúsculas.
carros.remove('EcoSport')
print(carros)

# O método count() é usado para contar quantas vezes um item específico aparece em uma lista.
carros.append('Hawal H6')
print(carros)

c = carros.count('Hawal H6')
print(c)

carros.pop()

# O método reverse() é usado para reverter a ordem dos elementos em uma lista.
# Esse método altera a lista original diretamente e não retorna uma nova lista.
carros.reverse()
print(carros)

# O método sort() é usado para ordenar os elementos de uma lista em ordem crescente.
# Assim como o método reverse(), o sort() altera a lista original diretamente e não retorna uma nova lista.
# O método sort() funciona apenas se os elementos da lista forem comparáveis (por exemplo, todos números ou todas strings).
carros.sort()
print(carros)

numeros = [5,8,15,23,52]
print(numeros)
numeros.sort()
print(numeros)

numeros.reverse()
print(numeros)

"""
    Python levantará um erro TypeError
"""
#novaLista = [True, 'André', 10]
#print(novaLista)

#novaLista.sort()
#print(novaLista)