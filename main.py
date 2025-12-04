# Aprendamos Python desde cero
# Listas:

from repositorio.clases import  Auto, Moto

automovil = Auto('Chevrolet', "Gasolina", 4)
automovil2 = Auto('HUINDAY', "Gasolina", 2)
motocicleta = Moto("Honda", "Gasolina", 250)
motocicleta2 = Moto("Suzuki", "Gasolina", 150)

arreglo = [automovil, automovil2, motocicleta, motocicleta2]

for i in arreglo:
    print(f'marca: {i.marca} combustible: {i._tipo_combustible}')


# https://github.com/hpmezam/python_desde_cero.git

