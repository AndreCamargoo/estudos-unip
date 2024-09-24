def calcCorrente(v, r1, r2, r3):
    req1 = (r2*r3) / (r2+r3)    
    return v / (r1+req1)

volts = int(input("Digite a voltagem: "))
r1 = int(input("Digite R1: "))
r2 = int(input("Digite R2: "))
r3 = int(input("Digite R3: "))

corrente = calcCorrente(volts, r1, r2, r3)

print(corrente)

