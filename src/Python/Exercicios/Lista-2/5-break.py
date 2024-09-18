import random

numero = 0
while True:
    numero = random.randint(1, 10) # gerar número aleatório entre 1 e 10 
    print(numero)
    
    if numero == 7:
        break