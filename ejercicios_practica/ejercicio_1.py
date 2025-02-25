# CODE:10
# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Objetivo:
# Ingrese dos números enteros cualesquiera
# y realice las siguientes comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Alumno
# En cada desafio se le indicará que dada cierta condición
# modifique el valor de una variable

# Compare los dos números y entre sí 
# utilizando if y else.
# - Si numero_1 es mayor a numero_2, almacenar 1 en res_1
# - De lo contrario, almacenar 2 en res_1
res_1 = 0

# Imprimir en pantalla la variable res_1

# Verifique si el numero_1 positivo, negativo o cero
# Utilice if, elif y else
# - Si numero_1 es positivo, almacenar 1 en res_2
# - Si numero_1 es negativo, almacenar 2 en res_2
# - Si numero_1 es cero, almacenar 3 en res_2
res_2 = 0

# Imprimir en pantalla la variable res_2


# Verifique si el numero_1 es mayor a 0 y menor a 100
# Utilice un if con un condicional compuesto
# - Si se cumple la condición, almacenar 1 en res_3
# - De lo contrario, almacenar 2 en res_3
res_3 = 0

# Imprimir en pantalla la variable res_3


# Verifique si:
# el numero_1 es menor a 10 o el numero_2 es mayor a -2
# Utilice un if con un condicional compuesto
# - Si se cumple la condición, almacenar 1 en res_4
# - De lo contrario, almacenar 2 en res_4
res_4 = 0

# Imprimir en pantalla la variable res_4

# Comienzo de codigo por Gonzalo Larrrea ///

if numero_1 > numero_2:
    res_1 = 1
    print(f"el numero mayor es {numero_1}")
    print(f"el valor de res_1 es {res_1}")
else:
    res_1 = 2
    print(f"el numero mayor es {numero_2}")
    print(f"el valor de res_1 es {res_1}")
print("\n")

if numero_1 > 0:
    res_2 = 1
    print(f"El numero {numero_1} es positivo")
    print(f"el valor de res_2 es {res_2}")
elif numero_1 < 0:
    res_2 = 2
    print(f"El numero {numero_1} es negativo")
    print(f"el valor de res_2 es {res_2}")
else:
    res_2 = 3
    print(f"El numero {numero_1} es 0")
    print(f"El valor de res_2 es {res_2}")
print("\n")

if numero_1 > 0 and numero_1 < 100:
    res_3 = 1
    print(f"el numero {numero_1} es mayor a 0 y menor a 100")
    print(f"El valor de res_3 es {res_3}")
else:
    res_3 = 2
    print(f"El numero {numero_1} es menor a 0 o mayor a 100")
    print(f"El valor de res_3 es {res_3}")
print("\n")

if numero_1 < 10 or numero_2 > -2:
    res_4 = 1
    print(f"El numero {numero_1} es menor a 10 o el numero {numero_2} es mayor a -2")
    print(f"El valor de res_4 es {res_4}")
else:
    res_4 = 2
    print(f"El numero {numero_1} es mayor a 10 y el numero {numero_2} es menor a -2")
    print(f"el valor de res_4 es {res_4}")
print("\n")

# Fin del codigo ///