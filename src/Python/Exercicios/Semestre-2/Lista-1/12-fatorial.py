numero = int(input("Digite um número: "))
fatorial = 1


for i in range(1, numero + 1): 
    print(f'fatorial {fatorial} * {i}')

    fatorial *= i  


print(f"O fatorial de {numero+1} é: {fatorial}")

