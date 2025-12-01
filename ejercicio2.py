# Determinar si un número es positivo, negativo o cero.
# Ingresar un número
numero = int(input('Ingresa un número: '))

# Analizar y decidir a que categoría pertenece
if numero > 0:
    print('El número es positivo')
elif numero < 0:
    print('El número es negativo')
else:
    print('El número es cero')

# Resultados
# print(f'El número ingresado es: {numero}')