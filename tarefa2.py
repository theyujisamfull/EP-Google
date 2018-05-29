
matriz = []

for i in range(1,21):
    grupo = i
    cacique = int ((grupo*(grupo+1))/2 )
    numero_de_indios = grupo+1
    matriz_do_grupo = []
    for j in range(cacique,cacique+numero_de_indios):
        matriz_do_grupo.append(j)
        
    matriz.append( matriz_do_grupo )

matriz_den = []
for i in range(20):
    for j in range(len(matriz[i])):
        if (j==0): # significa que é cacique
            den_cacique=len(matriz[i])-1+20-1 # 20 caciques
            matriz_den[i].append(1/den_cacique)
        else: # significa que é indio
            den_indio=len(matriz[i])-1
            matriz_den[i].append(1/den_indio)
    
print(matriz_den)
