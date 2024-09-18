import random

"""
    Exercício 3: Escreva um loop for que percorra os números de 1 a 20 e
    imprima apenas os números ímpares
"""
print("------- Exercício 3 -------")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
print("---------------------------")


""" 
    Exercício 4: Crie um loop while que continue pedindo ao usuário para inserir uma palavra 
    até que ele insira "sair". 
"""
print("------- Exercício 4 -------")
for i in range(10):
    if i % 2 != 0:
        continue
    print(i)
print("---------------------------")


""" 
    Exercício 5: Escreva um código que utilize break para sair de um loop infinito 
    quando um número aleatório entre 1 e 10 seja igual a 7. 
"""
print("------- Exercício 5 -------")
n = random.randint(1, 20)
print("O número gerado foi:", n)
for i in range(20):
    if  i == n:
        print(f"Cheguei ao número {n}")
        break
print("---------------------------")


""" 
    Exercício 6: Escreva um loop for que percorra uma lista de números e use continue para pular a 
    impressão dos números divisíveis por 3. 
"""
print("------- Exercício 6 -------")
for i in range(20):
    if i % 3 == 0:
        print(f"{i} % 3 = {i%3}")
        continue
print("---------------------------")


""" 
    Exercício 8: Escreva um programa que use uma estrutura while para calcular a soma 
    dos números de 1 a 100. 
"""
print("------- Exercício 8 -------")
for i in range(100):
    print(f"1+{i} = {1+i}")
print("---------------------------")


""" 
    Exercício 9: Crie um loop for que percorra uma lista de strings e imprima a string de maior comprimento.  
"""
print("------- Exercício 9 -------")
palavras = ["andre", "luciano", "professor", "sala", "estudo", "estudo"]

palavraMaior = ''
qtCaracteres = 0

for palavra in palavras:
    # tamanho_palavra = len(palavra)
    qt = 0

    for letra in palavra:
        qt += 1

    if (qt > qtCaracteres):
        palavraMaior = palavra
        qtCaracteres = qt

    print(f"A maior palavra é {palavraMaior} com tamanho = {qtCaracteres}")
print("---------------------------")