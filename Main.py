from Clases import Grafo, BFS, DFS, Nodo, Pelicula
import csv

# LECTURA DE CSV
peliculas = []
with open(file='imdb_top_1000.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    size = 0
    for row in reader:
        peliculas.append(row)

# CREACION DEL GRAFO
Grafo = Grafo()
id = 1
personas_existentes = {}
nodos_personas = []
for x in peliculas:
    pelicula_actual = Pelicula(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[14], x[15])

    for i in range(5):

        if i == 0:
            rol = "Director"
        else:
            rol = "Actor"

        persona_nombre = x[9 + i]

        if persona_nombre not in personas_existentes:
            persona = Nodo(id, persona_nombre, rol)
            nodos_personas.append(persona)
            personas_existentes[persona_nombre] = persona
            id += 1
        else:
            persona = personas_existentes[persona_nombre]

        pelicula_actual.agregarPersona(persona, Grafo)

# CONEXIONES DE CADA PERSONA *GRAFO*
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print()
print("Representacion grafica de la lista del grafo")
print()
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
Grafo.mostrar_grafo()

# APLICACION DE BFS
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print()
print("Recorrido desde Persona1 hasta Persona2, aplicacion de BFS")
print()
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
Persona1 = None
Persona2 = None
for nodo in nodos_personas:
    if nodo.nombre == "Mahesh Manjrekar":
        Persona1 = nodo
    if nodo.nombre == "Mario Casas":
        Persona2 = nodo
if Persona1 and Persona2:
    BFS(Grafo, Persona1, Persona2)
else:
    print("No se encontraron las personas especificadas.")

# APLICACION DE DFS
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print()
print("Colaboraciones posibles de una Persona, aplicacion de DFS")
print()
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
Persona3 = None
for nodo in nodos_personas:
    if nodo.nombre == "Robert Duvall":
        Persona3 = nodo
if Persona3:
    DFS(Grafo, Persona3)
