matriz_grupos = []
paginas_cacique = [] # quem é cacique
for grupo in range(1,21):
    pagina_cacique = int((grupo * (grupo + 1)) / 2)
    paginas_cacique.append(pagina_cacique)

    quantidade_paginas_indio = grupo
    matriz_grupo = []
    for pagina in range(pagina_cacique, pagina_cacique + quantidade_paginas_indio + 1):
        matriz_grupo.append(pagina)
    matriz_grupos.append(matriz_grupo)

# Constrói um vetor com os pesos relativos de cada página, isto é, com o valor
# que cada link saindo dessa página terá. Esse valor é igual 1 divido pelo
# número de links que saem da página
pesos_links=[]
for grupo in range(0,20):
    for posicao_pagina in range(len(matriz_grupos[grupo])):
        if posicao_pagina == 0: # significa que é cacique
            quantidade_links = len(matriz_grupos[grupo]) - 1 + 20 - 1 # 20 caciques
            pesos_links.append(1 / quantidade_links)
        else: # significa que é indio
            quantidade_links = len(matriz_grupos[grupo]) - 1
            pesos_links.append(1 / quantidade_links)

def encontrar_grupo(pagina):
    for grupo in range(0,20):
        if pagina in matriz_grupos[grupo]:
            return grupo

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
                linha_de_ligacao[pagina_saida - 1] = pesos_links[pagina_saida - 1]
        for pagina_saida in paginas_cacique:
            if pagina_saida != pagina_chegada:
                linha_de_ligacao[pagina_saida - 1] = pesos_links[pagina_saida - 1]
        matriz_de_ligacao.append(linha_de_ligacao)
    else:
        grupo_da_pagina = encontrar_grupo(pagina_chegada)
        for pagina_saida in matriz_grupos[grupo_da_pagina]:
            if pagina_saida != pagina_chegada:
                linha_de_ligacao[pagina_saida - 1] = pesos_links[pagina_saida - 1]
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

def mult(A,b):
    '''Multiplica uma matriz quadrada por um vetor'''
    return( [sum( A[i][j]*b[j] for j in range(len(A)) ) for i in range(len(A))] )

def soma(A,B):
    '''Soma duas matrizes quadradas de mesmo tamanho'''
    return( [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))] )

def sub(a,b):
    '''Subtrai dois vetores de mesmo tamanho'''
    return( [a[i]-b[i] for i in range(len(a))] )

def norma(a):
    '''Calcula a norma de primeira ordem de um vetor'''
    return( sum( [abs(x) for x in a] ) )

def multEscalar(A,e):
    '''Multiplica uma matriz quadrada por um número'''
    return( [[e*A[i][j] for j in range(len(A))] for i in range(len(A))] )

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
