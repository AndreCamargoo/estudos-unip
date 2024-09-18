import math

# Recebendo as coordenadas dos pontos
xb = int(input("Digite o ponto xb: "))
xa = int(input("Digite o ponto xa: "))

yb = int(input("Digite o ponto yb: "))
ya = int(input("Digite o ponto ya: "))

# Calculando a distância
distancia = math.sqrt((xb - xa)**2 + (yb - ya)**2)

# Exibindo o resultado
print("A distância entre os pontos é:", distancia)