import networkx as nx
import matplotlib.pyplot as plt

#rutasFile = "/Users/alejandraayala/Documents/Trabajos_UVG/Semestre 3/EstructuraDatos/HDT9_Alg.Dijkstra/rutas.txt"
rutasFile = "rutas.txt"

class Rutas:
    # Crear grafo
    def __init__(self, rutasFile):
        self.grafo = nx.Graph()
        self.cargar_rutas(rutasFile)

    # Cargar rutas desde el file
    def cargar_rutas(self, rutasFile):
        with open(rutasFile, 'r') as file:
            for line in file:
                origen, destino, costo = line.strip().split(',')
                costo = int(costo)
                self.grafo.add_edge(origen, destino, weight=costo)
                self.grafo.add_edge(destino, origen, weight=costo)  # Ruta simétrica

    # Hacer display de mapa
    def display_map(self, salida):
        if salida not in self.grafo:
            print(f'La estación {salida} no existe en el mapa.')
            return

        destinos = nx.shortest_path(self.grafo, source=salida)
        destinos_info = []
        for destino, path in destinos.items():
            costo = sum(self.grafo[path[i]][path[i+1]]['weight'] for i in range(len(path)-1))
            destinos_info.append((destino, costo))

        # Mostrar información de destinos y costos
        print(f'Resultados desde la Estación {salida}:')
        for destino, costo in destinos_info:
            print(f'Destino: {destino}, Costo: {costo}')
        
        # Mostrar resultados en forma gráfica
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

        

    # ver wel grafo 
    def visualizar_grafo(self):
        # Dibujar el grafo utilizando networkx y matplotlib
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(self.grafo)  # Layout para posicionar nodos
        nx.draw(self.grafo, pos, with_labels=True, node_color='skyblue', node_size=600, font_size=10, font_color='black')

        # Mostrar pesos de las aristas
        edge_labels = nx.get_edge_attributes(self.grafo, 'weight')
        nx.draw_networkx_edge_labels(self.grafo, pos, edge_labels=edge_labels)

        plt.title('Mapa de Rutas')
        plt.show()

    # algortimo de dijkstra
    def dijkstra_mejores_rutas(self, salida):
        if salida not in self.grafo:
            print(f'La estación {salida} no existe en el mapa.')
            return

        # Aplicar algoritmo de Dijkstra para encontrar las mejores rutas desde la estación de salida
        mejores_rutas = nx.single_source_dijkstra_path(self.grafo, source=salida, weight='weight')
        mejores_costos = nx.single_source_dijkstra_path_length(self.grafo, source=salida, weight='weight')

        # Mostrar los resultados de las mejores rutas y costos
        print(f'Mejores rutas desde la Estación {salida}:')
        for destino, ruta in mejores_rutas.items():
            costo = mejores_costos[destino]
            print(f'Destino: {destino}, Ruta: {ruta}, Costo: {costo}')

def main():
    scheduler = Rutas(rutasFile)

    scheduler.visualizar_grafo()

    start_station = input("Entre la estacion de salida: ")
    scheduler.display_map(start_station)
    scheduler.dijkstra_mejores_rutas(start_station)



if __name__ == "__main__":
    main()
