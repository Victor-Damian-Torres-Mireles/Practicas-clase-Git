# Combinacion o Concatencacion de Strings

first_name = "Victor"
last_name = "Torres Mireles"

full_name = first_name + " " + last_name     # Siguen siendo strings

print(full_name.title())

print("Hola".upper(), first_name + " " + last_name)

# White Space

"""
Whitespace se refiere a cualquier caracter que no se imprime, 
es decir, un espacio ( ), tabuladores (\t) y finales de linea
(\n).

Los whitespaces se utilizan comunmente para organizar las salidas 
de texto a usuario de tal manera que sea mas amigable de leer o 
ver para los usuarios.
"""

print("Python")
print("\tPython")
print("\t\tPython")
print("Lenguajes:\n\tPython\n\t\tC\n\t\tJavaScript")

# Concatencacion de Strings utilizando F-Strings

famous_person = "Victorete"
message = f"{famous_person.upper()} una vez dijo : Python is love"
print(message)