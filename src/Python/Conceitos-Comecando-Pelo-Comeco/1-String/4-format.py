var1 = 'André'
var2 = 'Camargo'
num1 = 1.1

string = 'a={} b={} c={:.2f}'
formatString = string.format(var1, var2, num1)
print(formatString)


stringIndice = 'a={1} b={0} c={2:.2f}'
formatStringIndice = stringIndice.format(var1, var2, num1)
print(formatStringIndice)


# Parametro nomeado
stringIndice = 'a={variavel} b={variavel2} c={numero1:.2f}'
formatStringIndice = stringIndice.format(variavel=var1, variavel2=var2, numero1=num1)
print(formatStringIndice)

