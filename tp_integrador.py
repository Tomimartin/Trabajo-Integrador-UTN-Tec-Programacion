import csv

# -------------------- CARGA DE DATOS --------------------
def cargar_paises(nombre_archivo):
    paises = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                pais = {
                    'nombre': fila['nombre'],
                    'poblacion': int(fila['poblacion']),
                    'superficie': int(fila['superficie']),
                    'continente': fila['continente']
                }
                paises.append(pais)
    except FileNotFoundError:
        print("No se encontró el archivo CSV.")
    return paises

# -------------------- BÚSQUEDAS Y FILTROS --------------------
def buscar_pais(paises, nombre):
    encontrados = []
    for p in paises:
        if nombre.lower() in p['nombre'].lower():
            encontrados.append(p)
    return encontrados

def filtrar_por_continente(paises, continente):
    filtrados = []
    for p in paises:
        if p['continente'].lower() == continente.lower():
            filtrados.append(p)
    return filtrados

def filtrar_por_poblacion(paises, min_pob, max_pob):
    filtrados = []
    for p in paises:
        if min_pob <= p['poblacion'] <= max_pob:
            filtrados.append(p)
    return filtrados

def filtrar_por_superficie(paises, min_sup, max_sup):
    filtrados = []
    for p in paises:
        if min_sup <= p['superficie'] <= max_sup:
            filtrados.append(p)
    return filtrados

# -------------------- ORDENAMIENTO --------------------
def ordenar_paises(paises, clave, descendente=False):
    n = len(paises)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if descendente:
                if paises[i][clave] < paises[j][clave]:
                    paises[i], paises[j] = paises[j], paises[i]
            else:
                if paises[i][clave] > paises[j][clave]:
                    paises[i], paises[j] = paises[j], paises[i]
    return paises

# -------------------- ESTADÍSTICAS --------------------
def mostrar_estadisticas(paises):
    if len(paises) == 0:
        print("No hay datos cargados.")
        return

    mayor_pob = paises[0]
    menor_pob = paises[0]
    suma_pob = 0
    suma_sup = 0
    continentes = {}

    for p in paises:
        if p['poblacion'] > mayor_pob['poblacion']:
            mayor_pob = p
        if p['poblacion'] < menor_pob['poblacion']:
            menor_pob = p
        suma_pob += p['poblacion']
        suma_sup += p['superficie']

        cont = p['continente']
        if cont not in continentes:
            continentes[cont] = 1
        else:
            continentes[cont] += 1

    prom_pob = suma_pob / len(paises)
    prom_sup = suma_sup / len(paises)

    print("\n ESTADÍSTICAS GLOBALES:")
    print(f"País con mayor población: {mayor_pob['nombre']} ({mayor_pob['poblacion']})")
    print(f"País con menor población: {menor_pob['nombre']} ({menor_pob['poblacion']})")
    print(f"Población promedio: {int(prom_pob)}")
    print(f"Superficie promedio: {int(prom_sup)}")
    print("Cantidad de países por continente:")
    for cont, cant in continentes.items():
        print(f" - {cont}: {cant}")
        


# -------------------- MENÚ PRINCIPAL --------------------
def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Buscar país por nombre")
    print("2. Filtrar países por continente")
    print("3. Filtrar por rango de población")
    print("4. Filtrar por rango de superficie")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("0. Salir")

def main():
    paises = cargar_paises("paises.csv")
    if not paises:
        return

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese nombre o parte del nombre del país: ")
            resultado = buscar_pais(paises, nombre)
            
            if len(resultado) == 0:
             print("❌ No se encontró ningún país con ese nombre.")
             continue
            
            
            for p in resultado:
                print(f"Pais:{p['nombre']} | Población:{p['poblacion']} habitantes | Superficie:{p['superficie']}km² | Continente:{p['continente']}")

        elif opcion == "2":
            cont = input("Ingrese continente: ")
            resultado = filtrar_por_continente(paises, cont)
            
            
            for p in resultado:
                print(f"Pais:{p['nombre']} | Población:{p['poblacion']} habitantes | Superficie:{p['superficie']}km² | Continente:{p['continente']}")

        elif opcion == "3":
            while True:
             min_p = int(input("Población mínima: "))
             max_p = int(input("Población máxima: "))
             if max_p > min_p:
              resultado = filtrar_por_poblacion(paises, min_p, max_p)
              
              if len(resultado) == 0:
                print("❌ No se encontraron países dentro de ese rango de población.")
                break
            
              for p in resultado:
                print(f"Pais:{p['nombre']} | Población:{p['poblacion']} habitantes | Superficie:{p['superficie']}km² | Continente:{p['continente']}")
              
              break
             else:
                print("Ingrese un rango mayor al mínimo.")
                

        elif opcion == "4":
          while True:
            min_s = int(input("Superficie mínima: "))
            max_s = int(input("Superficie máxima: "))
            if max_s > min_s:
             resultado = filtrar_por_superficie(paises, min_s, max_s)
             
             if len(resultado) == 0:
                print("❌ No se encontraron países dentro de ese rango de superficie.")
                break
             for p in resultado:
                print(f"Pais:{p['nombre']} | Población:{p['poblacion']} habitantes | Superficie:{p['superficie']}km² | Continente:{p['continente']}")
                
             break
            else:
               print("Ingrese un rango mayor al mínimo.") 

        elif opcion == "5":
            print("Ordenar por: 1-Nombre 2-Población 3-Superficie")
            criterio = input("Elija opción: ")
            descendente = input("¿Descendente? (s/n): ").lower() == "s"
            if criterio == "1":
                clave = "nombre"
            elif criterio == "2":
                clave = "poblacion"
            else:
                clave = "superficie"
            ordenados = ordenar_paises(paises[:], clave, descendente)# Hago una copia para no modificar la lista original
            for p in ordenados:
                print(f"Pais:{p['nombre']} | Población:{p['poblacion']} habitantes | Superficie:{p['superficie']}km² | Continente:{p['continente']}")

        elif opcion == "6":
            mostrar_estadisticas(paises)

        elif opcion == "0":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida.")

# -------------------- EJECUCIÓN --------------------
if __name__ == "__main__":
    main()
