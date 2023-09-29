import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt


L = 10

matrix = np.zeros((L, L))
cooredenadasPredadores = [[5,5]]
cooredenadasPresas = [[5,5]]

# matrixTest = np.zeros((10, 20))

# print(len(matrixTest))
# print(len(matrixTest[0]))

def mover(a,b,c):
    DecidirDirecao = np.random.randint(0, 3)
    TipoDePopulação = c
    
    if DecidirDirecao == 0:                                         #move para baixo
        print("MOVEU PARA CIMA")
        if a+1 < len(matrix):
            return print("fora para cima")
        else:
            matrix[a][b] = 0
            if TipoDePopulação == 1:
                matrix[a+1][b] = 1
            else:
                matrix[a+1][b] = 2
    if DecidirDirecao == 1:                                         #move para cima                                       
        print("MOVEU PRA BAIXO")
        if a-1 < 0:
            print("fora para baixo")
        else:
            matrix[a][b] = 0
            if TipoDePopulação == 1:
                matrix[a-1][b] = 1
            else:
                matrix[a-1][b] = 2
    if DecidirDirecao == 2:                                         #move para esquerda
        print("MOVEU PRA ESQUERDA")
        if b+1 > len(matrix[0]):
            print("fora pela esquerda")
        else:
            matrix[a][b] = 0
            if TipoDePopulação == 1:
                matrix[a][b+1] = 1
            else:
                matrix[a][b+1] = 2
        
    if DecidirDirecao == 3:                                         #move para direita
        print("MOVEU PRA DIREITA")
        if b-1 < 0:
            print("fora pela direita")
        else:
            matrix[a][b] = 0
            if TipoDePopulação == 1:
                matrix[a][b-1] = 1
            else:
                matrix[a][b-1] = 2
 

def gerarPresa():
    gerar_Presa_x = np.random.randint(0, L)
    gerar_Presa_y = np.random.randint(0, L)
 
    if matrix[gerar_Presa_y][gerar_Presa_x] != 1:
        matrix[gerar_Presa_y][gerar_Presa_x] = 1
        
    cooredenadasPresas.append([gerar_Presa_y,gerar_Presa_x])

    
    # print("presa x:", gerar_Presa_x, "presa y:", gerar_Presa_y)


def gerarPredador():
    gerar_Predador_x = np.random.randint(0, L)
    gerar_Predador_y = np.random.randint(0, L)
 
    if matrix[gerar_Predador_y][gerar_Predador_x] != 2:
        matrix[gerar_Predador_y][gerar_Predador_x] = 2
    
    cooredenadasPredadores.append([gerar_Predador_y,gerar_Predador_x])
    # print("presa x:", gerar_Presa_x, "presa y:", gerar_Presa_y)


i = 0
while i < 10:    
    # gerarPresa()   
    # gerarPredador() 

    i += 1

for i in cooredenadasPredadores:
    print("cooredenadasPredadores",cooredenadasPredadores)
    print("i",i)
    print(matrix)
    mover(i[0],i[1],2)
    print("depois: i",i)
    print(matrix)    
    
for i in cooredenadasPresas:
    print("cooredenadasPresas",cooredenadasPresas)
    print(matrix)
    mover(i[0],i[1],1)
    print("depois: i",i)
    print(matrix)

cmapmine = ListedColormap(['w','b','r'], N=3)
plt.matshow(matrix, cmap=cmapmine, vmin=0, vmax=3)
plt.show()


