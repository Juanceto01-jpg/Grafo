from graph import Graph

g = Graph(is_directed=False)

# a. Insertar vertices (ambientes de la casa)
print('cargando ambientes')
g.insert_vertex('cocina')
g.insert_vertex('comedor')
g.insert_vertex('cochera')
g.insert_vertex('quincho')
g.insert_vertex('banio 1')
g.insert_vertex('banio 2')
g.insert_vertex('habitacion 1')
g.insert_vertex('habitacion 2')
g.insert_vertex('sala de estar')
g.insert_vertex('terraza')
g.insert_vertex('patio')

# b. Cargar aristas (minimo 3 por vertice, 2 vertices con 5 aristas)
print('cargando aristas')


g.insert_edge('cocina', 'comedor', 3)
g.insert_edge('cocina', 'patio', 5)
g.insert_edge('cocina', 'sala de estar', 4)
g.insert_edge('cocina', 'banio 1', 6)
g.insert_edge('cocina', 'terraza', 8)


g.insert_edge('comedor', 'sala de estar', 2)
g.insert_edge('comedor', 'habitacion 1', 5)
g.insert_edge('comedor', 'habitacion 2', 6)
g.insert_edge('comedor', 'quincho', 7)


g.insert_edge('cochera', 'patio', 4)
g.insert_edge('cochera', 'quincho', 6)
g.insert_edge('cochera', 'terraza', 10)


g.insert_edge('quincho', 'patio', 3)


g.insert_edge('banio 1', 'habitacion 1', 2)
g.insert_edge('banio 1', 'sala de estar', 4)


g.insert_edge('banio 2', 'habitacion 2', 2)
g.insert_edge('banio 2', 'habitacion 1', 3)
g.insert_edge('banio 2', 'terraza', 5)

g.insert_edge('habitacion 2', 'sala de estar', 4)

print('grafo cargado')

# c. Arbol de expansion minima
print('arbol de expansion minima')
arbol = g.kruskal('cocina')
print(arbol)

peso_total = 0
for edge in arbol.split(';'):
    parts = edge.split('-')
    if len(parts) == 3:
        peso_total += int(parts[2])

print('metros de cable necesarios:', peso_total)

# d. Camino mas corto desde habitacion 1 hasta sala de estar
print('camino mas corto desde habitacion 1 a sala de estar')
path = g.dijkstra('habitacion 1')

destino = 'sala de estar'
peso_total = None
camino = []

while path.size() > 0:
    value = path.pop()
    if value[0] == destino:
        if peso_total is None:
            peso_total = value[1]
        camino.append(value[0])
        destino = value[2]

camino.reverse()
print('camino:', '-'.join(camino))
print('metros de cable de red necesarios:', peso_total)
