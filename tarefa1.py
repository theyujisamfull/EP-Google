def mult(A,b):
    '''Multiplica uma matriz quadrada por um vetor'''
    return( [sum( A[i][j]*b[j] for j in range(len(A)) ) for i in range(len(A))] )

def soma(a,b):
    return( [a[i]+b[i] for i in range(len(a))] )

def sub(a,b):
    return( [a[i]-b[i] for i in range(len(a))] )

def norma(a):
    return( sum( [abs(x) for x in a] ) )

def multEscalar(a,e):
    return( [e*x for x in a] )

def main():
    A = [[0,0,0,0,0,0,0,0.5],[0.5,0,0,0,0,0,0,0],[0.5,0.5,0,0,0,0,0,0.5],[0,0.5,0,0,0,0,0,0],[0,0,0,0.5,0,0,0,0],[0,0,0.5,0.5,1,0,0,0],[0,0,0.5,0,0,1,0,0],[0,0,0,0,0,0,1,0]]
    S = 8*[8*[1/8]]
    m = 0.15
    x0 = 8*[1/8]

    s = mult(S,x0)
    x = soma(multEscalar(mult(A,x0),1-m),multEscalar(s,m))
    x1 = x0
    while(norma(sub(x,x1)) > 10**(-5)):
        x1 = x
        x = soma(multEscalar(mult(A,x1),1-m),multEscalar(s,m))

    print("\nVetor de classificação:\n{}".format(x)) # vetor classificação

    paginas_rankeadas = sorted(enumerate(x), key = lambda item: item[1], reverse=True)
    print("\n|{0:^9}|{1:^8}|{2:^17}|".format("Ranking","Página","Importância"))
    for pagina in enumerate(paginas_rankeadas):
        print("|{rank:^9}|{pag:^8}|{imp:^17.12}|".format(rank=pagina[0]+1, pag=pagina[1][0], imp=pagina[1][1]))

    print("\nSoma das importâncias = {}".format(sum(x)))

main()
