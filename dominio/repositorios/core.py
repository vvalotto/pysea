from abc import abstractmethod, ABCMeta

class BaseRepositorio(metaclass=ABCMeta):

    def __init__(self, persistidor, entidad):
        self._persistidor = persistidor
        self._entidad = entidad

    @property
    def persistidor(self):
        return self._persistidor

    @property
    def entidad(self):
        return self._entidad

    @abstractmethod
    def guardar(self, entidad):
        pass

    @abstractmethod
    def obtener_por_id(self, id_entidad):
        pass

    @abstractmethod
    def actualizar(self, entidad):
        pass

    @abstractmethod
    def obtener_todos(self):
        pass
