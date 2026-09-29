"""
Las listas nos permiten almacenar informacion en un lugar
la cantidad que se desee: ya sean pocos elementos o millones
de elementos.

Una lista es una coleccion de items (elementos) que tiene un 
orden particular. Se pueden crear listas que incluyan strings, 
enteros, floats, los nombres de las personas de tu familia, 
etc, podemos almacenar (los tipos de datos permitidos en Python)
lo que queramos en una lista.

Son elementos Mutables: Pueden modificarse el tamaño de la lista.

Se recomienda nombrar una variable de tipo lista en plural.

En Python, los corchetes [] indican una lista, sus elementos 
se separan por comas.

Ejemplo:
"""

bicycles = ['trek', 'cannodale', 'redline', 'specialized', 'apache']
print(bicycles)

# En programacion siempre se empiza del 0

#Como podemos acceder a los elementos de una lista

"""
Las listas son colecciones ordenadas, Se puede acceder a un 
elemento de una lista diciendole a Python la posicion o indice
del elemento deseado.

Para obtener el valor deseado, se debe escribir el nombre de la 
lista, seguido del indice del elemento entre corchetes.
"""

print(bicycles[0], bicycles[1], bicycles[2])

print(bicycles[0] .upper())

# Los indices comienzan en 0, no en 1 
# bicycles = ['trek', 'cannodale', 'redline', 'specialized', 'apache']

# EJEMPLO

print(bicycles[1]) #Cannodale
print(bicycles[3]) #Specialized

# Accediendo al ultimo elemento de una lista
print(bicycles[-1]) #Apache
print(bicycles[-3]) #Specialized

# Utilizando valores individuales de una lista

message = f"My first bicycle was a {bicycles[-1].upper()}"
print(message)