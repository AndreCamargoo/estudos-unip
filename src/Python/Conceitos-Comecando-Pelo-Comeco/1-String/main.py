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

# Paramêtros do print
print(10,2,5, sep='-', end='\r\n') 
print(10,2,5, sep='-', end='###') 

# 1. sep
# O parâmetro sep define o separador que será usado entre os itens que você está imprimindo. Por padrão, o separador é um espaço (' '), mas você pode definir um separador personalizado.

# 2. end
# O parâmetro end define o que será adicionado no final da saída. Por padrão, end é uma nova linha ('\n'), o que significa que o próximo print começará em uma nova linha. 
# Você pode substituir isso por qualquer string.

# 3. \r
# Significado: O \r vem de "Carriage Return" (retorno de carro). Esse caractere faz com que o cursor volte para o início da linha atual sem avançar para a próxima linha.

# 4. \n
# Significado: O \n vem de "Line Feed" (alimentação de linha). Esse caractere faz com que o cursor vá para a próxima linha.