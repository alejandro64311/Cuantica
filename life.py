import random
import matplotlib
import matplotlib.pyplot as plt

# regilla inicial
dimension_inicial_rejilla=10
# Numero de evoluciones
numero_de_evoluciones = 50
# densidad poblacional
porcentaje_celdas_vacias= 0.65
# porcentaje de individuos que se mueven
porcentaje_individuos_mueven = 0.3
# Porcentaje de individios sanos o enfermos
porcentaje_sanos = 0.5
porcentaje_contagiados = 0.5
porcentaje_asintomaticos = 0.5

numero_individuos = dimension_inicial_rejilla*dimension_inicial_rejilla
numero_individuos_sanos  = int((numero_individuos)*(porcentaje_sanos))
numero_contagiados = int((numero_individuos)*(porcentaje_contagiados))
numero_asintomaticos  = int((numero_contagiados)*(porcentaje_asintomaticos))
numero_sintomaticos = numero_contagiados-numero_asintomaticos
# Datos del virus
porcentaje_de_hospitalizaciones = 0.3
porcentaje_fallecidos_en_hospital = 0.95
porcentaje_fallecidos_domesticos = 0.3
probabilidad_diaria_salir_hospital = 0.3

ratio_de_contagio = 0.13

#Codigo de estados
CELDA_VACIA = 0
CONTAGIADO_1=1
CONTAGIADO_N=14
ASINTOMATICO_1=15
ASINTOMATICO_N=28
AISLADO_1=29
AISLADO_N=42
HOSPITAL=43
MUERTO=44
SANO=45

M=[[0]*dimension_inicial_rejilla for i in range(dimension_inicial_rejilla)]




def llenarMatriz(individuos,codigo):
    for i in range(individuos):        
        irandom = random.randint(0,dimension_inicial_rejilla-1)
        jrandom = random.randint(0,dimension_inicial_rejilla-1)
        if M[irandom][jrandom]==0 :M[irandom][jrandom] = codigo
         
       
        

'''
U|A|V
L|C|R
W|B|X
'''
def aplicarReglas():
    temp=[[0]*dimension_inicial_rejilla for i in range(dimension_inicial_rejilla)]
    for i in range(dimension_inicial_rejilla):
        for j in range(dimension_inicial_rejilla):
            actualizarEstado(i,j)
            actualizarPosicion(i,j)
            

def setNuevoEstadoSano(i,j):
    C=M[i][j]
    L=M[i][j-1]
    R=M[i][(j+1)%dimension_inicial_rejilla]
    A=M[i-1][j]
    B=M[(i+1)%dimension_inicial_rejilla][j]
    U=M[i-1][j-1]
    V=M[i-1][(j+1)%dimension_inicial_rejilla]
    W=M[(i+1)%dimension_inicial_rejilla][j-1]
    X=M[(i+1)%dimension_inicial_rejilla][(j+1)%dimension_inicial_rejilla]
    
    v=[L,R,A,B,U,V,W,X]
 
    
    filtroContagiados= filter(lambda x: (x>= CONTAGIADO_1 and x<= CONTAGIADO_N) or (x>= ASINTOMATICO_1 and x<= ASINTOMATICO_N) or (x== HOSPITAL)  , v)
    
    listaContagiados = list(filtroContagiados)
    filtroHospitalYVacias =filter(lambda x: (x!=CELDA_VACIA)  , listaContagiados)
 
    listacontagiados= list(filtroHospitalYVacias)
    
    S=len(listacontagiados)
  
    if(S>=3):
        #print("\nvfiltered",listacontagiados)
        #print("i,j",i,j)
        M[i][j] = getNuevoEstadoContagio()


def getNuevoEstadoContagio():
    estados = [CONTAGIADO_1,ASINTOMATICO_1]
    porsentajeSintomaticos =  1-porcentaje_asintomaticos
    weight = [porsentajeSintomaticos*100, porcentaje_asintomaticos*100]
    valorSeleccionado = random.choices(estados,  weights = weight,k = 1)
    return valorSeleccionado[0];
        
    
