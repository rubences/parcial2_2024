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

Ejercicio 4: Solución Numérica de Ecuaciones en la Antigua Grecia
Implemente y compare tres métodos iterativos (bisección, secante y Newton-Raphson) para encontrar la raíz de la ecuación :

Determine la cantidad de iteraciones necesarias para que cada método converja.
Compare la precisión de cada método en términos del número de decimales correctos.


Luke Skywalker se encuentra en una misión para recuperar su sable de luz perdido. Durante su travesía, encuentra una serie de cajas que contienen diferentes objetos de valor (que podrían ser herramientas o elementos útiles para su misión), pero su mochila tiene una capacidad limitada para llevar solo ciertos elementos.

Cada objeto tiene un peso y un valor determinado. El sable de luz de Luke tiene un valor muy alto, pero también un peso considerable. Ayuda a Luke a decidir qué objetos debe llevar en su mochila para maximizar el valor de los objetos que puede cargar sin exceder la capacidad de la mochila.

Datos:
El sable de luz de Luke tiene un valor de 1000 (puntos de poder) y un peso de 10 (kilogramos).
Existen varios objetos con diferentes valores y pesos. Luke puede llevar cualquiera de estos objetos siempre que no sobrepasen el límite de peso de la mochila, que es de 50 kilogramos.
Objetos disponibles:
Blaster: valor = 500, peso = 15 kg
Raciones de comida: valor = 200, peso = 5 kg
Cloak Jedi: valor = 400, peso = 8 kg
Mapa Estelar: valor = 300, peso = 4 kg
Comunicador Galactic: valor = 350, peso = 3 kg
Sable de luz de Luke: valor = 1000, peso = 10 kg
Objetivo:
Implementa un algoritmo en Python que resuelva el problema de la mochila para ayudar a Luke Skywalker a seleccionar los objetos que debe llevar en su mochila. El objetivo es maximizar el valor total de los objetos sin exceder el peso máximo de 50 kg.


Enunciado del ejercicio:

Luke Skywalker se encuentra atrapado en una antigua cueva en Tatooine. Mientras explora la cueva, encuentra varias puertas y caminos que lo conducen a diferentes habitaciones llenas de objetos valiosos, pero algunos caminos están bloqueados por trampas. Además, el sable de luz de Luke se encuentra en una de las habitaciones, pero el camino está lleno de obstáculos.

Cada habitación tiene un valor (indicado por la cantidad de puntos de poder que el sable podría ganar si Luke lo encuentra) y un costo en puntos de vida (que es el daño que Luke recibiría al atravesar las trampas). Luke tiene una cantidad limitada de puntos de vida, por lo que debe elegir cuidadosamente las habitaciones a las que se adentrará para maximizar el valor total de los objetos que recoja sin perder todos sus puntos de vida.

Datos:
Luke tiene 100 puntos de vida al comenzar.
Las habitaciones están organizadas en un mapa de varias salas. En cada sala, hay una serie de caminos que conducen a otras salas (algunas son trampas, otras no).
El objetivo es encontrar el sable de luz, que tiene un valor de 1000 puntos de poder. Si Luke se acerca a esta sala, pero no puede completar el recorrido sin perder demasiados puntos de vida, debe volver atrás y buscar otro camino.
Estructura:
Las salas están representadas como un grafo, donde cada nodo es una habitación y las aristas representan caminos entre las habitaciones.
Cada habitación tiene un valor y un costo en puntos de vida:
Sala 1 (Inicio): valor = 0, costo = 0
Sala 2: valor = 500, costo = 10
Sala 3: valor = 300, costo = 5
Sala 4 (Sable de luz): valor = 1000, costo = 50
Sala 5: valor = 200, costo = 15
Sala 6: valor = 400, costo = 20
Las habitaciones conectadas entre sí tienen caminos que pueden ser explorados (algunas habitaciones pueden llevar a trampas, por lo que si los puntos de vida de Luke llegan a 0, el recorrido no es válido).
Requerimientos:
Implementa un algoritmo de backtracking para ayudar a Luke a encontrar el camino óptimo que lo lleve a la sala que contiene el sable de luz sin perder todos sus puntos de vida.
El algoritmo debe explorar todos los posibles caminos, evaluando cuál es el camino con el mayor valor acumulado sin exceder el límite de vida de 100 puntos.
Devuelve el camino que Luke debe seguir (las habitaciones) y el valor total de los objetos que recoge en el camino.
Restricciones:
Luke solo puede tomar decisiones sobre caminos si no exceden los 100 puntos de vida.
Si Luke no puede llegar a la sala del sable de luz, debe retornar el máximo valor posible sin perder demasiados puntos de vida.
