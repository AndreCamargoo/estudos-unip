"""
    Uma string é uma sequência de caracteres, semelhante a uma lista de caracteres.

    No entanto, enquanto listas em Python são mutáveis (podem ser alteradas),
    strings são imutáveis (não podem ser alteradas uma vez criadas).

    Você pode acessar, cortar e manipular strings de maneira semelhante às listas,
    mas lembre-se de que operações que tentam modificar uma string criam uma nova string.
"""

# Definindo uma string de exemplo
texto = "aula python, bora pra cima"

# Acessando o primeiro caractere da string
print(texto[0])

# Extraindo um segmento da string do índice 5 até o 7 (não inclui o 7)
print(texto[5:9])

# Extraindo um segmento da string a partir do índice 5 até o final
print(texto[5:])

# Extraindo um segmento da string do início até o índice 5 (não inclui o 5)
print(texto[:5])

# Contando o número total de caracteres na string
print(len(texto))

# Contando quantas vezes a letra 'a' aparece na string (difere maiúsculas de minúsculas)
print(texto.count('a'))

# Contando quantas vezes a letra 'y' aparece na faixa de índices de 5 a 7 (não inclui o 7)
print(texto.count('y', 5, 7))

# Encontrando o índice da primeira ocorrência da substring "Python" (retorna -1 se não encontrar)
print(texto.find("Python"))

# Convertendo toda a string para maiúsculas
print(texto.upper())

# Convertendo toda a string para minúsculas
print(texto.lower())

# Capitalizando a primeira letra da string (a primeira letra fica maiúscula e o restante minúsculo)
print(texto.capitalize())

# Capitalizando a primeira letra de cada palavra na string
print(texto.title())

# Dividindo a string em uma lista de palavras, usando espaços como delimitadores padrão
print(texto.split())

# Dividindo a string em uma lista de palavras, usando a vírgula como delimitador
print(texto.split(','))

# Unindo uma lista de palavras em uma única string, com hífen como separador
lista_de_palavras = texto.split()
print('-'.join(lista_de_palavras))

# Removendo espaços em branco no início e no fim da string
novo_texto = '  aula python, bora pra cima    '
print(novo_texto.strip())

# Removendo espaços em branco apenas à direita da string
novo_texto = '  aula python, bora pra cima    '
print(novo_texto.rstrip())

# Removendo espaços em branco apenas à esquerda da string
novo_texto = '  aula python, bora pra cima    '
print(novo_texto.lstrip())
