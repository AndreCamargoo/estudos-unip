notas = []


for i in range(1, 4):
    nota = float(input(f"Digite a {i}ª nota: "))
    notas.append(nota)


media = sum(notas) / len(notas)


print(f"A média foi {media:.2f}")
