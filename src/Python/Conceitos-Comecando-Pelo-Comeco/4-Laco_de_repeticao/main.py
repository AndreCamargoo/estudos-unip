"""
    Laço de repetição
"""

def enviaEmail(cliente):
    print(f'Email enviado para o cliente {cliente}')

clientes = ['andre', 'luciano', 'joao', 'ana', 'jose', 'maria'] # lista

for cliente in clientes:
    enviaEmail(cliente)
 
# Retonar o indice de cada interação   
for i, cliente in enumerate(clientes):
    enviaEmail(cliente)

print('\n')

# Parar a execução quando chegar a 2
for i, cliente in enumerate(clientes):
    if i == 2:
        break
    enviaEmail(cliente)

print('\n')
###################### END FOR ####################################

tabulada = 9
for i in range(1,11):
    resultado = tabulada*i
    print(f'{tabulada}*{i}={resultado}')

numero = 1
tabulada = 8

print('\n')

while numero < 11:
    resultado = tabulada*numero
    print(f'{tabulada}*{numero}={resultado}')
    numero += 1

print('\n')

# Para a execução
numero2 = 1
tabulada = 6  
while numero2 < 11:
    if numero2 == 3:
        break
    resultado = tabulada*numero2
    print(f'{tabulada}*{numero2}={resultado}')
    numero2 += 1

print('\n')

# Pula a execução
numero3 = 1
tabulada = 6  
while numero3 < 11:
    if numero3 == 3:
        numero3 += 1
        continue
    resultado = tabulada*numero3
    print(f'{tabulada}*{numero3}={resultado}')
    numero3 += 1