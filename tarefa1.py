A=[[0,0,0,0,0,0,0,0.5],[0.5,0,0,0,0,0,0,0],[0.5,0.5,0,0,0,0,0,0.5],[0,0.5,0,0,0,0,0,0],[0,0,0,0.5,0,0,0,0],[0,0,0.5,0.5,1,0,0,0],[0,0,0.5,0,0,1,0,0],[0,0,0,0,0,0,1,0]]
S = [ 8*[1/8] for i in range(8)]
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

x=soma(multEscalar(mult(A,x0),1-m),multEscalar( mult(S,x0),m))
x1=x0
k=0 # contador
while(norma(sub(x,x1))>10**(-5)):
    x1=x
    x=soma(multEscalar(mult(A,x1),1-m),multEscalar(x0,m))
    k+=1 # contador 
print(x) # vetor classificação

p=0
for i in x:
   p+=i
print(p)

    
