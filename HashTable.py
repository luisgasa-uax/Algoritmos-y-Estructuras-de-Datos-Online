# HashTable. Algoritmos y Estructuras de Datos. UAX. Online

class HashTable:
    def __init__(self, capacity=100, max_amount_collisions=5, auto_resize_multiplier=1.01 ) -> None:
        self.capacity = capacity  # tamaño de la tabla de hash
        self.table = [{} for _ in range(capacity)]  # creamos un dicionario en cada uno de los registros de la tabla
        self.size = 0
        self.MAX_AMOUNT_COLLISIONS = max_amount_collisions
        self.AUTO_RESIZE_MULTIPLIER = auto_resize_multiplier

    '''
        Calcula el código hash para la posición del registro en la tabla 
    '''
    def __hash__(self, key, capacity = None) -> int:
        num_hash = 0
        #'PepitoPiscinas43'  #=> 16 caracteres
        for i in range(0, len(key)):
            num_hash += ord(key[i])
            print(f'ord: {ord(key[i])} num_hash: {num_hash}')
        
        if capacity == None:
            capacity = self.capacity
        position = num_hash % capacity  # la posición de la tabla en la que debemos colocar el nodo
        return position
    
    '''
        Genera una clave para el diccionario interno de cada registro
    '''
    def _internal_dict_key(self, key) -> str:
        hash = self.__hash__(key)
        return key + str(hash)

    '''
        Inserta el nodo en la tabla
    '''
    def put(self, key, node) -> None:
        hash = self.__hash__(key)
        internal_key = self._internal_dict_key(key)
        self.table[hash][internal_key] = node  # insertamos el nodo en el diccionario interno del registro de la tabla
        self.size += 1

        # comprobamos las colisiones
        if len(self.table[hash]) > self.MAX_AMOUNT_COLLISIONS:
            self.rehashing(self.AUTO_RESIZE_MULTIPLIER)

    
    '''
    Busca un elemento en la estructura y devuelve el elemento o si no lo encuentra devuelve None
    '''
    def search(self, key) -> any:
        hash = self.__hash__(key)
        if len(self.table[hash]) == 0:
            return None
        else:
            internal_key = self._internal_dict_key(key)
            node = self.table[hash][internal_key]
            return node
    
    '''
    Elimina el nodo correspondiente a la clave

    Return:
        - 0 si no lo encuentra
        - 1 si lo encuentra
    '''
    def remove(self, key) -> int:
        node = self.search(key)
        if node is None:
            return 0
        del node        # forzamos la liberación de memoria del nodo eliminado
        self.size -= 1  # disminuimos el valor de size o cantidad de nodos almacenados
        return 1

    '''
    Devuelve la cantidad de elementos almacenados

    '''
    def __sizeof__(self) -> int:
        return self.size

    
    '''
    Redimensiona la tabla hash

    multiplier: factor de multiplicación de la capacidad de la tabla
    Return:
        None
    '''
    def rehashing(self, multiplier) -> None: 
        new_capacity = self.capacity * multiplier
        new_table = [{} for _ in range(new_capacity)] 

        for internal_dict in self.table:
            for key, value in internal_dict.items:
                new_position = self.__hash__(key, new_capacity)
                new_table[new_position].update({key:value})
        
        self.capacity = new_capacity
        self.table = new_table
