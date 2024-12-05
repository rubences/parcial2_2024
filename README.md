# parcial2_2024

Pregunta 1 (2 puntos) - Árbol de Decisiones para el Consejo de Elrond
El Consejo de Elrond se enfrenta a un dilema crítico: enviar representantes de la Tierra Media en diferentes misiones para enfrentar la amenaza de Sauron. Las misiones varían en su complejidad y peligrosidad, desde espionaje hasta combate. Elrond, líder de los Elfos, desea un método eficiente para decidir qué miembro enviar a cada misión.

Requerimientos
Diseña un árbol de decisiones para ayudar a Elrond. La raíz podría ser el tipo de misión, seguido de nodos con atributos como "experiencia en combate", "habilidades mágicas", etc., hasta llegar a las hojas, que serán personajes.
Implementa una función decide_member(mission_type: str) -> str.
Datos para el árbol
No se proporcionan tablas para esta sección, debes realizarlos.



Pregunta 2 (2 puntos) - Sistema de Prioridades para Gandalf
Gandalf el Gris, uno de los Istari enviados a la Tierra Media, recibe constantemente peticiones de ayuda de diversos reinos y personas. Necesita un método para ordenar y priorizar estas peticiones según su urgencia e importancia.

Requerimientos
Diseña una estructura de datos de cola de prioridad con tres niveles: Alto, Medio, Bajo.
Implementa una pila de "Pergaminos" donde Gandalf pueda almacenar las peticiones más urgentes.

Pregunta 3 (2 puntos) - Red Social de Hobbits
Los habitantes de la Comarca están interesados en una red social local, "HobbitBook", que les permita mantenerse en contacto y compartir noticias. Aunque no disponen de internet, imaginemos que pudiéramos aplicar estructuras de datos modernas para resolver su problema.

Requerimientos
Crea un grafo para representar las conexiones sociales entre los Hobbits.
Implementa algoritmos para encontrar el árbol de expansión máximo.
Datos para el grafo
Nodo

Vecinos

Frodo

Sam, Pippin, Merry

Sam

Frodo, Rosie

Merry

Pippin, Frodo

Pippin

Merry, Frodo



Pregunta 4 (2 puntos) - Optimización del Viaje de Aragorn
Aragorn debe recorrer varios reinos para reunir aliados contra Sauron. Dado que el tiempo es esencial, necesita minimizar el tiempo de viaje entre cada reino.

Requerimientos
Implementa un algoritmo que encuentre el camino más corto entre los reinos que necesita visitar.
El recorrido debe empezar y terminar en Rivendel.
Datos para el grafo
Origen

Destino

Tiempo de Viaje (días)

Rivendel

Gondor

7

Gondor

Rohan

5

Rohan

Mordor

10

Mordor

Rivendel

15

Gondor

Mordor

2







Pregunta 5 (2 puntos) - Estrategia de Batalla para la Última Alianza
La Última Alianza de Hombres y Elfos debe enfrentarse al ejército de Sauron. El ejército enemigo está compuesto por diferentes tipos de unidades, como orcos, trolls y Nazgûl. La Alianza necesita asignar sus unidades de la manera más eficaz posible para contrarrestar a las fuerzas enemigas.

Requerimientos
Diseña un árbol binario de búsqueda para organizar las unidades del ejército de la Alianza por "poder" y "tipo de unidad".
Implementa una función find_counter_unit(enemy_unit: str) -> str que tome como entrada el tipo de unidad enemiga y devuelva el tipo de unidad de la Alianza más adecuado para enfrentarla.


Pregunta 6 (2 puntos) - Economía de Mercado en la Tierra Media
Después de la derrota de Sauron, la economía de la Tierra Media está en pleno auge. Las diferentes ciudades y reinos desean intercambiar bienes de manera eficiente. Supongamos que cada ciudad tiene un producto estrella, y desea saber cuáles son los productos más populares en otros lugares.

Requerimientos
Implementa una tabla hash para almacenar el "producto estrella" de cada ciudad.
Desarrolla un algoritmo que permita a una ciudad encontrar rápidamente el producto estrella de otra ciudad dada su nombre.


Pregunta 7 (2 puntos) - Mensajería Rápida entre Reinos
La comunicación rápida entre los reinos es crucial, especialmente en tiempos de guerra. Imagina un sistema de "correos" que use cuervos para entregar mensajes. Cada reino tiene una cierta cantidad de cuervos y necesita minimizar el tiempo total de entrega.

Requerimientos
Diseña un grafo ponderado que represente el tiempo que tardan los cuervos en viajar entre los reinos.
Implementa el algoritmo de Dijkstra para encontrar el camino más rápido para enviar un mensaje de un reino a otro.
Datos para el grafo
Origen

Destino

Tiempo de Vuelo (horas)

Gondor

Rohan

3

Rohan

Isengard

2

Isengard

Rivendel

5

Rivendel

Mirkwood

4

Pregunta 8 (2 puntos) - Reconstrucción de la Biblioteca de Minas Tirith
Después de la guerra, la biblioteca de Minas Tirith necesita ser reorganizada. Hay manuscritos y tomos sobre historia, magia, y ciencia que necesitan ser ordenados de manera lógica.

Requerimientos
Implementa una estructura de árbol B para almacenar y recuperar rápidamente libros por diferentes categorías.
Implementa una función search_book(category: str, title: str) -> str que permita encontrar un libro dado su título y categoría.
