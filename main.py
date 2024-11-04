from contribuyentes import ingresar_contribuyente, calcular_estadisticas, mostrar_resultados

def main():
    contribuyentes = []
    
    while True:
        contribuyente = ingresar_contribuyente()
        contribuyentes.append(contribuyente)
        
        continuar = input("¿Desea ingresar otro contribuyente? (si/nn): ")
        if continuar.lower() != 'si':
            break

    # Procesar datos y mostrar resultados
    estadisticas = calcular_estadisticas(contribuyentes)
    mostrar_resultados(estadisticas)

if __name__ == "__main__":
    main()
