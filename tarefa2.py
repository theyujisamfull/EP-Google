
# Define funçoes para operar com matrizes e vetores
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

# Define funçoes específicas do exercicio
def gerar_matriz_grupos_e_paginas_cacique():
    #Declara matriz_grupos
    matriz_grupos = []
    #Declara lista que guarda as páginas que são caciques
    paginas_cacique = []
    #Gera a matriz que representa a rede cacique tribo com 20 páginas, ou seja,
    #[[1,2],[3,4,5],[6,7,8,9],...,[210,211,...,230]] 
    for i in range(1,21):
        #Determina a página cacique do grupo i
        cacique = int((i * (i + 1)) / 2)
        #Armazena os caciques no vetor paginas_cacique
        paginas_cacique.append(pagina_cacique)
        #O grupo i tem i páginas não caciques (indios)
        quantidade_paginas_indio = i
        #matriz_grupo guarda as páginas do grupo i
        grupo = []
        for pagina in range(cacique, pagina_cacique + quantidade_paginas_indio + 1):
            grupo.append(pagina)
        matriz_grupos.append(grupo)
    return (matriz_grupos,paginas_cacique)

def gerar_pesos_links(matriz_grupos):
    '''Recebe uma lista de listas, e retorna uma lista de números.

    pesos_links é uma lista de numeros que representam os pesos relativos
    de cada página, isto é, o valor que cada link saindo dessa página adicionara
    na importancia da pagina para qual aponta.
    Esse valor é igual a um divido pelo número de links que saem da página
    '''
    pesos_links=[]
    for grupo in range(0,20):
        for posicao_pagina in range(len(matriz_grupos[grupo])):
            if posicao_pagina == 0: # significa que é cacique
                quantidade_links = len(matriz_grupos[grupo]) - 1 + 20 - 1 # 20 caciques
                pesos_links.append(1 / quantidade_links)
            else: # significa que é indio
                quantidade_links = len(matriz_grupos[grupo]) - 1
                pesos_links.append(1 / quantidade_links)
    return pesos_links

def encontrar_grupo(matriz_grupos, pagina):
    '''Recebe uma lista de listas e um número, e retorna um número.
    Dado um número que representa uma página, retorna o índice
    da sublista de matriz_grupos que contém esse número, este indice
    representa o grupo em que a página está contida
    '''
    for grupo in range(0,20):
        if pagina in matriz_grupos[grupo]:
            return grupo

def gerar_matriz_de_ligacao(matriz_grupos, paginas_cacique, pesos_links):
    '''Recebe uma lista de listas e duas listas de números, e retorna
    uma matriz quadrada.

    matriz_de_ligacao é uma matriz 230x230 que representa os links da rede
    e seus valores relativos de importância. A linha 1 da matriz representa
    todos os links que chegam à pagina 1, o elemento da linha 1 coluna 3 tem
    valor 1/21, o que significa que a página 3 aponta para a página 1, e
    esse link contribui para a importância da pagina 1 por (1/21*100)% da
    importancia da pagina 3.

    Nota-se que em python os indíces começam em 0, portanto o elemento da
    linha 1 coluna 1 da matriz é dado por matriz_de_ligacao[0][0]
    '''
    matriz_de_ligacao=[]
    for pagina_chegada in range(1,231):
        #Cada valor diferente de zero na linha_de_ligacao representa que
        #a pagina_saida, de numero igual ao indice do elemento em questao,
        #aponta para a pagina_chegada
        linha_de_ligacao = 230*[0]
        if pagina_chegada in paginas_cacique:
            grupo_da_pagina = encontrar_grupo(matriz_grupos, pagina_chegada)
            for pagina_saida in matriz_grupos[grupo_da_pagina]:
                if pagina_saida != pagina_chegada:
                    linha_de_ligacao[pagina_saida - 1] = pesos_links[pagina_saida - 1]
            for pagina_saida in paginas_cacique:
                if pagina_saida != pagina_chegada:
                    linha_de_ligacao[pagina_saida - 1] = pesos_links[pagina_saida - 1]
            matriz_de_ligacao.append(linha_de_ligacao)
        else:
            grupo_da_pagina = encontrar_grupo(matriz_grupos, pagina_chegada)
            for pagina_saida in matriz_grupos[grupo_da_pagina]:
                if pagina_saida != pagina_chegada:
                    linha_de_ligacao[pagina_saida - 1] = pesos_links[pagina_saida - 1]
            matriz_de_ligacao.append(linha_de_ligacao)
    return matriz_de_ligacao

def gerar_vetores_V_L_C(matriz_de_ligacao):
    '''Recebe uma matriz e retorna três vetores de numeros.
    A matriz de ligação é esparsa, isto é, tem muitas entradas 0.
    Para economizar mémoria e cálulos cria-se os vetores V, L, e C.
    Para cada elemento não nulo de matriz_de_ligacao, coloca-se o valor do
    elemento no vetor V, a linha em que o elemento está no vetor L, e a coluna
    no vetor C.
    '''
    V=[]
    L=[]
    C=[]
    for i in range(0,230):
        for j in range(0,230):
            if matriz_de_ligacao[i][j] != 0:
                V.append( matriz_de_ligacao[i][j] )
                L.append(i)
                C.append(j)
    return (V,L,C)

def verifica(B):
    ''' recebe uma matriz e verifica se a soma das colunas é 1'''
    for i in range(0,229):
        s=0
        for j in range(0,229):
            s+=B[j][i]
        if round(s) != 1 :
              print(s)
              return(False)
    return(True)

def calcula_y(xi):
    y=230*[0]
    for s in range(0,3459):
        y[L[s]]=y[L[s]]+V[s]*xi[C[s]]

    return y


def main():
    (matriz_grupos, paginas_cacique) = gerar_matriz_grupos_e_paginas_cacique()
    pesos_links = gerar_pesos_links(matriz_grupos)
    matriz_de_ligacao = gerar_matriz_de_ligacao(matriz_grupos,paginas_cacique,pesos_links)
    (V,L,C) = gerar_vetores_V_L_C(matriz_de_ligacao)

    m = 0.15
    x0 = 230*[1/230]
    S = 230*[230*[m/230]]
    M = soma( multEscalar(matriz_de_ligacao,(1-m)) , S )
    
    '''
    não estamos utilizando V,L e C para calcular a resposta
    logo, aqui vai sugestão de uso
    '''


    x=mult(M,x0)
    x1=x0
    #y=calcula_y(x0)
    k=0 # contador
    '''
    while(norma(sub(y,x1))>10**(-5)):
        x1=y
        y=calcula_y(x1)
        k+=1
    '''
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

main()