def aplicarReglaMovimiento(i,j):
    cordenadas = [i,j]
    L=m[i][j-1]
    if L==0 : 
        cordenadas[0]=i
        cordenadas[1]=j
        
    R=m[i][(j+1)%dimension_inicial_rejilla]
    if R==0 : 
        cordenadas[0]=i
        cordenadas[1]=j
        
    A=m[i-1][j]
    if A==0 : 
        cordenadas[0]=i
        cordenadas[1]=j
        
    B=m[(i+1)%dimension_inicial_rejilla][j]
    if B==0 : 
        cordenadas[0]=i
        cordenadas[1]=j
        
    U=m[i-1][j-1]
    if U==0 : 
        cordenadas[0]=i
        cordenadas[1]=j
        
    V=m[i-1][(j+1)%dimension_inicial_rejilla]
    if V==0 : 
        cordenadas[0]=i
        cordenadas[1]=j
        
    W=m[(i+1)%dimension_inicial_rejilla][j-1]
    if W==0 : 
        cordenadas[0]=i
        cordenadas[1]=j
        
    X=m[(i+1)%dimension_inicial_rejilla][(j+1)%dimension_inicial_rejilla]
    if X==0 : 
        cordenadas[0]=i
        cordenadas[1]=j
        
    C=m[i][j]
    if C==0 : 
        cordenadas[0]=i
        cordenadas[1]=j
        
    return cordenadas
    

def actualizarEstado(i,j):
    if(M[i][j]==MUERTO): M[i][j] = CELDA_VACIA
    
    if(M[i][j]==CONTAGIADO_N): setNuevoEstadoContagiado(i,j)
    elif (M[i][j]<CONTAGIADO_N and M[i][j]>=CONTAGIADO_1): M[i][j] = M[i][j]+1
    
    if(M[i][j]==ASINTOMATICO_N): M[i][j] = SANO
    elif (M[i][j]<ASINTOMATICO_N and M[i][j]>=ASINTOMATICO_1): M[i][j] = M[i][j]+1
    
    if(M[i][j]==HOSPITAL): setNuevoEstadoHospital(i,j)
    
    if(M[i][j]==SANO): setNuevoEstadoSano(i,j)
    
def actualizarPosicion(i,j):
    return True

def setNuevoEstadoContagiado(i,j): 
    estados = [HOSPITAL, MUERTO, SANO]
    porsentajeSano =  1-(porcentaje_de_hospitalizaciones +porcentaje_fallecidos_domesticos)
    weight = [porcentaje_de_hospitalizaciones*100, porcentaje_fallecidos_domesticos*100,porsentajeSano*100]
    valorSeleccionado = random.choices(estados,  weights = weight,k = 1)
    if(len(valorSeleccionado)!=None):
       M[i][j] = valorSeleccionado[0]
 
def setNuevoEstadoHospital(i,j): 
    estados = [HOSPITAL, MUERTO, SANO]
    porsentajeHospital =  1-(probabilidad_diaria_salir_hospital +porcentaje_fallecidos_en_hospital)
    weight = [porsentajeHospital*100, porcentaje_fallecidos_en_hospital*100,probabilidad_diaria_salir_hospital*100]
    valorSeleccionado = random.choices(estados,  weights = weight,k = 1)
    if(len(valorSeleccionado)!=None):
       M[i][j] = valorSeleccionado[0]
    
def imprimir():
    
    for i in range(dimension_inicial_rejilla):
        print(M[i])

def graficar(num):
     imagen=open("cuadro_%03d.pbm"%num,"w")
     imagen.write("P1 "+str(dimension_inicial_rejilla)+" "+str(dimension_inicial_rejilla))
     for i in range(dimension_inicial_rejilla):
         for j in range(dimension_inicial_rejilla):
             imagen.write(" "+str(M[i][j]))
     imagen.close()


llenarMatriz(numero_individuos_sanos,45)
llenarMatriz(numero_sintomaticos,15)
llenarMatriz(numero_asintomaticos,25)
imprimir()


for ii in range(numero_de_evoluciones):
    print("\n",ii)
    aplicarReglas()
    imprimir()
    plt.imshow(M)
    plt.savefig("img%03d"%ii)
    

#plt.show()
