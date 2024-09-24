kms = [float(x) for x in input('Digite os km separados por espaços: ').split()]
tempo = [float(x) for x in input('Digite os tempos separado por espaços: ').split()]

sumKm = 0
sumTempo = 0

for k in kms:
    sumKm += k
    
for t in tempo:
    sumTempo += t

velocidade_media = sumKm / sumTempo
print(f'Velocidade média foi {velocidade_media}')

# Modo 2

velocidade_media2 = sum(kms) / sum(tempo)
print(f'Velocidade média foi {velocidade_media2}')

# Modo 3

def calculaMedia(dic):
    kms = 0
    tempo = 0
    
    for d in dic:
        kms += d['kms']
        tempo += d['tempo']
    
    return kms / tempo

print(
    calculaMedia([
        {'kms': 100, 'tempo': 5},
        {'kms': 200, 'tempo': 10},
    ])
)