# Trabajo-Integrador-UTN-Tec-Programacion
📘 Descripción del Programa

Este programa permite cargar información de países desde un archivo CSV y realizar diferentes operaciones sobre esos datos.
Entre sus funcionalidades se encuentran:

.Buscar países por nombre.

.Filtrar países por continente.

.Filtrar por rangos de población o superficie.

.Ordenar la lista según distintos criterios.

.Mostrar estadísticas globales (mayor y menor población, promedios, cantidad por continente).

.Interacción mediante un menú en consola.

El objetivo es practicar el uso de listas, diccionarios, filtros, ordenamientos y carga externa de datos utilizando Python y el módulo csv.

🖥️ Instrucciones de Uso

1.Asegurate de tener el archivo paises.csv en el mismo directorio que el script.

2.El CSV debe contener estas columnas:

nombre

poblacion

superficie

continente

3.Ejecutá el programa.

4.Al iniciar, aparecerá un menú interactivo con opciones numeradas.

5.Ingresá el número de la acción que quieras realizar y seguí las instrucciones en pantalla.

📥 Ejemplos de Entradas y Salidas
🔍 1. Búsqueda por nombre

Entrada:

Seleccione una opción: 1
Ingrese nombre o parte del nombre del país: arg


Salida:

País: Argentina | Población: 45376763 habitantes | Superficie: 2780400 km² | Continente: América

🌍 2. Filtrar por continente

Entrada:

Seleccione una opción: 2
Ingrese continente: Europa


Salida (ejemplo):

País: Francia | Población: 67081000 | Superficie: 643801 km² | Continente: Europa
País: Alemania | Población: 83149300 | Superficie: 357386 km² | Continente: Europa

👥 3. Filtrar por población

Entrada:

Seleccione una opción: 3
Población mínima: 1000000
Población máxima: 5000000


Salida:

País: Uruguay | Población: 3423100 | Superficie: 176215 km² | Continente: América


📊 4. Mostrar estadísticas

Salida:

ESTADÍSTICAS GLOBALES:
País con mayor población: China (1402112000)
País con menor población: Islandia (372520)
Población promedio: 120452000
Superficie promedio: 523000
Cantidad de países por continente:
 - América: 15
 - Europa: 18
 - Asia: 20


| Nombre       | Participación                                         |
| ------------ | ----------------------------------------------------- |
| Tomás Martín | Desarrollo de funciones de carga, filtros y búsqueda. |
| Emir Gris    | Implementación de ordenamiento y estadísticas.        |
| Tomás Martín | Diseño del menú interactivo, pruebas y validación.    |
| Emir Gris    | Documentación y armado del archivo README.md.         |
