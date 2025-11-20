from graph import Graph
g = Graph(is_directed=False)

# a. Insertar vertices con tipo de equipo
print('cargando vertices')
g.insert_vertex('Red Hat')
g.insert_vertex('Debian')
g.insert_vertex('Arch')
g.insert_vertex('Manjaro')
g.insert_vertex('Fedora')
g.insert_vertex('Ubuntu')
g.insert_vertex('Mint')
g.insert_vertex('Parrot')
g.insert_vertex('Guarani')
g.insert_vertex('MongoDB')
g.insert_vertex('Router 1')
g.insert_vertex('Router 2')
g.insert_vertex('Router 3')
g.insert_vertex('Switch 1')
g.insert_vertex('Switch 2')
g.insert_vertex('Impresora')

for vertex in g:
    if vertex.value in ['Manjaro', 'Fedora', 'Ubuntu', 'Mint', 'Parrot']:
        vertex.other_values = {'tipo': 'pc'}
    elif vertex.value in ['Red Hat', 'Debian', 'Arch']:
        vertex.other_values = {'tipo': 'notebook'}
    elif vertex.value in ['Guarani', 'MongoDB']:
        vertex.other_values = {'tipo': 'servidor'}
    elif vertex.value in ['Router 1', 'Router 2', 'Router 3']:
        vertex.other_values = {'tipo': 'router'}
    elif vertex.value in ['Switch 1', 'Switch 2']:
        vertex.other_values = {'tipo': 'switch'}
    elif vertex.value == 'Impresora':
        vertex.other_values = {'tipo': 'impresora'}

print('cargando aristas')


g.insert_edge('Red Hat', 'Router 2', 25)
g.insert_edge('Guarani', 'Router 2', 9)
g.insert_edge('Router 2', 'Router 3', 50)
g.insert_edge('Router 2', 'Router 1', 37)
g.insert_edge('Router 2', 'Switch 1', 37)


g.insert_edge('Router 3', 'Manjaro', 40)
g.insert_edge('Router 3', 'Switch 2', 61)
g.insert_edge('Router 3', 'Router 1', 43)


g.insert_edge('Router 1', 'Switch 1', 48)
g.insert_edge('Router 1', 'Fedora', 3)


g.insert_edge('Switch 1', 'Debian', 17)
g.insert_edge('Switch 1', 'Ubuntu', 18)
g.insert_edge('Switch 1', 'Impresora', 22)
g.insert_edge('Switch 1', 'Mint', 80)


g.insert_edge('Switch 2', 'Parrot', 12)
g.insert_edge('Switch 2', 'MongoDB', 5)
g.insert_edge('Switch 2', 'Arch', 56)

print('grafo cargado')

# b. Barrido en profundidad y amplitud desde notebooks
print('barrido profundidad desde Red Hat')
g.deep_sweep('Red Hat')

print('barrido profundidad desde Debian')
g.deep_sweep('Debian')

print('barrido profundidad desde Arch')
g.deep_sweep('Arch')

print('barrido amplitud desde Red Hat')
g.amplitude_sweep('Red Hat')

print('barrido amplitud desde Debian')
g.amplitude_sweep('Debian')

print('barrido amplitud desde Arch')
g.amplitude_sweep('Arch')

# c. Camino mas corto desde Manjaro, Red Hat, Fedora hasta Impresora
print('camino mas corto desde Manjaro a Impresora')
path_manjaro = g.dijkstra('Manjaro')
destino = 'Impresora'
peso_total = None
camino = []
while path_manjaro.size() > 0:
    value = path_manjaro.pop()
    if value[0] == destino:
        if peso_total is None:
            peso_total = value[1]
        camino.append(value[0])
        destino = value[2]
camino.reverse()
print('camino:', '-'.join(camino), 'peso:', peso_total)

