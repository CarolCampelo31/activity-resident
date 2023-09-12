l = [['q','w','e','r','t','y','u','i','o','p'], ['a','s','d','f','g','h','j','k','l',';'],['z','x','c','v','b','n','m',',','.','/']]
l1 = []
direcao = input()
escrito = input().split()
qtd = len(escrito)
j = 0
n = 0
m = 0
k = 0

if direcao == 'R':
    for escrito[n] in l[0:4]:
        for k in range (10):
            for i in range (qtd):
                l[m][k] = l[m+1][k]
                l1.append(l[m][k])
                i = i + 1
                m = m + 1 
            k = k + 1
        n = n + 1
if direcao == 'L':
   for escrito[n] in l[0:4]:
        for k in range (10):
            for i in range (qtd):
                l[m][k] = l[m-1][k]
                l1.append(l[m][k])
                i = i + 1
                m = m + 1 
            k = k + 1
        n = n + 1
print(l1)
        