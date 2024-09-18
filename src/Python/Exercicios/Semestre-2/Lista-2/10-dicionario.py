def parImpar(numero):    
    res = {
        0: "Par",   # Resto da divisão por 2 é 0
        1: "Ímpar"  # Resto da divisão por 2 é 1
    }
    
    return res[int(numero) % 2]

numero = input('Digite seu número: ')
print(parImpar(numero))
