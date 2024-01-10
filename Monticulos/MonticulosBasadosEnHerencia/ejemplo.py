
from MinHeap import MinHeap
from Nodo import Nodo
from Empleado import Empleado


empleado1 = Empleado(5, 'Pepe', 'García', '123456789X', '10/01/2000')
empleado2 = Empleado(10, 'Juan', 'Sánchez', '987654321C', '10/01/2001')
empleado3 = Empleado(3, 'Maria', 'Pozas', '753951285P', '10/01/1999')



monticulo = MinHeap()

print('Esta vacio? ' + str(monticulo.is_empty()))
print('Tamaño actual: ' + str(monticulo.size()))

nodo1 = Nodo(empleado1)
nodo2 = Nodo(empleado2)
nodo3 = Nodo(empleado3)


print('Insertamos nodo ')
monticulo.push(nodo1)
print('Tamaño actual: ' + str(monticulo.size()))
print(monticulo.peek())

print('Insertamos nodo ')
monticulo.push(nodo2)
print('Tamaño actual: ' + str(monticulo.size()))
print(monticulo.peek())
print(str(monticulo))


print('Insertamos nodo ')
monticulo.push(nodo3)
print('Tamaño actual: ' + str(monticulo.size()))
print(nodo3)
print(str(monticulo))
