# nombre = input('¿Cuál es tu nombre? ')
# print(nombre)

# edad = int(input('¿Cuántos años tienes? '))
# print(edad)
# print(type(edad))  # Por defecto, input() devuelve una cadena de texto

# # Con decimales
# estatura = float(input('¿Cuál es tu estatura en metros? '))
# print(estatura)
# print(type(estatura))

# # Mini demostración de uso de input() y conversión de tipos
# numero_str = input('Ingresa un número:')
# print('Antes de la conversión:', numero_str, type(numero_str))

# numero_int = int(numero_str)
# print('Después de la conversión a entero:', numero_int, type(numero_int))

# Ejercicio final: connersor de Celsius a Fahrenheit
print('Conversor de grados Celsius a Fahrenheit')

celsius = float(input('Ingresa la temperatura en grados Celsius: '))
fahrenheit = (celsius * 9/5) + 32

print(f'{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.')