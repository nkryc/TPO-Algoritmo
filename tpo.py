n = int(input("¿Cuántos contribuyentes desea registrar?: "))
dnis = [None] * n
apellidos = [None] * n
nombres = [None] * n
edades = [None] * n
fechas_nacimiento = [None] * n
profesiones = [None] * n
fechas_declaracion = [None] * n
montos = [None] * n
origenes_fondos = [None] * n


for i in range(n):
    print(f"\nRegistro del contribuyente {i + 1}:")
    dnis[i] = input("Ingrese DNI: ")
    apellidos[i] = input("Ingrese Apellido: ")
    nombres[i] = input("Ingrese Nombre: ")
    edades[i] = int(input("Ingrese Edad: "))
    fechas_nacimiento[i] = input("Ingrese Fecha de nacimiento: ")
    profesiones[i] = input("Ingrese Profesión: ")
    fechas_declaracion[i] = input("Ingrese Fecha de declaración: ")
    montos[i] = float(input("Ingrese Monto a declarar: "))
    origenes_fondos[i] = input("Ingrese Origen de los fondos: ")


print(f"\nTotal de contribuyentes: {n}")
print(f"Menor edad: {min(edades)}, Mayor edad: {max(edades)}, Edad promedio: {sum(edades) / n:.2f}")
print(f"Fecha más lejana: {min(fechas_declaracion)}, Fecha más cercana: {max(fechas_declaracion)}")
print(f"Monto mínimo: {min(montos)}, Monto máximo: {max(montos)}, Monto promedio: {sum(montos) / n:.2f}")
