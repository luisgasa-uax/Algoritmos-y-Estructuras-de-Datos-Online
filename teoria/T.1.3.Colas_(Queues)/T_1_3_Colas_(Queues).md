# T.1.3. Colas (Queues)

Una cola es una estructura de datos que sigue el principio **FIFO** (First In, First Out), lo que significa que el primer elemento que se añade a la cola es el primero en ser retirado.

Imagina una fila de personas esperando en la taquilla de un cine: la primera persona que llega es la primera en ser atendida y así sucesivamente. Las colas en programación siguen el mismo principio.

![cola 2.png](./T_1_3_Colas_(Queues)/cola_2.png)

## 1.4.1. **Operaciones básicas**

1. **Encolar (Enqueue)**: Agregar un elemento al final de la cola.
2. **Desencolar (Dequeue)**: Eliminar y retornar el primer elemento de la cola. Si la cola está vacía, esta operación generalmente arroja un error o se maneja de una manera específica.
3. **Frente (Front/Peek)**: Consultar el primer elemento de la cola sin eliminarlo.
4. **Tamaño (Size)**: Determinar la cantidad de elementos en la cola.
5. **Está vacía (isEmpty)**: Verificar si la cola está vacía.

## 1.4.2. **Usos comunes de las colas**

- **Gestión de tareas en sistemas**: Cuando las tareas se añaden a una lista de espera y se procesan en orden de llegada.
- **Simulaciones**: Simular escenarios donde el orden de llegada y servicio importa, como en la simulación de una cola de supermercado.
- **Navegación en anchura en grafos**: En algoritmos como el BFS (Búsqueda en Amplitud).

## 1.4.3. **Ventajas y desventajas**

| Ventajas | Desventajas |
| --- | --- |
| Orden predecible debido al comportamiento FIFO. | Puede ser ineficiente si se implementa con arrays (al eliminar el primer elemento). |
| Gestión eficiente de recursos en sistemas y simulaciones. | Puede requerir más memoria si se implementa con listas enlazadas. |
| Facilita la multitarea en sistemas operativos. | La búsqueda puede ser lenta, ya que se debe recorrer desde el inicio. |
| Las operaciones de encolar y desencolar son generalmente rápidas. | Si no se maneja correctamente, puede causar desbordamiento de cola. |
| Es una herramienta esencial para ciertos algoritmos y problemas, como el BFS. | Es posible que no sea la estructura óptima para todos los escenarios. |

## 1.4.4. **Implementación**

Las colas pueden implementarse **utilizando arrays/listas o listas enlazadas**. A menudo, las estructuras de datos estándar en la mayoría de los lenguajes de programación (como Python) ofrecen implementaciones eficientes de colas para evitar operaciones costosas.

Ten en cuenta que, debido a la propia naturaleza de las colas (FIFO), **necesitamos tener controlados los dos extremos de esta.** Es decir, necesitamos conocer el frente y el final de la cola. Lo puedes ver en el método constructor de la cola.

```python
class Nodo: 
    """Implementa la clase Nodo para una estructura de datos tipo Cola.

    Attributes: 
        valor (Object): El valor almacenado en el nodo.
        siguiente (Nodo, optional): El siguiente nodo en la Cola, inicialmente None.
    """
    def __init__(self, valor) -> None:
        """Inicializa un Nodo con un valor dado.

        Args:
            valor (Object): El valor que se almacenará en el nodo.
        """
        self.valor = valor
        self.siguiente = None

class Cola:
    """Implementa una estructura de datos de tipo Cola.

    Attributes: 
        frente (Nodo, optional): El primer nodo de la Cola, inicialmente None.
        final (Nodo, optional): El último nodo de la Cola, inicialmente None.
        tamanio (int): El número de nodos en la Cola, inicialmente 0.
    """
    def __init__(self) -> None:
        """Constructor de la clase Cola que inicializa una Cola vacía."""
        self.frente = None
        self.final = None
        self.tamanio = 0
```

### 1.4.4.1. Encolar (Enqueue):

Añade un elemento al final de la cola. Si la cola está vacía, el nuevo nodo se convierte tanto en el frente como en el final. Si no está vacía, se ajusta el puntero `siguiente` del último nodo para que apunte al nuevo nodo y luego se mueve el puntero `final` para que señale al nuevo nodo.

