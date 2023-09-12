#os casos bases são uma lista vazia ou a lista de um elemento
#1<=2 and asc([1,2,3,4,5])
# T and 2<=3 and asc([3,4,5])
# T and T and 3<=4 and asc([4,5])...
#lista[1:] funciona sempre fazendo a comparação excluindo o primeiro elemento da lista q foi testado no teste anterior

def ordem_asc(lista):
    if len(lista) <= 1:
        return True
    return lista[0]<=lista[1] and ordem_asc(lista[1:])
    
    
            