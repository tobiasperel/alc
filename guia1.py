import numpy as np

#ej3

v = np.array([1, 2, 3,-1])
w = np.array([2,3,0,5])
# print ("v+w = ", v+w)
# print("2v = ", 2*v)
# print("v**2 = ", v**2)

#matrices
A = np.array( [ [ 1 , 2 , 3 , 4 , 5 ] , [ 0 , 1 , 2 , 3 , 4 ] , [ 2 , 3 , 4 , 5 , 6 ] , [ 0 , 0 , 1 , 2 , 3 ] , [ 0 , 0 , 0 , 0 , 1 ] ] )
# print(A)
A [ 0 : 2 , 3 : 5 ]
A [ : 2 , 3 : ]
A [ [ 0 , 2 , 4 ] , : ]
ind = np.array ( [ 0 , 2 , 4 ] )
A[ ind , ind ] # diagonal
A[ ind , ind [ : , None ] ]

# Numeros c o m p l e j o s
1j * 1j
(1+2j) * 1j

# ej 4 y = ax^2 + bx + c

import matplotlib.pyplot as plt #l i b r e r i a para g r a f i c a r

# Definir los puntos
points = np.array([[1, 1], [2, 2], [3, 0]])

# Crear el sistema de ecuaciones
sis = np.array([
    [1**2, 1, 1],
    [2**2, 2, 1],
    [3**2, 3, 1]
])
sol = np.array([1, 2, 0])

# Resolver el sistema de ecuaciones
x = np.linalg.solve(sis,sol)
a, b, c = x
# . . .

xx = np.array ( [ 1 , 2 , 3 ] )
yy = np.array( [ 1 , 2 , 0 ] )
x = np.linspace( 0 , 4 , 100 ) #g e n e r a 100 puntos e q u i e s p a c i a d o s e n t r e 0 y 4 .
f = lambda t : a * t **2+b* t+c #e s t o g e n e r a una f u n c i o n f de t .
plt.plot( xx , yy , '*' )
plt.plot ( x , f ( x ) )
plt.savefig('grafico.png')