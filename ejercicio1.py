# Convertir un número de segundos en horas, minutos y segundos.
segundos_totales = int(input('Ingresa la cantidad de segundos: '))
# ¿Cuántas horas completas hay?
horas = segundos_totales // 3600

# ¿Cuántos minutos completos quedan después de descontar esas horas?
segundos_restantes = segundos_totales % 3600
minutos = segundos_restantes // 60

# ¿Cuántos segundos sobran al final?
segundos = segundos_restantes % 60

# Resultados
print(f'horas: {horas}')
# print(f'segundos restantes: {segundos_restantes}')
print(f'minutos: {minutos}')
print(f'segundos: {segundos}')