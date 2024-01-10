class Empleado:
    '''
    Clase Empleado para representar la información de un empleado.

    Atributos:
    num_empleado (int): Número identificador del empleado.
    nombre (str): Nombre del empleado.
    apellidos (str): Apellidos del empleado.
    dni (str): Documento Nacional de Identidad del empleado.
    fecha_nac (str): Fecha de nacimiento del empleado.
    '''

    def __init__(self, num_empleado, nombre, apellidos, dni, fecha_nac):
        '''
        Inicializa un nuevo empleado con sus datos personales.

        :param num_empleado: Número identificador del empleado.
        :param nombre: Nombre del empleado.
        :param apellidos: Apellidos del empleado.
        :param dni: DNI del empleado.
        :param fecha_nac: Fecha de nacimiento del empleado.
        '''
        self.num_empleado = num_empleado
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.fecha_nac = fecha_nac

    def compare_to(self, empleado1):
        '''
        Compara este empleado con otro según su número identificador.

        :param empleado1: Objeto Empleado a comparar.
        :return: 1 si este empleado tiene un número mayor, -1 si menor, 0 si son iguales.
        '''
        if self.num_empleado > empleado1.num_empleado:
            return 1
        elif self.num_empleado < empleado1.num_empleado:
            return -1
        else:
            return 0

    def equals(self, empleado1) -> bool:
        '''
        Determina si dos empleados son iguales basándose en criterios definidos.
        Actualmente, este método no implementa una lógica específica.

        :param empleado1: Empleado con el cual comparar.
        :return: True si se consideran iguales, False en caso contrario.
        '''
        resultado = True
        # Aquí irían los criterios de igualdad
        return resultado
    
    def __str__(self):
        '''
        Representación en cadena del empleado, mostrando su número identificador.

        :return: Representación en cadena del número identificador del empleado.
        '''
        return str(self.num_empleado ) + ' ' + self.nombre + ' ' +  self.apellidos + ' ' +  self.dni + ' ' +  self.fecha_nac

    def __lt__(self, other):
        '''
        Sobrecarga del operador < para comparar empleados según su número identificador.

        :param other: Otro objeto Empleado para la comparación.
        :return: True si este empleado tiene un número identificador menor que 'other'.
        '''
        return self.num_empleado < other.num_empleado

    def __le__(self, other):
        '''
        Sobrecarga del operador <= para comparar empleados según su número identificador.

        :param other: Otro objeto Empleado para la comparación.
        :return: True si este empleado tiene un número identificador menor o igual que 'other'.
        '''
        return self.num_empleado <= other.num_empleado

    def __gt__(self, other):
        '''
        Sobrecarga del operador > para comparar empleados según su número identificador.

        :param other: Otro objeto Empleado para la comparación.
        :return: True si este empleado tiene un número identificador mayor que 'other'.
        '''
        return self.num_empleado > other.num_empleado

    # Comentado ya que parece haber un error en la implementación
    def __ge__(self, other):
        '''
        Sobrecarga del operador >= para comparar empleados según su número identificador.

        :param other: Otro objeto Empleado para la comparación.
        :return: True si este empleado tiene un número identificador mayor o igual que 'other'.
        '''
        return self.num_empleado >= other.num_empleado

    def __eq__(self, other):
        '''
        Sobrecarga del operador == para comparar empleados según su número identificador.

        :param other: Otro objeto Empleado para la comparación.
        :return: True si este empleado tiene un número identificador igual a 'other'.
        '''
        return self.num_empleado == other.num_empleado

    def __ne__(self, other):
        '''
        Sobrecarga del operador != para comparar empleados según su número identificador.

        :param other: Otro objeto Empleado para la comparación.
        :return: True si este empleado tiene un número identificador distinto de 'other'.
        '''
        return not(self.__eq__(other))
