A=[[0,0,0,0,0,0,0,0.5],[0.5,0,0,0,0,0,0,0],[0.5,0.5,0,0,0,0,0,0.5],[0,0.5,0,0,0,0,0,0],[0,0,0,0.5,0,0,0,0],[0,0,0.5,0.5,1,0,0,0],[0,0,0.5,0,0,1,0,0],[0,0,0,0,0,0,1,0]]

x0 = 8*[1/8]

def mult(B,b):
    R=[]
    soma=0
    for i in range(8):
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
    
