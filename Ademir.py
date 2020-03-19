import numpy as np 

#obter o tamanho da matriz um e dois
# obter a matriz um e dois.
# multiplicar as duas matrizes

l1 = int(input("Linhas de A :"))     # numero de linhas da matriz A
c1 = int(input("Colunas de A:"))     # numero de colunas da matriz A

l2 = int(input("Linhas de B :"))    # numero de linhas da matriz 2
c2 = int(input("Colunas de B:"))    # numero de colunas da matriz 2


A=np.zeros((l1,c1))#defiinir matris l1Xc1
for i in range (0,l1):
    for j in range (0,c1):
     A[i][j]=(int(input(f'Entre valor da posicao [{i},{j}] da matriz:' )))

B=np.zeros((l2,c2))#defiinir matris l2Xc2

for i in range (0,l2):
    for j in range (0,c2):
        B[i][j] = (int(input(f'Entre valor da posicao [{i},{j}] da matriz:' )))
   
print ("Matrizes A e B coletadas.")

if(l1!=c2):
    print("Multiplicação de matrizes não definida!")
else:
    C=np.zeros((l1,c2))
    for i in range(0,l1):
        for j in range(0,c2):
            for k in range(0,l1):
                C[i][j]+=A[i][k]*B[k][j]    
    print(C)