![cola_-_queue.png](./T_1_3_Colas_(Queues)//cola_-_queue.png)

```python
def enqueue(self, valor: object):
		"""Añade un nuevo elemento al final de la Cola.
		
		Args:
		    valor (object): El valor a encolar.
		"""
		nodo = Nodo(valor=valor)
		if self.is_empty():
		    self.frente = nodo
		    self.final = nodo
		else: 
		    self.final.siguiente = nodo  
		    self.final = nodo
		self.tamanio += 1
```

### 1.4.4.2. Desencolar (Dequeue):

Elimina y devuelve el primer elemento de la cola (el frente). Si la cola se queda vacía después de la operación, se asegura de que tanto el frente como el final apunten a `None`.

![cola_-_dequeue.png](./T_1_3_Colas_(Queues)//cola_-_dequeue.png)

```python
def dequeue(self):
		"""Retira y devuelve el elemento del frente de la Cola.
		
		Returns:
		    object: El valor del elemento retirado o None si la cola está vacía.
		"""
		if self.is_empty():
		    print("ADVERTENCIA: la cola está vacía")
		    return None
		valor_salida = self.frente.valor
		self.frente = self.frente.siguiente
		if self.frente == None:     # no hay elementos en la cola
		    self.final = None
		self.tamanio -= 1
		return valor_salida
```

### 1.4.4.3. Frente (Front/Peek):

Devuelve el primer elemento de la cola (el frente) sin eliminarlo. Si la cola está vacía, se levanta un error.

```python
def peek(self):
		"""Devuelve el valor del elemento que está en el frente de la Cola sin retirarlo.
		
		Returns:
		    object: El valor del frente de la Cola o None si la cola está vacía.
		"""
		if self.is_empty():
		    print("ADVERTENCIA: la cola está vacía")
		    return None
		valor_salida = self.frente.valor
		return valor_salida
```

### 1.4.4.5. Está vacía (isEmpty):

Elimina y devuelve el primer elemento de la cola (el frente). Si la cola se queda vacía después de la operación, se asegura de que tanto el frente como el final apunten a `None`.

```python
def is_empty(self) -> bool:
		"""Comprueba si la Cola está vacía.
		
		Returns:
		    bool: True si la Cola está vacía, False en caso contrario.
		"""
		if self.tamanio == 0: 
		    return True
		return False
```

### 1.4.4.6. Tamaño (size):

Devuelve la cantidad (`int`) de elementos almacenados en la Cola.

```python
def size(self) -> int:
		"""Devuelve la cantidad de elementos almacenados en la Cola.
		
		Returns:
		    int: El tamaño de la Cola.
		"""
		return self.tamanio
```

---


## 1.4.5. Ejercicio de consolidación

**Ejercicio: Simulación de un Centro de Atención al Cliente**

**Contexto**: Imagina que estás a cargo del sistema de un centro de atención al cliente. Las personas llegan y se ponen en cola para ser atendidas. Cada persona es atendida en un tiempo aleatorio entre 1 y 5 minutos. Tu tarea es simular el proceso de atención y calcular los tiempos de espera promedio de los clientes.

**Requerimientos**:

1. Crea una clase `Cliente` que tenga:
    - Un identificador único.
    - El tiempo que llegó.
    - El tiempo que fue atendido.
2. Utiliza una estructura de cola para gestionar los clientes.
3. Simula la llegada de clientes cada 1 a 3 minutos. 

```
import time
time.sleep(3) # segundos
```

1. Cada vez que un cliente es atendido:
    - Desencólate al siguiente cliente.
    - Registra el tiempo actual como el tiempo de atención del cliente.
    - Calcula el tiempo que el cliente esperó.
2. La simulación debe durar 60 minutos. Al final, muestra el tiempo promedio de espera de todos los clientes.

**Consejos**:

- Puedes usar la biblioteca `random` de Python para generar tiempos aleatorios de llegada y atención.
- Controla la simulación con un bucle que represente cada minuto.

Este ejercicio te permitirá practicar no solo las operaciones básicas de las colas, sino también la lógica y la simulación de un escenario del mundo real.