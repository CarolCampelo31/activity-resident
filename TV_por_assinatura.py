pactE = input()
pgtE = input()
pact = pactE.lower()
pgt = pgtE.lower()

a = 80.80
b = 100.40
c = 130.23
d = 215.50

while pgt == 'débito automático':
    if pact == 'básico':
        mens = a - (0.05*a)
        UpCan = 32 + 6
    if pact == 'entretenimento':
        mens = b - (0.05*b)
        UpCan = 55 + 6
    if pact == 'multicultural':
        mens = c - (0.1*c)
        UpCan = 70 + 11
    if pact == 'completo':
        mens = d - (0.1*d)
        UpCan = 112 + 11
print ('%.2f'%(mens))
print (UpCan)