print('camino mas corto desde Red Hat a Impresora')
path_redhat = g.dijkstra('Red Hat')
destino = 'Impresora'
peso_total = None
camino = []
while path_redhat.size() > 0:
    value = path_redhat.pop()
    if value[0] == destino:
        if peso_total is None:
            peso_total = value[1]
        camino.append(value[0])
        destino = value[2]
camino.reverse()
print('camino:', '-'.join(camino), 'peso:', peso_total)

print('camino mas corto desde Fedora a Impresora')
path_fedora = g.dijkstra('Fedora')
destino = 'Impresora'
peso_total = None
camino = []
while path_fedora.size() > 0:
    value = path_fedora.pop()
    if value[0] == destino:
        if peso_total is None:
            peso_total = value[1]
        camino.append(value[0])
        destino = value[2]
camino.reverse()
print('camino:', '-'.join(camino), 'peso:', peso_total)

# d. Arbol de expansion minima
print('arbol de expansion minima')
arbol = g.kruskal('Router 1')
print(arbol)
peso_total = 0
for edge in arbol.split(';'):
    parts = edge.split('-')
    if len(parts) == 3:
        peso_total += int(parts[2])
print('peso total:', peso_total)

# e. Desde que PC es el camino mas corto a Guarani
print('camino mas corto desde PCs a Guarani')
pcs = ['Manjaro', 'Fedora', 'Ubuntu', 'Mint', 'Parrot']
min_distancia = float('inf')
mejor_pc = None

for pc in pcs:
    path = g.dijkstra(pc)
    while path.size() > 0:
        value = path.pop()
        if value[0] == 'Guarani':
            if value[1] < min_distancia:
                min_distancia = value[1]
                mejor_pc = pc
            break

print('desde', mejor_pc, 'con peso', min_distancia)

# f. Desde que computadora del Switch 1 es el camino mas corto a MongoDB
print('camino mas corto desde computadoras de Switch 1 a MongoDB')
computadoras_sw1 = ['Debian', 'Ubuntu', 'Mint']
min_distancia = float('inf')
mejor_comp = None

for comp in computadoras_sw1:
    path = g.dijkstra(comp)
    while path.size() > 0:
        value = path.pop()
        if value[0] == 'MongoDB':
            if value[1] < min_distancia:
                min_distancia = value[1]
                mejor_comp = comp
            break

print('desde', mejor_comp, 'con peso', min_distancia)

# g. Cambiar conexion de impresora a Router 2 y resolver punto c
print('cambiando conexion de impresora a Router 2')
g.delete_edge('Switch 1', 'Impresora', 'value')
g.insert_edge('Router 2', 'Impresora', 15)

print('camino mas corto desde Manjaro a Impresora (nueva conexion)')
path_manjaro = g.dijkstra('Manjaro')
destino = 'Impresora'
peso_total = None
camino = []
while path_manjaro.size() > 0:
    value = path_manjaro.pop()
    if value[0] == destino:
        if peso_total is None:
            peso_total = value[1]
        camino.append(value[0])
        destino = value[2]
camino.reverse()
print('camino:', '-'.join(camino), 'peso:', peso_total)

print('camino mas corto desde Red Hat a Impresora (nueva conexion)')
path_redhat = g.dijkstra('Red Hat')
destino = 'Impresora'
peso_total = None
camino = []
while path_redhat.size() > 0:
    value = path_redhat.pop()
    if value[0] == destino:
        if peso_total is None:
            peso_total = value[1]
        camino.append(value[0])
        destino = value[2]
camino.reverse()
print('camino:', '-'.join(camino), 'peso:', peso_total)

print('camino mas corto desde Fedora a Impresora (nueva conexion)')
path_fedora = g.dijkstra('Fedora')
destino = 'Impresora'
peso_total = None
camino = []
while path_fedora.size() > 0:
    value = path_fedora.pop()
    if value[0] == destino:
        if peso_total is None:
            peso_total = value[1]
        camino.append(value[0])
        destino = value[2]
camino.reverse()
print('camino:', '-'.join(camino), 'peso:', peso_total)
