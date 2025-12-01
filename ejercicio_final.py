# Ejercicio final: Cálculo del área de un círculo
# Autor: Henry Meza | DeepVisionH2M

# Importaciones - llamamos las librerías que necesitamos
import math

# Declaraciones - definimos las variables del programa
radio = 3
area = None

# Cálculos - aplicamos la fórmula matemática del área del círculo
area = math.pi * (radio ** 2)

# Resultados
print(f'El radio del círculo es: {radio}')
print(f'El área del círculo con radio {radio} es: {area:.2f}') # Mostramos con 2 decimales

# Variables adicionales
numero1 = 22
numero2 = numero1 + 2
print(f'El valor de numero1 es {numero1} y el valor de numero2 es {numero2}')

# Verificar tipos
print(f'Tipo de dato de radio: {type(radio)}')
print(f'Tipo de dato de area: {type(area)}')