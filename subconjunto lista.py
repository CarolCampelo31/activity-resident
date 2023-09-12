
n = int(input('n: '))

lista1 = [n]

lista1 = input('lista1:').split(' ')

m = int(input('m: '))

lista2 = [m]

lista2 = input('lista2:').split(' ')

if set(lista1).intersection(lista2):
    print ('1')
else:
    print ('0')