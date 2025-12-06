from modelos.estudiante import Estudiante
from modelos.profesor import Profesor
from sistema.gestor import GestorPersonas
def menu():
    print("---- Sistema POO ----")
    print("1. Agregar un estudiante")
    print("2. Agregar un profesor")
    print("3. Listar descripciones")
    print("4. Buscar persona")
    print("5. Eliminar persona")


def main():
    gestor = GestorPersonas()
    while True:
        menu()
        opcion = input('Seleccionar una opción: ')
        
        if opcion == "1":
            cedula = input("Cédula: ")
            nombre = input("Nombre: ")
            edad = input("Edad: ")
            carrera = input("Carrera: ")
            est = Estudiante(cedula, nombre, edad, carrera)
            gestor.agregar(est)
            print("Estudiante agreado a la lista")
        elif opcion == "2":
            cedula = input("Cédula: ")
            nombre = input("Nombre: ")
            edad = input("Edad: ")
            especialidad = input("Especialidad: ")
            gestor.agregar(Profesor(cedula, nombre, edad, especialidad))
            print("Profesor agreado a la lista")
        elif opcion == "3":
            print("------- Lista de datos --------")
            for i in gestor.listar_descripcion():
                print(f"- {i}")
        elif opcion == "4":
            cedula = input("Cédula: ")
            p = gestor.buscar(cedula)
            print(f'Resultado: {p.descripcion() if p else "No encontrado."}')
        elif opcion == "5":
            cedula = input("Cédula para eliminar: ")
            a = gestor.eliminar(cedula)
            if a:
                print('Eliminado')
            else:
                print('No existe')
        elif opcion == "6":
            print('Fin de programa!')
            break
        else:
            print('Opción inválida')

if __name__ == "__main__":
    main()