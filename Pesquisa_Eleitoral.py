a = int(input('Digite a quantidade de votos do candidato A:\n'))

b = int(input('Digite a quantidade de votos do candidato B:\n'))

c = int(input('Digite a quantidade de votos do candidato C:\n'))

n = int(input('Digite a quantidade de votos nulos:\n'))

qtdVotTot = a + b + c + n
qtdVotA = (a/qtdVotTot) * 100
qtdVotB = (b/qtdVotTot) * 100
qtdVotC = (c/qtdVotTot) * 100
qtdVotN = (n/qtdVotTot) * 100

print('Candidato A: %.3f %s'%(qtdVotA, '%'))

print('Candidato B: %.3f %s'%(qtdVotB, '%'))

print('Candidato C: %.3f %s'%(qtdVotC, '%'))

print('Votos Nulos: %.3f %s'%(qtdVotN, '%'))