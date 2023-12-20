
'''
Clase de ejemplo para almacenar en los nodos de nuestros montículos
'''

class Empleado: 
    def __init__(self, num_empleado, nombre, apellidos, dni, fecha_nac) -> None:
        self.num_empleado = num_empleado
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.fecha_nac = fecha_nac

    def __str__(self) -> str:
        return str('Num. Empleado: ' + self.num_empleado + ', Nombre: ' + self.nombre + 
                   ', Apellidos: ' + self.apellidos + ', DNI: ' + self.dni + 
                   ', Fecha de nacimiento ' + self.fecha_nac)
    
    '''
    def compare_to(self, empleado1) -> int:
        if (self.num_empleado > empleado1.num_empleado):
            return 1
        elif (self.num_empleado < empleado1.num_empleado):
            return -1
        else:
            return 0
    '''

    def __eq__(self, empleado1: Empleado) -> bool:
        if ( self.nombre == empleado1.nombre and 
             self.apellidos == empleado1.apellidos and
             self.dni == empleado1.dni and
             self.fecha_nac == empleado1.fecha_nac ):
            return True
        else:
            return False
    
    # less than ==> lt
    def __lt__(self, empleado1: Empleado) -> bool:
        return( self.num_empleado < empleado1.num_empleado)
    
    # greater than
    def __gt__(self, empleado1: Empleado) -> bool:
        return( self.num_empleado > empleado1.num_empleado)

    # less or equal
    def __le__(self, empleado1: Empleado) -> bool:
        return( self.num_empleado <= empleado1.num_empleado)
    
    # greater or equal
    def __ge__(self, empleado1: Empleado) -> bool:
        return( self.num_empleado >= empleado1.num_empleado)
    
    # not equal
    def __ne__(self, empleado1: Empleado) -> bool:
        return not( self.__eq__(self, empleado1) )
