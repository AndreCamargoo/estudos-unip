lista = [int(x) for x in input("Digite os números da lista separados por espaço: ").split()]

item = int(input("Digite o número a ser encontrado: "))

encontrado = False

for i in range(len(lista)):
    if lista[i] == item: 
        print(f"Número {item} encontrado na posição {i}")
        encontrado = True 
        break  


if not encontrado:
    print(f"Número {item} não encontrado.")