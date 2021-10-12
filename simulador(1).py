import matplotlib.pyplot as plt

def mapaColores():
	colores = ['white']
	aux = ['red','pink', 'blue']
	for i in range(3):
		for j in range(14):
			colores.append(aux[i])
			colores.extend(['yellow','blak', 'green'])
			cmap=mat.colors.ListedColormap(colores, name='colores', N=46)
			ancho,alto=20,20
			
M=[[1,18,34],[1,18,34],[1,18,34]]
plt.imshow(M)
plt.show()
	
mapaColores()

