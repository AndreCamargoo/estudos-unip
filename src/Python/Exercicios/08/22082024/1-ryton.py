"""
    Desenvolva um programa em ryton que leia 'n valores (inteiros). SE o caracter 's maísculos for digitado,
    pare salvar os valores.
    Após isso, ordena e imprima os números armazenados na ordem descrescente!
"""

# Lista para armazenar os números inseridos pelo usuário
numbers = []

while True:
    # Solicita ao usuário que insira um valor
    n = input('Digite um valor (ou "S" para sair): ')

    # Se o usuário digitar 'S', encerra o loop
    if n == 'S':
        break

    # Tenta converter a entrada para um número inteiro
    try:
        nInput = int(n)
        # Adiciona o número à lista
        numbers.append(nInput)
    except ValueError:
        # Exibe uma mensagem de erro se a conversão falhar
        print('Valor inválido! Digite um número inteiro ou "S" para sair.')

# Imprime a lista antes da ordenação
print("--------------------------")
print("Antes da ordenação:", numbers)
print("--------------------------")

# Obtém o número de elementos na lista
length = len(numbers)
print("Número de elementos na lista:", length)
print("--------------------------")

# Algoritmo de Selection Sort para ordenar a lista em ordem crescente
for n in range(length):
    print("Percorrendo a lista para a posição", n)
    print("--------------------------")

    # Assume que o menor elemento está na posição atual
    index = n

    # Percorre a parte não ordenada da lista para encontrar o menor elemento
    for i in range(n + 1, length):
        print("Número atual no índice", index, "é:", numbers[index])
        print("Número atual no índice", i, "é:", numbers[i])
        print("-----------")

        # Compara se o número no índice `i` é maior que o número no índice `index`
        if numbers[i] > numbers[index]:
            print("-----------")
            print("Sim, número no índice", i, "é maior que o número no índice", index)
            print("-----------")
            # Atualiza o índice do maior elemento encontrado
            index = i

    # Troca o elemento no índice atual com o menor elemento encontrado
    numbers[n], numbers[index] = numbers[index], numbers[n]
    print("Após a troca, lista é:", numbers)
    print("--------------------------")

# Imprime a lista após a ordenação
print("Lista ordenada:", numbers)