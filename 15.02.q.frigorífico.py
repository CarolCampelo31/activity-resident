n = int(input())
p = 0
maior = 0
menor = 9999999999
i = 0
idmaior = 0
idmenor = 0

while i <= n-1:
    id,p = map(float,input().split())
    id = int(id)
    p = float(p)
    i = i + 1

    if p > maior:
        maior = p
        idmaior = id
    if p < menor:
        menor = p
        idmenor = id
        
print('Gordo: id: %d peso: %.2fKg'%(idmaior,maior))
print('Magro: id: %d peso: %.2fKg'%(idmenor,menor))
