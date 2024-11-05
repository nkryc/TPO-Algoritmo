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
    if  listas.contador_contribuyentes == 0:
        print("No se registraron contribuyentes.")
        return

    # Calculos 
    menor_edad = min( listas.edad_list)
    mayor_edad = max( listas.edad_list)
    promedio_edad = sum( listas.edad_list) /  listas.contador_contribuyentes
    fecha_mas_lejana = max( listas.fecha_declaracion_list)
    fecha_mas_cercana = min( listas.fecha_declaracion_list)
    menor_monto = min( listas.monto_a_declarar_list)
    mayor_monto = max( listas.monto_a_declarar_list)
    promedio_monto = sum( listas.monto_a_declarar_list) /  listas.contador_contribuyentes

    # Ranking profesiones
    ranking_profesiones = {}
    for profesion in listas.profesion_list:
        if profesion in ranking_profesiones:
            ranking_profesiones[profesion] += 1
        else:
            ranking_profesiones[profesion] = 1

    # Ranking origen de fondos
    ranking_origen_fondos = {}
    for origen in listas.origen_fondos_list:
        if origen in ranking_origen_fondos:
            ranking_origen_fondos[origen] += 1
        else:
            ranking_origen_fondos[origen] = 1

    # Muestra resultados :P
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

