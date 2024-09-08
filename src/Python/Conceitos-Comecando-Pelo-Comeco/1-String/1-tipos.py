"""
    Tipos de Dados em Python
"""

print(1) # int: Um número inteiro positivo
print(0) # int: O número inteiro zero
print(-0) # int: Um número inteiro negativo, mas -0 é equivalente a 0
print('1') # string: O número 1 representado como uma sequência de caracteres

print(1.1) # float: Um número com ponto flutuante positivo
print(-1.1) # float: Um número com ponto flutuante negativo
print(-0.0) # float: Zero com ponto flutuante, o mesmo que 0.0
print('1.1') # string: O número 1.1 representado como uma sequência de caracteres

print('André "Camargo') # string: Uma string com uma aspa dupla no meio, o que pode causar um erro de sintaxe se não for escapado corretamente

print(True) # bool: O valor booleano verdadeiro
print('True') # string: A palavra "True" representada como uma sequência de caracteres

print(False) # bool: O valor booleano falso
print('False') # string: A palavra "False" representada como uma sequência de caracteres

# Como verificar o tipo de cada dado

print(type(1)) # <class 'int'>: Verifica e imprime o tipo do valor 1, que é um inteiro
print(type(1.1)) # <class 'float'>: Verifica e imprime o tipo do valor 1.1, que é um ponto flutuante
print(type('1')) # <class 'str'>: Verifica e imprime o tipo do valor '1', que é uma string
print(type(True)) # <class 'bool'>: Verifica e imprime o tipo do valor True, que é um booleano
