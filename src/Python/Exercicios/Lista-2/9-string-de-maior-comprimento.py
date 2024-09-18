listaPalavras = ["apple", "banana", "cherry", "abacaxi"]
maiorPalavra = "Nao sei"
tamanhoMaiorPalavra = 0

for palavra in listaPalavras:
  tamanho = 0
  
  for letra in palavra:
    tamanho = tamanho + 1
  
  if (tamanho > tamanhoMaiorPalavra):
    maiorPalavra = palavra
    tamanhoMaiorPalavra = tamanho
    
  print(f"Palavra: {palavra}")
  print(f"Tamanho: {tamanho}") 
  print(f"Maior Palavra: {maiorPalavra}")
  print("-"*60) 
  
print(f"A maior palavra é: {maiorPalavra} com tamanho = {tamanhoMaiorPalavra}")
