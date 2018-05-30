


matriz = []
numeros_caciques = [] # quem  cacique
for i in range(1,21):
    grupo = i
    cacique = int((grupo*(grupo+1))/2 )
    numeros_caciques.append(cacique)
    numero_de_indios = grupo+1
    matriz_do_grupo = []
    for j in range(cacique,cacique+numero_de_indios):
        matriz_do_grupo.append(j)
        
    matriz.append(matriz_do_grupo)

matriz_den = []

for i in range(20):
    m_den=[]
    for j in range(len(matriz[i])):
        if (j==0): # significa que cacique
            den_cacique=len(matriz[i])-1+20-1 # 20 caciques
            m_den.append(1/den_cacique)
        else: # significa que indio
            den_indio=len(matriz[i])-1
            m_den.append(1/den_indio)
    matriz_den.append(m_den)

vetor_den=[]
vetor_matriz=[]
for i in range (0,20):
    for j in matriz_den[i]: vetor_den.append(j)
    for k in matriz[i]: vetor_matriz.append(k) 



def qual_grupo_e_pertence(e):
    for i in range(0,20):
        if e in matriz[i]: return i
                   
                   

#Declara matriz de lig 
matriz_de_ligacao=[]

for e in range(1,231):
    #Cada elemento z da linha e da matriz_de_ligacao diferente de zero quer dizer que z aponta pra e
    #Se i  cacique sabe-se que todos os outros caciques apontam pra i
    x = 230*[0]
    if e in numeros_caciques: 
        grupo_que_e_pertence = qual_grupo_e_pertence(e)
        for j in matriz[grupo_que_e_pertence]:
            if j != e:  x[j-1] = ( vetor_den[ j-1 ]  )
    
        for j in numeros_caciques:
            if j != e:  x[j-1] = ( vetor_den[ j-1 ]  )
        
        matriz_de_ligacao.append(x)
    else:
        grupo_que_e_pertence = qual_grupo_e_pertence(e)
        for j in matriz[grupo_que_e_pertence]:
            if j != e:  x[j-1] = ( vetor_den[ j-1 ]  )
        matriz_de_ligacao.append(x)

V=[]
for i in range(0,230):
    for j in range(0,len(matriz_de_ligacao[i])):
        if matriz_de_ligacao[i][j]!=0: V.append(matriz_de_ligacao[i][j])


L=[]
for i in range(0,230):
    for j in range(0,len(matriz_de_ligacao[i])):
        if matriz_de_ligacao[i][j]!=0: L.append(i)


C=[]
for i in range(0,230):
    for j in range(0,len(matriz_de_ligacao[i])):
        if matriz_de_ligacao[i][j]!=0: C.append(j)






print(C)







     





    












