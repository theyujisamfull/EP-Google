A=[[0,0,0,0,0,0,0,0.5],[0.5,0,0,0,0,0,0,0],[0.5,0.5,0,0,0,0,0,0.5],[0,0.5,0,0,0,0,0,0],[0,0,0,0.5,0,0,0,0],[0,0,0.5,0.5,1,0,0,0],[0,0,0.5,0,0,1,0,0],[0,0,0,0,0,0,1,0]]
S = 8*[8*[1/8]]
m=0.15
x0 = 8*[1/8]

def mult(B,b):
    R=[]
    for i in range(8):
        soma=0
        for j in range(8):
            soma+=B[i][j]*b[j]
        R.append(soma)
    return(R)

def soma(a,b):
    c=[]
    for i in range(8):
        c.append(a[i]+b[i])
    return(c)

def sub(a,b):
    c=[]
    for i in range(8):
        c.append(a[i]-b[i])
    return(c)

def norma(a):
    s=0
    for i in range(len(a)):
        s+=abs(a[i])
    return(s)

def multEscalar(a,e):
    b=[]
    for i in range(8):
        b.append(e*a[i])
    return(b)

s = mult(S,x0)
x=soma(multEscalar(mult(A,x0),1-m),multEscalar(s, m))
x1=x0
while(norma(sub(x,x1))>10**(-5)):
    x1=x
    x=soma(multEscalar(mult(A,x1),1-m),multEscalar(s, m))

print("\nVetor de classificação:\n{}".format(x)) # vetor classificação

paginas_rankeadas = sorted(enumerate(x), key = lambda item: item[1], reverse=True)
print("\n|{0:^9}|{1:^8}|{2:^17}|".format("Ranking","Página","Importância"))
for pagina in enumerate(paginas_rankeadas):
    print("|{rank:^9}|{pag:^8}|{imp:^17.12}|".format(rank=pagina[0]+1, pag=pagina[1][0], imp=pagina[1][1]))

p=0
for i in x:
   p+=i
print("\nSoma das importâncias = {}".format(p))
