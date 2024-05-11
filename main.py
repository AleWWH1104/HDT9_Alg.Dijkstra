import networkx as nx

rutasFile = "/Users/alejandraayala/Documents/Trabajos_UVG/Semestre 3/EstructuraDatos/HDT9_Alg.Dijkstra/rutas.txt"
#Crear grafo
def crear_grafo():
    grafo = nx.Graph()
    with open(rutasFile, 'r') as file:
        for line in file:
            origen, destino, costo = line.strip().split(',')
            costo = int(costo)
            grafo.add_edge(origen, destino, weight=costo)
            grafo.add_edge(destino, origen, weight=costo)  # Ruta simétrica
    return grafo

