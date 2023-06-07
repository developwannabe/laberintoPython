# Diseño de Software

- Autor: Alonso Illán Martínez del Santo

- Versión: Python 3.11

- A instalar: pip install pygame

### Algoritmos implementados:
  - Factory Method
  - Decorator
  - Strategy
  - Composite
  - Iterator
  - Template Method
  - Abstract Factory
  - Singleton
  - Builder
  - Proxy
  - Bridge
  - Mediator
  - State
  - Prototype
  - Observer
  - Command
  - Visitor

### Funcionalidades añadidas:
  - El personaje tiene una bolsa con objetos que podrán ser usados. (Composite)
  - La espada tiene un material del cual estará fabricada. Esto influirá en su comportamiento al usarse. (Strategy)
  - La vista solo recalcula individualmente los objetos que cambian su estado. (Observer)
  - Implementados comandos para los objetos. (Command)
  - El personaje ahora tiene un cuerpo, donde tendrá sus armas. (Bridge)
  - Si dos bichos perezosos se encuentrar en la misma habitación, tienen una probabilidad de cambiar su modo a agresivo. (Mediator y Template Method)
  - Ahora las puertas tienen estado abierto y cerrado. (State)

### UML:

![UML Laberinto](https://github.com/developwannabe/laberintoPython/blob/main/uml/UML.svg?raw=true)

### Diagrama de secuencia para el cambio de modo de bichos perezosos:

![UML Laberinto](https://github.com/developwannabe/laberintoPython/blob/main/uml/cambiarModo.svg?raw=true)
