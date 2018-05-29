
matriz = []

for i in range(1,21):
    grupo = i
    cacique = int ((grupo*(grupo+1))/2 )
    numero_de_indios = grupo+1
    matriz_do_grupo = []
    for j in range(cacique,cacique+numero_de_indios):
        matriz_do_grupo.append(j)
        
    matriz.append( matriz_do_grupo )



quem_sao_os_caciques = []
for i in range(1,21):
    quem_sao_os_caciques.append( int( (i*(i+1))/2)  )


matriz_de_

x1 = 20*[0]
for i in matriz[0]:
    x1[i-1]=1

print(x1)

