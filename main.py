import networkx as nx

rutasFile = "/Users/alejandraayala/Documents/Trabajos_UVG/Semestre 3/EstructuraDatos/HDT9_Alg.Dijkstra/rutas.txt"

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
        for destino, path in destinos.items():
            costo = sum(self.grafo[path[i]][path[i+1]]['weight'] for i in range(len(path)-1))
            print(f'Destino: {destino}, Costo: {costo}')

def main():
    scheduler = Rutas(rutasFile)
    start_station = input("Entre la estacion de salida: ")
    scheduler.display_map(start_station)

if __name__ == "__main__":
    main()
