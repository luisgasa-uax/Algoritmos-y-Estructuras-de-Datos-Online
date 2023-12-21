# 02.	BubbleSort: Optimización de un Sistema de Gestión de Inventario

## Contexto
En una librería, se está implementando un nuevo sistema de gestión de inventario. Para asegurar que los libros más vendidos estén siempre al frente, se necesita una forma eficiente de ordenar el inventario basándose en las ventas. Aquí es donde entra en juego el algoritmo de la burbuja, un método simple pero efectivo para ordenar datos.

## Requerimientos
Desarrollar un programa en Python que utilice el algoritmo de la burbuja para ordenar una lista de libros basándose en el número de ventas.

##Instrucciones
- Implementa el algoritmo de la burbuja para ordenar una lista de tuplas, donde cada tupla contiene el nombre del libro y el número de ventas.
- Asegúrate de que el algoritmo ordene los libros de manera que los más vendidos queden al principio de la lista.

## Preguntas Adicionales
- Análisis de Complejidad Temporal:
    - Evalúa y explica la complejidad temporal del algoritmo de la burbuja en los casos peor, mejor y promedio. 
- Análisis de Complejidad Espacial:
    - Analiza la complejidad espacial del algoritmo en los casos peor, mejor y promedio.

## Datos de Muestra
### Lista de entrada: 
`[("Don Quijote", 120), ("Cien Años de Soledad", 150), ("El Principito", 200), ("1984", 90)]`

### Salida Esperada
Lista ordenada: 
`[("El Principito", 200), ("Cien Años de Soledad", 150), ("Don Quijote", 120), ("1984", 90)]`

---

> **Consejo**
> Recuerda que el algoritmo de la burbuja compara pares de elementos adyacentes y los intercambia si están en el orden incorrecto. Este proceso se repite hasta que no se necesiten más intercambios, lo cual indica que la lista está ordenada. Visualiza cómo cada "burbuja" (elemento) se mueve a través de la lista para entender mejor el proceso.
