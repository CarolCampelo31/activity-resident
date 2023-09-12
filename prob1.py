#Devido aos altos índices de poluição, uma cidade resolveu multar as casas que possuem mais de 2 veículos em 
#R$ 12.89 por mês por cada veículo extra. Escreva um programa que receba como entrada a quantidade de veículos 
#de várias residências, até que seja informado o valor 999, 
#e exiba o total mensal arrecadado com as multas, e a quantidade de casas multadas.

qtde = int(input())
i=0
multaTotal = 0

while qtde != 999:
    qtdExc = max(0,qtde-2)
    multaMensalRes = 12.89 * qtdExc
    if qtde>2:
        i = i+1 
    multaTotal = multaTotal + multaMensalRes
    qtde = int(input())
    
print("%.2f"%multaTotal)    
print(i)
