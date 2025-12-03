# Ingresar una hora, minutos y segundos y calcular
# qué hora será exactamente un segundo despues.
hora = int(input("Ingrese la hora: "))
minutos = int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))

segundos +=1

if segundos == 60:
    segundos=0
    minutos += 1
    if minutos == 60:
        minutos = 0
        hora +=1
        if hora == 24:
            hora = 0

print(f'La hora despues de un segundo es: {hora}:{minutos}:{segundos}')