def is_primo(numero):
    # Números menores que 2 não são considerados primos.
    if numero <= 1:
        return False

    # Mostra o número e sua raiz quadrada
    print(f"Verificando se {numero} é primo. Raiz quadrada: {int(numero**0.5)}\n")

    for i in range(2, int(numero**0.5) + 1):
        print(f"Testando divisor: {i}")
        
        if numero % i == 0:
            print(f"{numero} é divisível por {i}. Não é primo.\n")
            return False
            
    print(f"\n{numero} não é divisível por nenhum número até sua raiz quadrada. É primo.\n")
    return True

# Testando a função
num = int(input("Digite um número inteiro: "))
if is_primo(num):
    print(f'{num} é um número primo.')
else:
    print(f'{num} não é um número primo.')


'''
O que é um número primo?
Um número primo é um número natural maior que 1 que só pode ser dividido por 1 e por ele mesmo sem deixar resto. Em outras palavras, ele tem exatamente dois divisores.

Exemplos de números primos
2: Divisores são 1 e 2 (é primo).
3: Divisores são 1 e 3 (é primo).
4: Divisores são 1, 2 e 4 (não é primo, pois tem 3 divisores).
5: Divisores são 1 e 5 (é primo).
6: Divisores são 1, 2, 3 e 6 (não é primo, pois tem 4 divisores).
7: Divisores são 1 e 7 (é primo).
Por que 32 não é primo?
Agora, analisando o número 32:

Os divisores de 32 são 1, 2, 4, 8, 16 e 32.
Como 32 tem mais de dois divisores (na verdade, ele tem 6 divisores), ele não é primo.
Resumo
Números primos: Têm exatamente 2 divisores (1 e ele mesmo).
Números compostos: Têm mais de 2 divisores (como 4, 6 e 32).

    Divisores de 36
    Os divisores de 36 são:

    1 (36 ÷ 1 = 36)
    2 (36 ÷ 2 = 18)
    3 (36 ÷ 3 = 12)
    4 (36 ÷ 4 = 9)
    6 (36 ÷ 6 = 6)
    9 (36 ÷ 9 = 4)
    12 (36 ÷ 12 = 3)
    18 (36 ÷ 18 = 2)
    36 (36 ÷ 36 = 1)
    
    Como você pode ver, 36 possui os seguintes divisores: 1, 2, 3, 4, 6, 9, 12, 18 e 36.
    Isso significa que 36 tem mais de dois divisores.
    
    Portanto, 36 não é um número primo, pois ele pode ser dividido por vários números além de 1 e ele mesmo.

Divisores de 11
Os divisores de 11 são:

1 (11 ÷ 1 = 11)
11 (11 ÷ 11 = 1)

Os únicos divisores de 11 são 1 e 11.

Portanto, 11 é um número primo, pois ele tem exatamente dois divisores: 1 e ele mesmo.
'''
