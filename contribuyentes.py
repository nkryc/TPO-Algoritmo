from datetime import datetime
from collections import Counter

def ingresar_contribuyente():
    dni = input("Ingrese DNI: ")
    apellido = input("Ingrese Apellido: ")
    nombre = input("Ingrese Nombre: ")
    edad = int(input("Ingrese Edad: "))
    fecha_nacimiento = input("Ingrese Fecha de Nacimiento (DD/MM/YYYY): ")
    profesion = input("Ingrese Profesión: ")
    fecha_declaracion = input("Ingrese Fecha de Declaración (DD/MM/YYYY): ")
    monto_a_declarar = float(input("Ingrese Monto a Declarar: "))
    origen_fondos = input("Ingrese Origen de los Fondos: ")
    activo_regularizado = input("Ingrese Activo Regularizado: ")
    ubicacion_activo = input("Ubicación de los bienes (Argentina/Exterior): ")

    return {
        "dni": dni,
        "apellido": apellido,
        "nombre": nombre,
        "edad": edad,
        "fecha_nacimiento": fecha_nacimiento,
        "profesion": profesion,
        "fecha_declaracion": datetime.strptime(fecha_declaracion, "%d/%m/%Y"),
        "monto_a_declarar": monto_a_declarar,
        "origen_fondos": origen_fondos,
        "activo_regularizado": activo_regularizado,
        "ubicacion_activo": ubicacion_activo
    }

def calcular_estadisticas(contribuyentes):
    total_personas = len(contribuyentes)
    edades = [c["edad"] for c in contribuyentes]
    fechas_declaracion = [c["fecha_declaracion"] for c in contribuyentes]
    montos = [c["monto_a_declarar"] for c in contribuyentes]
    activos = [c["activo_regularizado"] for c in contribuyentes]
    profesiones = [c["profesion"] for c in contribuyentes]
    origen_fondos = [c["origen_fondos"] for c in contribuyentes]
    ubicaciones = [c["ubicacion_activo"] for c in contribuyentes]

    menor_edad = min(edades)
    mayor_edad = max(edades)
    promedio_edad = sum(edades) / total_personas

    fecha_mas_lejana = min(fechas_declaracion)
    fecha_mas_cercana = max(fechas_declaracion)

    menor_monto = min(montos)
    mayor_monto = max(montos)
    promedio_monto = sum(montos) / total_personas

    ranking_profesiones = Counter(profesiones)
    ranking_origen_fondos = Counter(origen_fondos)

    activos_frecuencia = Counter(activos)
    activo_mas_frecuente = activos_frecuencia.most_common(1)[0][0]
    activo_menos_frecuente = activos_frecuencia.most_common()[-1][0]

    porcentaje_bienes_argentina = (ubicaciones.count("Argentina") / total_personas) * 100
    porcentaje_bienes_exterior = (ubicaciones.count("Exterior") / total_personas) * 100

    return {
        "total_personas": total_personas,
        "menor_edad": menor_edad,
        "mayor_edad": mayor_edad,
        "promedio_edad": promedio_edad,
        "fecha_mas_lejana": fecha_mas_lejana,
        "fecha_mas_cercana": fecha_mas_cercana,
        "menor_monto": menor_monto,
        "mayor_monto": mayor_monto,
        "promedio_monto": promedio_monto,
        "ranking_profesiones": ranking_profesiones,
        "ranking_origen_fondos": ranking_origen_fondos,
        "activo_mas_frecuente": activo_mas_frecuente,
        "activo_menos_frecuente": activo_menos_frecuente,
        "porcentaje_bienes_argentina": porcentaje_bienes_argentina,
        "porcentaje_bienes_exterior": porcentaje_bienes_exterior
    }

def mostrar_resultados(estadisticas):
    print(f"\nTotal de personas registradas: {estadisticas['total_personas']}")
    print(f"Menor edad: {estadisticas['menor_edad']}")
    print(f"Mayor edad: {estadisticas['mayor_edad']}")
    print(f"Edad promedio: {estadisticas['promedio_edad']:.2f}")
    print(f"Fecha de declaración más lejana: {estadisticas['fecha_mas_lejana'].strftime('%d/%m/%Y')}")
    print(f"Fecha de declaración más cercana: {estadisticas['fecha_mas_cercana'].strftime('%d/%m/%Y')}")
    print(f"Menor monto a declarar: {estadisticas['menor_monto']}")
    print(f"Mayor monto a declarar: {estadisticas['mayor_monto']}")
    print(f"Promedio de monto a declarar: {estadisticas['promedio_monto']:.2f}")

    print("\nRanking de profesiones:")
    for profesion, count in estadisticas['ranking_profesiones'].items():
        print(f"{profesion}: {count}")

    print("\nRanking de origen de fondos:")
    for origen, count in estadisticas['ranking_origen_fondos'].items():
        print(f"{origen}: {count}")

    print(f"\nActivo más frecuente: {estadisticas['activo_mas_frecuente']}")
    print(f"Activo menos frecuente: {estadisticas['activo_menos_frecuente']}")
    print(f"Porcentaje de bienes en Argentina: {estadisticas['porcentaje_bienes_argentina']:.2f}%")
    print(f"Porcentaje de bienes en el exterior: {estadisticas['porcentaje_bienes_exterior']:.2f}%")
