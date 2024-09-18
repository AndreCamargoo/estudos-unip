peso = float(input('Informe seu peso em kg: '))
altura = float(input('Informe sua altura em metros: '))

calc = peso / (altura*altura)

if calc < 18.5:
    print("Você está abaixo do peso. (grau: 0)")
elif 18.5 <= calc < 24.9:
    print("Seu peso está normal. (grau: 0)")
elif 25 <= calc < 29.9:
    print("Você está com sobrepeso. (grau: 1)")
elif 30 <= calc < 39.9:
    print("Você está com obesidade. (grau: 2)")
else:
    print("Você está com obesidade. (grau: 3)")