while registrando:
    print("\n--- Registro de Contribuyente ---")
    dni = input("DNI: ")
    apellido = input("Apellido: ")
    nombre = input("Nombre: ")
    fecha_nacimiento_str = input("Fecha de nacimiento (DD/MM/AAAA): ")
    fecha_nacimiento = convertir_fecha(fecha_nacimiento_str)
    edad = datetime.today().year - fecha_nacimiento.year

    profesion = input("Profesión: ")
    fecha_declaracion_str = input("Fecha de declaración (DD/MM/AAAA): ")
    fecha_declaracion = convertir_fecha(fecha_declaracion_str)

    monto_declarar = float(input("Monto a declarar: "))
    origen_fondos = input("Origen de los fondos: ")

    contribuyente = {
        'dni': dni,
        'apellido': apellido,
        'nombre': nombre,
        'edad': edad,
        'fecha_nacimiento': fecha_nacimiento,
        'profesion': profesion,
        'fecha_declaracion': fecha_declaracion,
        'monto_declarar': monto_declarar,
        'origen_fondos': origen_fondos
    }

    contribuyentes.append(contribuyente)

    continuar = input("¿Desea registrar otro contribuyente? (S/N): ").lower()
    registrando = continuar == 's'