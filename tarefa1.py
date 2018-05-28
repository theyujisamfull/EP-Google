A=[[0,0,0,0,0,0,0,0.5],[0.5,0,0,0,0,0,0,0],[0.5,0.5,0,0,0,0,0,0.5],[0,0.5,0,0,0,0,0,0],[0,0,0,0.5,0,0,0,0],[0,0,0.5,0.5,1,0,0,0],[0,0,0.5,0,0,1,0,0],[0,0,0,0,0,0,1,0]]
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

x=soma(multEscalar(mult(A,x0),1-m),multEscalar(x0,m))
while

    
