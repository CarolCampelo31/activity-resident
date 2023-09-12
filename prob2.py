#Faça uma função recursiva que receba um número inteiro positivo par N e 
#imprima todos os números pares de 0 até N em ordem decrescente.
n = int(input())
i=0
for i in range (n,-1,-1):
    if i%2 ==0:
        print (i)