
matriz = []

for i in range(1,21):
    grupo = i
    cacique = int ((grupo*(grupo+1))/2 )
    numero_de_indios = grupo+1
    matriz_do_grupo = []
    for j in range(cacique,cacique+numero_de_indios):
        matriz_do_grupo.append(j)
        
    matriz.append( matriz_do_grupo )

print(matriz)
