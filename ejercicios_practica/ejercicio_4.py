# CODE:14
# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos condicionales y operador incremento

# Objetico
# Verificar cuanta veces (contar) el usuario
# ingresa por consola un número mayor a cero
cantidad_numeros_positivos = 0

# Alumno:
# Deberá solicitar tres números enteros por consola,
# cada nuḿero entero lo debe almacenar en variables llamadas:
# numero_1
# numero_2
# numero_3

# Deberá realizar un tres condicionales separados,
# en cada condicional deberá averiguar si cada número
# es mayor a cero.

# Por cada número mayor a cero (cada condicional que se cumpla)
# deberá incrementar en 1 (+= 1) la "variable cantidad_numeros_positivos"


# Al finalizar, imprimir en pantalla la variable cantidad_numeros_positivos


# Comienzo de codigo por Gonzalo Larrea

cantidad = int(input("Que cantidad de numeros quiere ingresar?:"))
contador = 1
cantidad_numeros_positivos = 0

while contador <= cantidad:
    numero = int(input("Ingrese un numero: \n"))
    if numero > 0:
        cantidad_numeros_positivos += 1
    else:
        pass
    contador += 1

print(f"Se ingresaron {cantidad_numeros_positivos} numeros positivos \n")
