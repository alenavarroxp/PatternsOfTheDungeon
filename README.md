# Diseño de Software
## Información del proyecto
- **Autor:** Alejandro Navarro de la Cruz
- **Version:** Python 3.11
---
## Diagrama de Diseño realizado con StarUML <br/>

<img src="https://github.com/alenavarroxp/laberintoPython/blob/main/DesignDiagram/DiagramaDise%C3%B1o.jpg"/>

## 17 Patrones implementados <br/>
| Patrón de Diseño | Descripción |
|------------------|-------------|
| Factory Method   | Patrón que define una interface para crear un objeto, pero deja que las subclases decidan qué clase instanciar |
| Decorator        | Patrón que permite agregar funcionalidad a un objeto existente dinámicamente, sin afectar a otros objetos de la misma clase. |
| Strategy         | Patrón que define una familia de algoritmos, encapsula cada uno de ellos y los hace intercambiables. |
| Composite        | Patrón que permite construir objetos complejos a partir de objetos más simples, formando una estructura en árbol. |
| Iterator         | Patrón que permite recorrer los elementos de una colección de manera secuencial sin exponer su representación interna. |
| Template Method  | Patrón que define el esqueleto de un algoritmo en una operación, dejando que las subclases definan algunos de los pasos. |
| Abstract Factory | Patrón que proporciona una interface para crear familias de objetos relacionados o dependientes sin especificar sus clases concretas. |
| Builder          | Patrón que separa construcción y representación de un objeto complejo para permitir diferentes construcciones con el mismo proceso.|
| Singleton        | Patrón que asegura que una clase sólo tiene una instancia y proporciona un punto de acceso a la instancia. 
| Proxy            | Patrón que proporciona un sustituto o referencia a otro objeto para controlar el acceso a ese objeto. |
| Prototype        | Patrón que especifica el tipo de objetos a crear utilizando una instancia prototípica, y los crea copiando este prototipo. |
| Mediator         | Patrón que define un objeto que encapsula la interacción entre un conjunto de objetos. Promueve un acoplamiento débil al evitar que los objetos tengan referencia al resto de objetos explícita. |
| State            | Patrón que permite a un objeto alterar su comportamiento cuando cambia su estado interno. |
| Bridge           | Patrón que desacopla una abstracción de su implementación de modo que las dos puedan variar de forma independiente. |
| Visitor          | Patrón que representa una operación a realizar en los elementos de un objeto compuesto y nos permite definir una nueva operación sin modificar las clases de los objetos sobre los que se aplica. |
| Flyweight        | Patrón que utiliza compartir para soportar de manera eficiente un gran número de objetos pequeños. (ADAPTACIÓN) |
| Command          | Patrón que encapsula una petición como un objeto, permitiendo parametrizar a los clientes con diferentes peticiones y soportar operaciones deshacer. |

## Dependencias<br/>
**PYGAME:** pip install pygame <br/>
**COLORAMA:** pip install colorama <br/>


## Diagrama de Secuencia de Personaje_Compra_Tienda
Este diagrama de secuencia simula el comportamiento interno que ocurre cuando un personaje entra a una tienda y compra un objeto
<img src="https://github.com/alenavarroxp/laberintoPython/blob/main/DesignDiagram/SequenceDiagram/Personaje_Compra_Objeto">



