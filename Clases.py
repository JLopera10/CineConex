from collections import defaultdict, deque

class Nodo:
    def __init__(self, id, nombre, rol):
        self.next = defaultdict(lambda: None)
        self.id = id
        self.nombre = nombre
        self.rol = rol


class Pelicula:
    def __init__(self, link_poster, titulo, fecha_salida,
                 certificado, duracion, genero, imdb_rating,
                 descripcion, puntaje, votos, ganancia):
        self.link_poster = link_poster
        self.titulo = titulo
        self.fecha_salida = fecha_salida
        self.certificado = certificado
        self.duracion = duracion
        self.genero = genero
        self.imdb_rating = imdb_rating
        self.descripcion = descripcion
        self.puntaje = puntaje
        self.votos = votos
        self.ganancia = ganancia
        self.head = None
        self.tail = None

    def agregarPersona(self, persona, grafo):
        if self.head is None:
            self.head = persona
            self.tail = persona
        else:
            self.tail.next[self.titulo] = persona
            self.tail = persona
            current = self.head
            max_iterations = 1000  # Establecer un límite máximo de iteraciones
            iterations = 0
            while current.next[self.titulo] is not None and iterations < max_iterations:
                found = False
                for conexion in grafo.graph[persona]:
                    if conexion["Persona"] == current:
                        found = True
                if not found:
                    grafo.agregar_arista(persona, current, self.titulo)
                current = current.next[self.titulo]
                iterations += 1
            if iterations >= max_iterations:
                print("Advertencia: El bucle alcanzó el límite máximo de iteraciones.")

    def imprimirPersonas(self):
        current = self.head
        while current:
            print(f"Nombre: {current.nombre}, Rol: {current.rol}")
            current = current.next[self.titulo]


class Grafo:
    def __init__(self):
        self.graph = defaultdict(list)

    def agregar_arista(self, persona1, persona2, pelicula):

        self.graph[persona1].append({"Persona": persona2, "Pelicula": pelicula})
        self.graph[persona2].append({"Persona": persona1, "Pelicula": pelicula})

    def mostrar_grafo(self):
        for persona in self.graph:
            print(f"{persona.nombre} ->", end=" ")
            for conexion in self.graph[persona]:
                print(f"{conexion["Persona"].nombre}, ", end="")
            print()


def BFS(grafo, inicio, destino):
    visitado = [False] * (len(grafo.graph) + 1)
    padre = [None] * (len(grafo.graph) + 1)
    cola = deque()
    cola.append(inicio)
    visitado[inicio.id] = True

    while cola:
        actual = cola.popleft()
        if actual == destino:
            break
        for adyacente in grafo.graph[actual]:
            if not visitado[adyacente["Persona"].id]:
                cola.append(adyacente["Persona"])
                visitado[adyacente["Persona"].id] = True
                padre[adyacente["Persona"].id] = {"Nodo": actual, "Pelicula": adyacente["Pelicula"]}  # Almacenar el padre y la película

    if padre[destino.id] is None:
        print("No hay camino posible desde", inicio.nombre, "hasta", destino.nombre)
        return

    # Reconstruir el camino
    camino = []
    v = destino
    while v is not None:
        camino.append(v)
        # Verificar si v tiene un padre
        if padre[v.id] is None:
            break
        v = padre[v.id]["Nodo"]

    if v is None:
        print("No hay camino posible desde", inicio.nombre, "hasta", destino.nombre)
        return

    camino.reverse()

    print("El camino más corto desde", inicio.nombre, "hasta", destino.nombre, "es:")
    print()
    for i in range(len(camino) - 1):
        nodo_actual = camino[i]
        nodo_siguiente = camino[i + 1]
        for conexion in grafo.graph[nodo_actual]:
            if conexion["Persona"] == nodo_siguiente:
                pelicula = conexion["Pelicula"]
                print(f"{nodo_actual.nombre} se conecta con {nodo_siguiente.nombre} por {pelicula},")
                break
    print()


def DFS(grafo, vertice, visitado=None):
    if visitado is None:
        visitado = set()
    visitado.add(vertice.id)
    for adyacente in grafo.graph[vertice]:
        if adyacente["Persona"].id not in visitado:
            print(f"{vertice.nombre} colaboro con {adyacente["Persona"].nombre} en {adyacente["Pelicula"]}")
            DFS(grafo, adyacente["Persona"], visitado)