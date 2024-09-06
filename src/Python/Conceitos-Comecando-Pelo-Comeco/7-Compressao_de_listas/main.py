"""
    Compressão de listas ( List Comprehension )
"""

# Forma 1: Sem usar compressão de lista
numeros = [1, 2, 3, 4, 5]
novos_numeros = []

for n in numeros:
    novos_numeros.append(n*2)

print(novos_numeros)

# Forma 2: maneira compacta e elegante
numeros = [1, 2, 3, 4, 5]

numeros_dobrados = [n*2 for n in numeros]
print(numeros_dobrados)

# Buscar nomes em uma lista
nomes = ['André', 'Ana', 'Luciano', 'Willian', 'Henrique', 'Japones (prometida)']

# Filtrar nomes que começam com 'A'
nomes_com_a = [nome for nome in nomes if nome.startswith('A')]
print(nomes_com_a)

# Colocando as palavras em maiúsculas
palavras = ['python', 'java', 'c++', 'javascript']

palavras_maiusculas = [palavra.upper() for palavra in palavras]
print(palavras_maiusculas)

# Achatar Lista de listas
listas_aninhadas = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
lista_flat = [item for sublista in listas_aninhadas for item in sublista]
print(lista_flat)

# Manual
listas_aninhadas = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
nova_lista_aninhadas = []

for n1 in listas_aninhadas:
    for n in n1:
        nova_lista_aninhadas.append(n)

print(nova_lista_aninhadas)

# Função para auxiliar
numeros = [1, 2, 3, 4, 5]

def dobro(numero):
    return numero * 2

numeros_dobrados = [dobro(n) for n in numeros]
print(numeros_dobrados)

# Mesmo resultado, porém mais verboso
numeros_dobrados = []
for n in numeros:
    numeros_dobrados.append(dobro(n))

print(numeros_dobrados)

# Somentes nomes que iniciam com A maiúsculas
nomes = ['andré', 'ana', 'luciano', 'willian', 'henrique', 'japones (prometida)', 'alberto']

nomes_maiusculos_a = [nome.capitalize() for nome in nomes if nome.startswith('a') or nome.startswith('l')]

# Ordena a lista
nomes_maiusculos_a.sort()
print(nomes_maiusculos_a)

