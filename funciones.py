import listas

def agregar_contribuyente(dni, apellido, nombre, edad, fecha_nacimiento, profesion, fecha_declaracion, monto_a_declarar, origen_fondos):
   
    datos.dni_list.append(dni)
    datos.apellido_list.append(apellido)
    datos.nombre_list.append(nombre)
    datos.edad_list.append(edad)
    datos.fecha_nacimiento_list.append(fecha_nacimiento)
    datos.profesion_list.append(profesion)
    datos.fecha_declaracion_list.append(fecha_declaracion)
    datos.monto_a_declarar_list.append(monto_a_declarar)
    datos.origen_fondos_list.append(origen_fondos)
    
   
    datos.contador_contribuyentes += 1

def calcular_estadisticas():
    if datos.contador_contribuyentes == 0:
        print("No se registraron contribuyentes.")
        return

    # Cálculos de estadísticas
    menor_edad = min(datos.edad_list)
    mayor_edad = max(datos.edad_list)
    promedio_edad = sum(datos.edad_list) / datos.contador_contribuyentes
    fecha_mas_lejana = max(datos.fecha_declaracion_list)
    fecha_mas_cercana = min(datos.fecha_declaracion_list)
    menor_monto = min(datos.monto_a_declarar_list)
    mayor_monto = max(datos.monto_a_declarar_list)
    promedio_monto = sum(datos.monto_a_declarar_list) / datos.contador_contribuyentes

    # Ranking de profesiones
    ranking_profesiones = {}
    for profesion in datos.profesion_list:
        if profesion in ranking_profesiones:
            ranking_profesiones[profesion] += 1
        else:
            ranking_profesiones[profesion] = 1

    # Ranking de origen de fondos
    ranking_origen_fondos = {}
    for origen in datos.origen_fondos_list:
        if origen in ranking_origen_fondos:
            ranking_origen_fondos[origen] += 1
        else:
            ranking_origen_fondos[origen] = 1

    # Mostrar los resultados
    print(f"\nTotal de personas registradas: {datos.contador_contribuyentes}")
    print(f"Menor edad: {menor_edad}")
    print(f"Mayor edad: {mayor_edad}")
    print(f"Edad promedio: {promedio_edad:.2f}")
    print(f"Fecha de declaración más lejana: {fecha_mas_lejana}")
    print(f"Fecha de declaración más cercana: {fecha_mas_cercana}")
    print(f"Menor monto a declarar: {menor_monto}")
    print(f"Mayor monto a declarar: {mayor_monto}")
    print(f"Promedio de monto a declarar: {promedio_monto:.2f}")

    print("\nRanking de profesiones:")
    for profesion, count in ranking_profesiones.items():
        print(f"{profesion}: {count}")

    print("\nRanking de origen de fondos:")
    for origen, count in ranking_origen_fondos.items():
        print(f"{origen}: {count}")

