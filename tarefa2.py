
# Define funçoes para operar com matrizes e vetores
def mult(A,b):
    '''Multiplica uma matriz quadrada por um vetor'''
    return( [sum( A[i][j]*b[j] for j in range(len(A)) ) for i in range(len(A))] )

def soma(A,B):
    '''Soma duas matrizes quadradas de mesmo tamanho'''
    #return( [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))] )
    return( [A[j] + B[j] for j in range(len(A))] )

def sub(a,b):
    '''Subtrai dois vetores de mesmo tamanho'''
    return( [a[i]-b[i] for i in range(len(a))] )

def norma(a):
    '''Calcula a norma de primeira ordem de um vetor'''
    return( sum( [abs(x) for x in a] ) )

def multEscalar(A,e):
    '''Multiplica uma matriz quadrada por um número'''
    #return( [[e*A[i][j] for j in range(len(A))] for i in range(len(A))] )
    return( [e*A[j] for j in range(len(A))] )

# Define funçoes específicas do exercicio
def gerar_matriz_grupos_e_paginas_cacique():
    '''Não recebe parâmetro e retorna uma lista de listas, e uma lista de numeros.

    matriz_grupos é uma lista de listas na forma
    [[1,2],[3,4,5],[6,7,8,9],...,[210,211,...,230]]
    Cada uma das listas internas representa um grupo de paginas,
    e o valor de seus elementos identificam as páginas.
    A primeira página de cada grupo é sempre um cacique, isto é, as
    páginas 1,3,6,...,210 são caciques.

    paginas_cacique é uma lista na forma
    [1,3,6,10,...,210]
    Cada um desses valores representa uma página cacique
    '''
    matriz_grupos = []
    paginas_cacique = []
    for grupo in range(1,21):
        pagina_cacique = int((grupo * (grupo + 1)) / 2)
        paginas_cacique.append(pagina_cacique)

        quantidade_paginas_indio = grupo
        matriz_grupo = []
        for pagina in range(pagina_cacique, pagina_cacique + quantidade_paginas_indio + 1):
            matriz_grupo.append(pagina)
        matriz_grupos.append(matriz_grupo)
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
    V=[]
    L=[]
    C=[]
    for pagina_chegada in range(1,231):
        '''
        Cada valor diferente de zero na linha_de_ligacao representa que
        a pagina_saida, de numero igual ao indice do elemento em questao,
        aponta para a pagina_chegada
        '''
        if pagina_chegada in paginas_cacique:
            grupo_da_pagina = encontrar_grupo(matriz_grupos, pagina_chegada)
            p= paginas_cacique+matriz_grupos[grupo_da_pagina]
            p.sort()
            for pagina_saida in p:
                if pagina_saida != pagina_chegada:
                    V.append(pesos_links[pagina_saida - 1])
                    L.append(pagina_chegada - 1)
                    C.append(pagina_saida - 1)

        else:
            grupo_da_pagina = encontrar_grupo(matriz_grupos, pagina_chegada)
            for pagina_saida in matriz_grupos[grupo_da_pagina]:
                if pagina_saida != pagina_chegada:
                    V.append(pesos_links[pagina_saida - 1])
                    L.append(pagina_chegada - 1)
                    C.append(pagina_saida - 1)
    return (V,L,C)





def calcula_y(xi,V,L,C):
    y=230*[0]
    for s in range(0,3460):
        y[L[s]]=y[L[s]]+V[s]*xi[C[s]]

    return y


def main():
    (matriz_grupos, paginas_cacique) = gerar_matriz_grupos_e_paginas_cacique()
    pesos_links = gerar_pesos_links(matriz_grupos)
    (V,L,C) = gerar_matriz_de_ligacao(matriz_grupos,paginas_cacique,pesos_links)
        


    x0 = 230*[1/230]
    y=calcula_y(x0,V,L,C)

    k=0
    x1=x0

    m = 0.15
    x2 = soma(multEscalar(y,1-m),multEscalar(x0,m))
    
    while(norma(sub(x2,x1))>10**(-5)):
        k=k+1
        x1=x2
        y=calcula_y(x1,V,L,C)
        x2 = soma(multEscalar(y,1-m),multEscalar(x0,m))




    add=0
    for i in y:
        add+=i
        if i<0: print('menor q zero')

    print(add)
    print(k)
    print(x2)

    

main()


    

