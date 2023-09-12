a = int(input('Digite a quantidade de pessoas:\n'))
b = int(input('Selecione a cidade escolhida: (1 - Pipa e 2 - Fortaleza)\n'))
c = int(input('Digite a quantidade de quartos:\n'))
    

if b == 1:
    if c == 2:
        precoP = 600/a + 75
        precoT = 600 + 75*a
    else:
        precoP = 900/a + 75
        precoT = 900 + 75*a
if b == 2:
    if c == 3:
        precoP = 950/a + 60
        precoT = 950 + 60*a
    else:
        precoP = 1120/a + 60
        precoT = 1120 + 60*a
        
print('Valor total da viagem: R$ %.2f'%(precoT))
print('Valor por pessoa: R$ %.2f'%(precoP))