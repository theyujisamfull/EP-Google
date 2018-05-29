
matriz = []
numeros_caciques=[]
for i in range(1,21):
    grupo = i
    cacique = int ((grupo*(grupo+1))/2 )
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
        if (j==0): # significa que é cacique
            den_cacique=len(matriz[i])-1+20-1 # 20 caciques
            m_den.append(1/den_cacique)
        else: # significa que é indio
            den_indio=len(matriz[i])-1
            m_den.append(1/den_indio)
    matriz_den.append(m_den)
    
vetor_den=[]
vetor_matriz=[]
for i in range (0,20):
    for j in matriz_den[i]: vetor_den.append(j)
    for k in matriz[i]: vetor_matriz.append(k)



def find_the_cacique(y):
    while(y in numeros_caciques == False):
        y=y-1
    return(y)

quaseV=[]
for i in range(1,231):
    linha=[]
    if i in numeros_caciques:
        linha=numeros_caciques # adiciona os caciques + o grupo de i
        x = (-1+(1+8*i)**0.5)/2 # linha do cacique 
        for k in matriz[int(x)-1]:
            linha.append(k) # tenho a linha do cacique mas tenho que tirar o cacique
        linha=sorted(set(linha))
        linha.remove(i)
    else:
        c=find_the_cacique(i)
        x = (-1+(1+8*c)**0.5)/2 # linha do cacique
        linha=matriz[int(x)-1]
        linha.remove(i)
    quaseV.append(linha)

V=[]
for i in range(len(quaseV)):
    for j in quaseV: V.append(j)
print(len(V))

