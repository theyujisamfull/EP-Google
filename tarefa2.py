
# Define funçoes para operar com matrizes e vetores
def mult(A,b):
    '''Multiplica uma matriz quadrada por um vetor'''
    return( [sum( A[i][j]*b[j] for j in range(len(A)) ) for i in range(len(A))] )

def soma(A,B):
    '''Soma duas matrizes quadradas de mesmo tamanho'''
    return( [A[j] + B[j] for j in range(len(A))] )

def sub(a,b):
    '''Subtrai dois vetores de mesmo tamanho'''
    return( [a[i]-b[i] for i in range(len(a))] )

def norma(a):
    '''Calcula a norma de primeira ordem de um vetor'''
    return( sum( [abs(x) for x in a] ) )

def multEscalar(A,e):
    '''Multiplica uma matriz quadrada por um número'''
    return( [e*A[j] for j in range(len(A))] )


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
    matriz_de_ligacao=[]
    V=[]
    L=[]
    C=[]
    # Cada uma das 230 pagina_chegada representam cada uma das linhas da matriz
    # de ligação
    for pagina_chegada in range(1,231):
        #Verifica se a pagina_chegada é cacique
        if pagina_chegada in paginas_cacique:
            #Encontra a qual grupo tal pagina_chegada pertence
            grupo_da_pagina = encontrar_grupo(matriz_grupos, pagina_chegada)
            #A pagina_chegada é apontada pelos elementos do seu grupo e por
            #os outros caciques. Ordena-se as paginas que apontam para pagina_chegada
            p= paginas_cacique+matriz_grupos[grupo_da_pagina]
            p.sort()
            #pagina_saida são todas as paginas que apontam para pagina_chegada
            for pagina_saida in p:
                #Adiciona os pesos (1/numero de paginas que saem) das paginas
                #que apontam pra pagina_chegada na matriz V.
                #E pra cada um desses pesos adiciona-se nas matrizes L e C
                #a linha e a coluna em que se encontram na matriz de ligação
                #obs: o pagina_chegada nao aponta pra ela mesma por isso verifica
                #se pagina_saida é diferente da pagina_chegada
                if pagina_saida != pagina_chegada:
                    V.append(pesos_links[pagina_saida - 1])
                    L.append(pagina_chegada - 1)
                    C.append(pagina_saida - 1)
        #A pagina_chegada é indio
        else:
            #Encontra a qual grupo tal pagina_chegada pertence
            grupo_da_pagina = encontrar_grupo(matriz_grupos, pagina_chegada)
            #pagina_saida são todas as paginas que apontam para pagina_chegada
            for pagina_saida in matriz_grupos[grupo_da_pagina]:
                #Adiciona os pesos (1/numero de paginas que saem) das paginas
                #que apontam pra pagina_chegada na matriz V.
                #E pra cada um desses pesos adiciona-se nas matrizes L e C
                #a linha e a coluna em que se encontram na matriz de ligação
                #obs: o pagina_chegada nao aponta pra ela mesma por isso verifica
                #se pagina_saida é diferente da pagina_chegada
                if pagina_saida != pagina_chegada:
                    V.append(pesos_links[pagina_saida - 1])
                    L.append(pagina_chegada - 1)
                    C.append(pagina_saida - 1)
    return (V,L,C)

def calcular_y(xi,V,L,C):
    '''Recebe quatro listas e retorna uma lista.
    Dado um vetor xi que representa os valores das importancias das paginas em
    uma certa iteração, utiliza os vetores V, L, e C, para calcular a próxima
    iteração do vetor xi de importancias. O vetor V guarda os valores não nulos
    da matriz de ligação, e os vetores L e C guardam suas posições da linha e coluna
    na matriz de ligação.
    '''
    y=230*[0]
    for s in range(0,3460):
        y[L[s]]=y[L[s]]+V[s]*xi[C[s]]

    return y


def main():
    #Matriz_grupos é a matriz que contém vetores que representam cada um dos
    #20 grupos, ou seja, cada um desses vetores possuem as páginas do grupo.
    (matriz_grupos, paginas_cacique) = gerar_matriz_grupos_e_paginas_cacique()
    #pesos_links é vetor que carrega os pesos (1/numero de paginas que saem
    #da pagina) de cada uma das 230 paginas.
    pesos_links = gerar_pesos_links(matriz_grupos)
    #Gera os vetores V=vetores não nulos da matriz de ligação,L,C são os indices
    # da linha e coluna de cada um desses elementos não nulos.
    (V,L,C) = gerar_matriz_de_ligacao(matriz_grupos,paginas_cacique,pesos_links)

    x0 = 230*[1/230]
    y = calcular_y(x0,V,L,C)

    x1 = x0
    m = 0.15
    x2 = soma(multEscalar(y,1-m),multEscalar(x0,m))

    while(norma(sub(x2,x1))>10**(-5)):
        x1=x2
        y=calcular_y(x1,V,L,C)
        x2 = soma(multEscalar(y,1-m),multEscalar(x0,m))

    # Cria uma lista de tuplas na forma [(pagina,importancia)]
    paginas_rankeadas = list(enumerate(x2))

    # Cria uma lista na forma [(pagina,importancia)] somente com o cacique e a
    # primeira página indio de cada grupo
    paginas_rankeadas_sem_repeticao = []
    for pagina_cacique in paginas_cacique:
        paginas_rankeadas_sem_repeticao.append(paginas_rankeadas[pagina_cacique-1])
        paginas_rankeadas_sem_repeticao.append(paginas_rankeadas[pagina_cacique])

    # Ordena os elementos da lista criada em ordem descrescente de importância
    paginas_rankeadas_sem_repeticao = sorted(paginas_rankeadas_sem_repeticao,
                                            key = lambda item: item[1],
                                            reverse=True)

    # Printa uma tabela com os rankings, números da paginas, importancias, e indica
    # se é cacique ou não
    print("\n|{0:^9}|{1:^8}|{2:^10}|{3:^19}|".format("Ranking","Página","Cacique?","Importância"))
    for pagina in enumerate(paginas_rankeadas_sem_repeticao):
        print("|{rank:^9}|{pag:^8}|{cacique:^10}|{imp:^19.12}|".format(
                                                                    rank=pagina[0]+1,
                                                                    pag=pagina[1][0]+1,
                                                                    cacique= "Sim" if pagina[1][0]+1 in paginas_cacique else "Não",
                                                                    imp=pagina[1][1]))

main()
