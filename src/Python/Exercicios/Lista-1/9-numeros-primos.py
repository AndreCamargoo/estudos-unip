numero = int(input("Digite um número: "))  # Pede ao usuário para digitar um número
eh_primo = True  # Assumimos inicialmente que o número é primo

if numero < 2:  # Números menores que 2 não são primos
    eh_primo = False
else:
    for i in range(2, numero):  # Verifica divisores de 2 até (n-1)
        print(i, numero)
        if numero % i == 0:  # Se o número é divisível por i, não é primo
            eh_primo = False
            break  # Interrompe o loop se encontrar um divisor

if eh_primo:  # Se não encontrou divisores, o número é primo
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")
