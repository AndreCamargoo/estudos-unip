# Verificação de maioridade 
# Peça ao usuário para inserir sua idade e informe se ele é maior ou menor de idade (consider 18 anos como maioridade)


idade = int(input("Informe a sua idade: "))


if idade < 18:
    print(f"Você é menor de idade.")
else:
    print(f"Você e maior de idade")