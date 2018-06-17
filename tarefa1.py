def mult(A,b):
    '''Multiplica uma matriz quadrada nxn por um vetor de tamanho n'''
    return( [sum( A[i][j]*b[j] for j in range(len(A)) ) for i in range(len(A))] )

def soma(a,b):
    '''Soma dois vetores de mesmo tamanho'''
    return( [a[i]+b[i] for i in range(len(a))] )

def sub(a,b):
    '''Subtrai dois vetores de mesmo tamanho'''
    return( [a[i]-b[i] for i in range(len(a))] )

def norma(a):
    '''Calcula a norma de primeira ordem de um vetor'''
    return( sum( [abs(x) for x in a] ) )

def multEscalar(a,e):
    '''Multiplica um vetor por um número'''
    return( [e*x for x in a] )

def main():
    # A é a matriz de ligação do problema
    A = [
    [0,0,0,0,0,0,0,0.5],
    [0.5,0,0,0,0,0,0,0],
    [0.5,0.5,0,0,0,0,0,0.5],
    [0,0.5,0,0,0,0,0,0],
    [0,0,0,0.5,0,0,0,0],
    [0,0,0.5,0.5,1,0,0,0],
    [0,0,0.5,0,0,1,0,0],
    [0,0,0,0,0,0,1,0]
    ]
    # S é uma matriz nxn com todas as entradas iguai a 1/n
    # ela é utilizada para garantir que a matriz
    # M = mA + (1-m)S , 0 < m < 1
    # tenha todas as entradas estritamente positivas
    # e colunas somando 1
    S = 8*[8*[1/8]]
    # m é o fator utilizado para construir a matriz M
    m = 0.15
    # x0 é o vator de importância inicial e tem n entradas
    # com valores 1/n , onde n é a quantidade de paginas
    # na rede
    x0 = 8*[1/8]

    # No algoritmo calculamos
    # x_l2 = M x_l1
    #      = (1-m)A x_l1 + mS x_l1
    # até a norma de primeira ordem de x_l2 e x_l1
    # ficar menor que o valor desejado.
    # Inicialmente atribuimos x_l1 = x0 para dar início
    # ao processo.
    # Como o termo (mS x_l1) é constante para qualquer
    # x_l1 nas condições do exercicio, o isolamos do calculo.
    # Ao final do processo x_l2 será o vetor de importância.
    constante = multEscalar(mult(S,x0),m)
    x_l2 = soma(multEscalar(mult(A,x0),1-m),constante)
    x_l1 = x0
    while norma(sub(x_l1,x_l2)) > 10**(-5):
        x_l1 = x_l2
        x_l2 = soma(multEscalar(mult(A,x_l1),1-m),constante)

    print("\nVetor de importância:\n{}".format(x_l2))

    # Ordena as páginas da rede em ordem decrescente de importancia
    paginas_rankeadas = sorted(enumerate(x_l2), key = lambda item: item[1], reverse=True)

    print("\n|{0:^9}|{1:^8}|{2:^17}|".format("Ranking","Página","Importância"))
    for pagina in enumerate(paginas_rankeadas):
        print("|{rank:^9}|{pag:^8}|{imp:^17.12}|".format(rank=pagina[0]+1, pag=pagina[1][0], imp=pagina[1][1]))

    print("\nSoma das importâncias = {}".format(sum(x_l2)))

main()




A = [[0,0,0,0,0,0,0,0.5],[0.5,0,0,0,0,0,0,0],[0.5,0.5,0,0,0,0,0,0.5],[0,0.5,0,0,0,0,0,0],[0,0,0,0.5,0,0,0,0],[0,0,0.5,0.5,1,0,0,0],[0,0,0.5,0,0,1,0,0],[0,0,0,0,0,0,1,0]]
S = 8*[8*[1/8]]
M = 8*[8*[0]]


for i in range(8):
    for j in range(8):
        A[i][j] = A[i][j]*(1-0.15)

for i in range(8):
    for j in range(8):
        S[i][j] = S[i][j]*(0.15)

for i in range(8):
    for j in range(8):
        M[i][j] = A[i][j]+S[i][j]
print(M)




