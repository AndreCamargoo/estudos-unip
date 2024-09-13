notas = [float(x) for x in input('Digite os números separados por espaço: ').split('|')]
qtNotas = len(notas)
valorNota = 0.0


for n in notas:
    if valorNota > 0:
        valorNota += n
    else:
        valorNota = n


print(valorNota / qtNotas)