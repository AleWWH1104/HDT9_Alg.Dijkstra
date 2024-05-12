# Hoja de trabajo No. 9  
Algoritmos y Estructura de Datos

Iris Ayala
David Dominguez
  
Este proyecto implementa una red de transporte utilizando NetworkX en Python. Permite cargar rutas desde un archivo, visualizar el mapa de rutas, mostrar rutas desde una estación específica y calcular las mejores rutas utilizando el algoritmo de Dijkstra.

## Contenido  

- Estructura del Proyecto
- Descripción de Clases y Funciones

## Uso

1. Coloca tu archivo de rutas (rutas.txt) en la raíz del proyecto con el siguiente formato:

   origen,destino,costo
   A,B,10
   B,C,5
   ...

2. Ejecuta el programa principal:

   python main.py

3. Selecciona las opciones del menú interactivo para explorar las funcionalidades:

   - Visualizar el mapa de rutas.
   - Mostrar rutas desde una estación específica.
   - Calcular las mejores rutas desde una estación utilizando Dijkstra.

## Estructura del Proyecto

- main.py: Archivo principal que contiene la lógica principal del programa.
- rutas.txt: Archivo de ejemplo que contiene las rutas de la red de transporte.
- README.md: Documentación del proyecto.
- requirements.txt: Archivo que lista las dependencias del proyecto.

![UML](https://github.com/AleWWH1104/HDT9_Alg.Dijkstra/assets/84152698/4768d5ee-99e7-47d0-882d-8ba641809913)


## Descripción de Clases y Funciones

Clase Rutas:

- Descripción: Representa la red de transporte y permite realizar operaciones relacionadas con las rutas.
  
  - Atributos:
    - grafo: Grafo que representa la red de transporte donde los nodos son estaciones y los bordes son rutas con costos.
  
  - Métodos:
    - __init__(self, rutasFile): Constructor que inicializa la red de transporte cargando rutas desde un archivo.
    - cargar_rutas(self, rutasFile): Carga las rutas desde un archivo en el grafo de la red de transporte.
    - display_map(self, salida): Muestra las rutas y costos desde una estación específica en formato de texto y gráfico.
    - visualizar_grafo(self): Visualiza el grafo completo de la red de transporte utilizando matplotlib.
    - dijkstra_mejores_rutas(self, salida): Calcula y muestra las mejores rutas desde una estación utilizando el algoritmo de Dijkstra.

Función main():

- Descripción: Función principal que ejecuta el programa e interactúa con el usuario a través de un menú.

  - Funcionalidades:
    - Visualizar el mapa de rutas.
    - Mostrar rutas desde una estación específica.
    - Calcular las mejores rutas desde una estación utilizando Dijkstra.
