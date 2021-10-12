import random

# regilla inicial
dimension_inicial_rejilla=20
# Número de evoluciones
numero_de_evoluciones = 1000
# densidad poblacional
porcentaje_celdas_vacias= 0.65
# porcentaje de individuos que se mueven
porcentaje_individuos_mueven = 0.3
# Porcentaje de individios sanos o enfermos
porcentaje_sanos = 0.95
porcentaje_contagiados = 0.05
porcentaje_asintomaticos = 0.3

numero_individuos = dimension_inicial_rejilla*dimension_inicial_rejilla
numero_individuos_sanos  = (numero_individuos)*(porcentaje_sanos)
numero_contagiados = (numero_individuos)*(porcentaje_contagiados)
numero_asintomaticos  = (numero_individuos)*(porcentaje_asintomaticos)

# Datos del virus
porcentaje_de_hospitalizaciones = 0.03
porcentaje_fallecidos_en_hospital = 0.95
porcentaje_fallecidos_domesticos = 0.05
probabilidad_diaria_salir_hospital = 0.3

ratio_de_contagio = 0.13

M=[[0]*dimension_inicial_rejilla for i in range(dimension_inicial_rejilla)]



M[3][1]=1
M[3][2]=1
M[3][3]=1
M[2][3]=1
M[1][2]=1

M[10][3]=1
M[11][3]=1
M[12][3]=1

def llenarMatriz(individuos,codigo):
    for i in range(individuos):        
        irandom = random.randint(0,dimension_inicial_rejilla)
        jrandom = random.randint(0,dimension_inicial_rejilla)
        M[irandom][jrandom] = codigo
        


'''
U|A|V
L|C|R
W|B|X
'''
def aplicarReglas(m):
    temp=[[0]*dimension_inicial_rejilla for i in range(dimension_inicial_rejilla)]
    for i in range(dimension_inicial_rejilla):
        for j in range(dimension_inicial_rejilla):
            C=m[i][j]
            L=m[i][j-1]
            R=m[i][(j+1)%dimension_inicial_rejilla]
            A=m[i-1][j]
            B=m[(i+1)%dimension_inicial_rejilla][j]
            U=m[i-1][j-1]
            V=m[i-1][(j+1)%dimension_inicial_rejilla]
            W=m[(i+1)%dimension_inicial_rejilla][j-1]
            X=m[(i+1)%dimension_inicial_rejilla][(j+1)%dimension_inicial_rejilla]
            v=[L,R,A,B,U,V,W,X]
            S=sum(v)
            N=0
            if C==0 and S==3: N=1
            if C==1 and (S==3)|(S==2): N=1
            temp[i][j]=N
    return temp
'''
def imprimir():
    for i in range(dimension_inicial_rejilla):
        print(M[i])
'''
def graficar(num):
    imagen=open("cuadro_%03d.pbm"%num,"w")
    imagen.write("P1 "+str(dimension_inicial_rejilla)+" "+str(dimension_inicial_rejilla))
    for i in range(dimension_inicial_rejilla):
        for j in range(dimension_inicial_rejilla):
            imagen.write(" "+str(M[i][j]))
    imagen.close()
#imprimir()
for i in range(80):
    graficar(i)
    M=aplicarReglas(M)



