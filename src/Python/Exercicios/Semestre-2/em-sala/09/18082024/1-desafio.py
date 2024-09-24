lista =  [2,3,5,1,7,29]

par = 0
impar = 0

for l in lista:
    if l % 2 == 0:
        par +=1
    else:
        impar +=1
        
print(par)
print(impar)

# Modo 2

lista = [2, 3, 5, 1, 7, 29]

par = sum(1 for x in lista if x%2 == 0)
impar = sum(1 for x in lista if x%2 != 0)

print(par)
print(impar)