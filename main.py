import listas
import funciones

def main():
    
    while True:
        dni = input("Ingrese DNI: ")
        apellido = input("Ingrese Apellido: ")
        nombre = input("Ingrese Nombre: ")
        edad = int(input("Ingrese Edad: "))
        fecha_nacimiento = input("Ingrese Fecha de Nacimiento (DD/MM/YYYY): ")
        profesion = input("Ingrese Profesión: ")
        fecha_declaracion = input("Ingrese Fecha de Declaración (DD/MM/YYYY): ")
        monto_a_declarar = float(input("Ingrese Monto a Declarar: "))
        origen_fondos = input("Ingrese Origen de los Fondos: ")

        # Recoge la informacion
        funciones.agregar_contribuyente(dni, apellido, nombre, edad, fecha_nacimiento, profesion, fecha_declaracion, monto_a_declarar, origen_fondos)

        continuar = input("¿Desea ingresar otro contribuyente? (s/n): ")
        if continuar.lower() != 's':
            break

    # Calcula y muestra las estadisticas
    funciones.calcular_estadisticas()

if __name__ == "__main__":
    main()
