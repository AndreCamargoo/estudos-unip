def calc(v, r1, r2):
    # Calcula a corrente total no circuito
    req = v / (r1 + r2)
    
    # Calcula a tensão em R1 e R2
    vr1 = req * r1
    vr2 = req * r2
    
    return req, vr1, vr2

'''

   +-------[R1]------+
   |                 |
   |                 [R2]---+
   |                 |
   |                 |
  V_in              V_out
  
'''

# Solicita a voltagem e os resistores ao usuário
volts = int(input("Digite a voltagem: "))
r1 = int(input("Digite R1: "))
r2 = int(input("Digite R2: "))

# Chama a função calc e armazena os resultados
result = calc(volts, r1, r2)

# Exibe os resultados
print(f'Corrente: {result[0]} A')
print(f'VR1: {result[1]} V')
print(f'VR2: {result[2]} V')