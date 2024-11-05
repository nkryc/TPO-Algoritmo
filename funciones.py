import listas

def agregar_contribuyente(dni, apellido, nombre, edad, fecha_nacimiento, profesion, fecha_declaracion, monto_a_declarar, origen_fondos):
   
    listas.dni_list.append(dni)
    listas.apellido_list.append(apellido)
    listas.nombre_list.append(nombre)
    listas.edad_list.append(edad)
    listas.fecha_nacimiento_list.append(fecha_nacimiento)
    listas.profesion_list.append(profesion)
    listas.fecha_declaracion_list.append(fecha_declaracion)
    listas.monto_a_declarar_list.append(monto_a_declarar)
    listas.origen_fondos_list.append(origen_fondos)
    
    listas.contador_contribuyentes += 1

def calcular_estadisticas():
    if listas.contador_contribuyentes == 0:
        print("No se registraron contribuyentes.")
        return

    # Calculo de menor, mayor y promedio de edades
    menor_edad = float('inf')
    mayor_edad = float('-inf')
    suma_edades = 0

    for edad in listas.edad_list:
        if edad < menor_edad:
            menor_edad = edad
        if edad > mayor_edad:
            mayor_edad = edad
        suma_edades += edad

    promedio_edad = suma_edades / listas.contador_contribuyentes

    # Calculo de fecha de declaración más lejana y más cercana
    fecha_mas_lejana = listas.fecha_declaracion_list[0]
    fecha_mas_cercana = listas.fecha_declaracion_list[0]

    for fecha in listas.fecha_declaracion_list:
        if fecha > fecha_mas_lejana:
            fecha_mas_lejana = fecha
        if fecha < fecha_mas_cercana:
            fecha_mas_cercana = fecha

    # Calculo de menor, mayor y promedio de montos
    menor_monto = float('inf')
    mayor_monto = float('-inf')
    suma_montos = 0

    for monto in listas.monto_a_declarar_list:
        if monto < menor_monto:
            menor_monto = monto
        if monto > mayor_monto:
            mayor_monto = monto
        suma_montos += monto

    promedio_monto = suma_montos / listas.contador_contribuyentes

    # Ranking de profesiones
    ranking_profesiones = {}
    for profesion in listas.profesion_list:
        if profesion in ranking_profesiones:
            ranking_profesiones[profesion] += 1
        else:
            ranking_profesiones[profesion] = 1

    # Ranking de origen de fondos
    ranking_origen_fondos = {}
    for origen in listas.origen_fondos_list:
        if origen in ranking_origen_fondos:
            ranking_origen_fondos[origen] += 1
        else:
            ranking_origen_fondos[origen] = 1

    # Mostrar resultados
    print(f"\nTotal de personas registradas: {listas.contador_contribuyentes}")
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

