matriz_grupos = []
paginas_cacique = [] # quem é cacique
for grupo in range(1,21):
    pagina_cacique = int((grupo*(grupo+1))/2)
    paginas_cacique.append(pagina_cacique)

    quantidade_paginas_indio = grupo
    matriz_grupo = []
    for pagina in range(pagina_cacique, pagina_cacique + quantidade_paginas_indio + 1):
        matriz_grupo.append(pagina)
    matriz_grupos.append(matriz_grupo)

# Constrói a matriz com os pesos relativos de cada página
matriz_den = []
for i in range(0,20):
    m_den=[]
    for j in range(len(matriz_grupos[i])):
        if (j==0): # significa que é cacique
            den_cacique = len(matriz_grupos[i])-1+20-1 # 20 caciques
            m_den.append(1/den_cacique)
        else: # significa que é indio
            den_indio = len(matriz_grupos[i])-1
            m_den.append(1/den_indio)
    matriz_den.append(m_den)

vetor_den=[]
for i in range (0,20):
    for j in matriz_den[i]: vetor_den.append(j)

def encontrar_grupo(pagina):
    for grupo in range(0,20):
        if pagina in matriz_grupos[grupo]: return grupo

#Declara matriz de ligação
matriz_de_ligacao=[]
for pagina_chegada in range(1,231):
    #Cada valor diferente de zero na linha_de_ligacao representa que
    #a pagina_saida, de numero igual ao indice do elemento em questao,
    #aponta para a pagina_chegada
    #A linha um da matriz_de_ligacao representa as paginas que apontam
    #para a pagina 1, a linha n representa as paginas que apontam para n
    linha_de_ligacao = 230*[0]
    if pagina_chegada in paginas_cacique:
        grupo_da_pagina = encontrar_grupo(pagina_chegada)
        for pagina_saida in matriz_grupos[grupo_da_pagina]:
            if pagina_saida != pagina_chegada:
                linha_de_ligacao[pagina_saida-1] = ( vetor_den[ pagina_saida-1 ]  )
        for pagina_saida in paginas_cacique:
            if pagina_saida != pagina_chegada:
                linha_de_ligacao[pagina_saida-1] = ( vetor_den[ pagina_saida-1 ]  )
        matriz_de_ligacao.append(linha_de_ligacao)
    else:
        grupo_da_pagina = encontrar_grupo(pagina_chegada)
        for pagina_saida in matriz_grupos[grupo_da_pagina]:
            if pagina_saida != pagina_chegada:
                linha_de_ligacao[pagina_saida-1] = ( vetor_den[ pagina_saida-1 ]  )
        matriz_de_ligacao.append(linha_de_ligacao)

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

def mult(B,b):
    R=[]
    for i in range(230):
        soma=0
        for j in range(230):
            soma+=B[i][j]*b[j]
        R.append(soma)
    return(R)

def soma(A,B):
    # A e B tem que ter mesma dimensão
    C=[]
    for i in range(len(A)):
        linha=[]
        for j in range(len(A[i])):
            linha.append(A[i][j]+B[i][j])
        C.append(linha)
    return(C)

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
        linha=[]
        for j in range(230):
            linha.append(e*a[i][j])
        b.append(linha)
    return(b)


m=0.15
x0= 230*[1/230]
S = 230*[230*[m/230]]
M = soma( multEscalar(matriz_de_ligacao,(1-m)) , S )


x=mult(M,x0)
x1=x0
k=0 # contador
while(norma(sub(x,x1))>10**(-5)):
    x1=x
    x=mult(M,x1)
    k+=1 # contador
 # vetor classificação

add=0
for i in x:
    add+=i
    if i<0: print('menor q zero')

print(add)
print(len(x))
