# Solicita ao usuário para inserir o peso em kg e a altura em metros


peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))


imc = peso / (altura * altura) # Calcula o IMC usando a fórmula


print(f"Seu IMC é: {imc:.2f}") # Exibe o resultado do IMC


# Categoriza o IMC de acordo com as faixas estabelecidas
if imc < 18.5:
    print("Você está abaixo do peso. (grau: 0)")
elif 18.5 <= imc < 24.9:
    print("Seu peso está normal. (grau: 0)")
elif 25 <= imc < 29.9:
    print("Você está com sobrepeso. (grau: 1)")
elif 30 <= imc < 39.9:
    print("Você está com obesidade. (grau: 2)")
else:
    print("Você está com obesidade. (grau: 3)")
