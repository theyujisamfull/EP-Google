def mult(B,b):
    R=[]
    for i in range(230):
        soma=0
        for j in range(230):
            soma+=B[i][j]*b[j]
        R.append(soma)
    return(R)

def soma(a,b):
    c=[]
    for i in range(230):
        c.append(a[i]+b[i])
    return(c)

def sub(a,b):
    c=[]
    for i in range(230):
        c.append(a[i]-b[i])
    return(c)

def norma(a):
    s=0
    for i in range(len(a)):
        s+=abs(a[i])
    return(s)

def multEscalar(a,e):
    b=[]
    for i in range(230):
        b.append(e*a[i])
    return(b)



matriz = []
numeros_caciques = [] # quem é cacique
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



def qual_grupo_e_pertence(e):
    for i in range(0,20):
        if e in matriz[i]: return i
                   
                   

#Declara matriz de ligação 
matriz_de_ligacao=[]

for e in range(1,231):
    #Cada elemento z da linha e da matriz_de_ligacao diferente de zero quer dizer que z aponta pra e
    #Se i é cacique sabe-se que todos os outros caciques apontam pra i
    z = 230*[0]
    if e in numeros_caciques: 
        grupo_que_e_pertence = qual_grupo_e_pertence(e)
        for j in matriz[grupo_que_e_pertence]:
            if j != e:  z[j-1] = ( vetor_den[ j-1 ]  )
    
        for j in numeros_caciques:
            if j != e:  z[j-1] = ( vetor_den[ j-1 ]  )
        
        matriz_de_ligacao.append(z)
    else:
        grupo_que_e_pertence = qual_grupo_e_pertence(e)
        for j in matriz[grupo_que_e_pertence]:
            if j != e:  z[j-1] = ( vetor_den[ j-1 ]  )
        matriz_de_ligacao.append(z)

def verifica(B):
    for i in range(0,229):
        s=0
        for j in range(0,229):
            s+=B[j][i]
        if round(s) != 1 :
              print(s)
              return(False)
    return(True)

V=[]
L=[]
C=[]
for i in range(0,230):
    for j in range(0,230):
        if matriz_de_ligacao[i][j] !=0:
            V.append( matriz_de_ligacao[i][j] )
            L.append(i)
            C.append(j)

def calcula_y(xi):
    y=230*[0]
    for s in range(0,3459):
        y[L[s]]=y[L[s]]+V[s]*xi[C[s]]

    return y

m=0.15
x0= 230*[1/230]
S = 230*[230*[1/230]]
x=soma(multEscalar(  calcula_y(x0) ,1-m),multEscalar( mult(S,x0),m))
x1=x0
k=0 # contador
while(norma(sub(x,x1))>10**(-5)):
    x1=x
    x=soma(multEscalar( calcula_y(x1) ,1-m),multEscalar( mult(S,x1),m))
    k+=1 # contador 
#print(x) # vetor classificação

add=0
for i in x:
    add+=i
print(add)

print(verifica(matriz_de_ligacao))







