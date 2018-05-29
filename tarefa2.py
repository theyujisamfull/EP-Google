
matriz = []

for i in range(0,20):
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
