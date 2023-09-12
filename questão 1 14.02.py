primos = []
numero = 2
lismedia = []
n = 0
matriz = []

while 0 < numero <=100:
    j = 2
    while numero % j != 0 and j <= int(numero/2) :
        j += 1
	
    if j > int(numero/2):
        primos.append (numero)
    numero = numero+1
print (primos)

pares = primos[1:]

while n < 24:
    media = (pares[n] + pares[n+1]) /2
    lismedia.append(media)
    n = n + 2

print (lismedia)

matriz.append(lismedia[1:4])
matriz.append(lismedia[4:7])
matriz.append(lismedia[7:10])

print (matriz)

for i in matriz:
    print(i)









