"""
    Hoja de trabajo No. 9
    Algoritmos y Estructura de Datos

    sistema para agendar viajes y sistema con algoritmo de Dijkstra 

    Iris Ayala
    David Dominguez

    Mayo 11, 2024

"""

import networkx as nx
import matplotlib.pyplot as plt

# Definición de la clase Rutas que representa la red de transporte
class Rutas:
    """
    Clase para modelar una red de transporte y realizar operaciones relacionadas con las rutas.
    
    Attributes:
    -----------
    grafo : networkx.Graph
        Grafo que representa la red de transporte donde los nodos son estaciones y los bordes son rutas con costos.
    """

    def __init__(self, rutasFile):
        """
        Inicializa una instancia de la clase Rutas cargando las rutas desde un archivo.

        Parameters:
        -----------
        rutasFile : str
            Ruta del archivo que contiene las rutas en el formato 'origen,destino,costo'.
        """
        self.grafo = nx.Graph()
        self.cargar_rutas(rutasFile)

    def cargar_rutas(self, rutasFile):
        """
        Carga las rutas desde un archivo en el grafo de la red de transporte.

        Parameters:
        -----------
        rutasFile : str
            Ruta del archivo que contiene las rutas en el formato 'origen,destino,costo'.
        """
        with open(rutasFile, 'r') as file:
            for line in file:
                origen, destino, costo = line.strip().split(',')
                costo = int(costo)
                self.grafo.add_edge(origen, destino, weight=costo)
                self.grafo.add_edge(destino, origen, weight=costo)  # Agregar ruta simétrica

    def display_map(self, salida):
        """
        Muestra las rutas y costos desde una estación específica en formato de texto y gráfico.

        Parameters:
        -----------
        salida : str
            Nombre de la estación de salida desde la cual se desean mostrar las rutas.
        """
        if salida not in self.grafo:
            print(f'La estación {salida} no existe en el mapa.')
            return

        # Calcular las rutas más cortas desde la estación de salida
        destinos = nx.shortest_path(self.grafo, source=salida)
        destinos_info = []
        for destino, path in destinos.items():
            costo = sum(self.grafo[path[i]][path[i+1]]['weight'] for i in range(len(path)-1))
            destinos_info.append((destino, costo))

        # Mostrar información de destinos y costos en texto
        print(f'Resultados desde la Estación {salida}:')
        for destino, costo in destinos_info:
            print(f'Destino: {destino}, Costo: {costo}')
        
        # Mostrar resultados en forma gráfica utilizando matplotlib
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(self.grafo)
        
        # Dibujar nodos y aristas del grafo completo
        nx.draw(self.grafo, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_color='black')

        # Resaltar nodo de salida en rojo
        nx.draw_networkx_nodes(self.grafo, pos, nodelist=[salida], node_color='red', node_size=700)

        # Dibujar aristas y etiquetas de costo para destinos desde la estación de salida
        for destino, costo in destinos_info:
            path = nx.shortest_path(self.grafo, source=salida, target=destino)
            edge_labels = {(path[i], path[i+1]): self.grafo[path[i]][path[i+1]]['weight'] for i in range(len(path)-1)}
            nx.draw_networkx_edges(self.grafo, pos, edgelist=[(path[i], path[i+1]) for i in range(len(path)-1)], edge_color='red', width=2)
            nx.draw_networkx_edge_labels(self.grafo, pos, edge_labels=edge_labels, font_color='red')

        plt.title(f'Rutas desde la Estación {salida}')
        plt.show()

    def visualizar_grafo(self):
        """
        Visualiza el grafo completo de la red de transporte utilizando matplotlib.
        """
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(self.grafo)  # Layout para posicionar nodos
        nx.draw(self.grafo, pos, with_labels=True, node_color='skyblue', node_size=600, font_size=10, font_color='black')

        # Mostrar pesos de las aristas como etiquetas
        edge_labels = nx.get_edge_attributes(self.grafo, 'weight')
        nx.draw_networkx_edge_labels(self.grafo, pos, edge_labels=edge_labels)

        plt.title('Mapa de Rutas')
        plt.show()

    def dijkstra_mejores_rutas(self, salida):
        """
        Calcula y muestra las mejores rutas desde una estación utilizando el algoritmo de Dijkstra.

        Parameters:
        -----------
        salida : str
            Nombre de la estación de salida desde la cual se desean calcular las mejores rutas.
        """
        if salida not in self.grafo:
            print(f'La estación {salida} no existe en el mapa.')
            return

        # Aplicar algoritmo de Dijkstra para encontrar las mejores rutas
        mejores_rutas = nx.single_source_dijkstra_path(self.grafo, source=salida, weight='weight')
        mejores_costos = nx.single_source_dijkstra_path_length(self.grafo, source=salida, weight='weight')

        # Mostrar los resultados de las mejores rutas y costos
        print(f'Mejores rutas desde la Estación {salida}:')
        for destino, ruta in mejores_rutas.items():
            costo = mejores_costos[destino]
            print(f'Destino: {destino}, Ruta: {ruta}, Costo: {costo}')

def main():
    # Archivo que contiene las rutas de la red de transporte
    rutasFile = "rutas.txt"
    #rutasFile = "/Users/alejandraayala/Documents/Trabajos_UVG/Semestre 3/EstructuraDatos/HDT9_Alg.Dijkstra/rutas.txt"

    # Crear instancia de la clase Rutas
    scheduler = Rutas(rutasFile)

    # Menú interactivo para utilizar las funcionalidades de la red de transporte
    while True:
        print("\nMenu")
        print("1. Visualizar Mapa de Rutas")
        print("2. Mostrar Rutas desde una Estación")
        print("3. Calcular Mejores Rutas desde una Estación (con Dijkstra)")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            scheduler.visualizar_grafo()
        elif opcion == '2':
            start_station = input("Ingrese la estacion de salida: ")
            scheduler.display_map(start_station)
        elif opcion == '3':
            start_station = input("Ingrese la estacion de salida: ")
            scheduler.dijkstra_mejores_rutas(start_station)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Error: seleccione una opción válida (1-4)")

if __name__ == "__main__":
    main()
