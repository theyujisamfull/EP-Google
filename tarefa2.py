
matriz = []

for i in range(0,20):
    grupo = i
    cacique = int ((grupo*(grupo+1))/2 )
    numero_de_indios = grupo+1
    matriz_do_grupo = []
    for j in range(cacique,cacique+numero_de_indios):
        matriz_do_grupo.append(j)
        
    matriz.append( matriz_do_grupo )

<<<<<<< HEAD
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
=======


quem_sao_os_caciques = []
for i in range(1,21):
    quem_sao_os_caciques.append( int( (i*(i+1))/2)  )
'''

matriz_de_ligacao=[]
for i in range(1,231):
    x = 20*[0]
    for j in matriz[i]:
        x[j-1]=1

'''

#denominador_cacique = len(matriz[i])
s=0
for i in range(0,20):
   s = s+ len(matriz[i])
print(len(matriz[0]) )


if 1 in quem_sao_os_caciques: print('oi')
>>>>>>> 1cee6cc67f4e2e3ab3b2f64cf53766e857513361
