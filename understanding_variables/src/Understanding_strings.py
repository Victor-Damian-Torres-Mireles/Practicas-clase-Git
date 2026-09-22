# STRINGS

""" 
Un string es de manera sencilla una serie de caracteres. 
En Python, todo lo que se encuentre entre comillas simples ''
o dentro de comillas dobles "" es considerado un string

Ejemplo:

"Esto es un string"
'Esto tambien es un string'
'Le die a mi amigo, "Python es mi lenguaje favorito"
"El lenguaje de 'Python' lleva el nombre por Monty Python, no por la serpiente"

Ejemplo incorrecto:

"Charly'
'Charly"

"""
name = "VicTOr DamIAn TORres Mireles"          # Variable tipo String 
print(name)

print(name.title ())     # .title()  Solo funciona para variables tipo string
print(name)

name = name.title()
print(name)

# Metodos

"""
Un metodo es una accion que Python puede realizar sobre una
variable.

El punto . despues de una variable seguido por el nombre del 
metodo en este caso title() dice qye se tiene que ejecutar el 
metodo title () de la variable name.

Todos los metodos van seguidos de parentesis, porque en ocasiones
necesitan informacion adicional para funcionar. En esta ocasion
el metodo title no requiere informacion adicional para ejecutarse.
"""

print(name.upper())
print("----------")
print(name.lower())