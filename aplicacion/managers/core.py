from abc import ABCMeta, abstractmethod

class BaseManager(metaclass=ABCMeta):

    @abstractmethod
    def guardar(self):
        pass

    @abstractmethod
    def obtener_por_id(self, id):
        pass

    @abstractmethod
    def habilitar(self):
        pass

    @abstractmethod
    def deshabilitar(self):
        pass


class ManagerEntidad(BaseManager):

    def __init__(self, repositorio, entidad):
        self._entidad = entidad
        self._repositorio = repositorio

    def guardar(self):
        try:
            if self._entidad == None:
                raise ('Nada para guadar')
            if self._entidad.id == None:
                self._repositorio.guardar(self._entidad)
            else:
                self._repositorio.actualizar(self._entidad)
        except Exception as ex:
            raise(ex.args)


    def obtener_por_id(self, id):
        try:
            entidad = self._repositorio.obtener_por_id(id)
            return entidad
        except Exception as ex:
            raise(ex)


    def habilitar(self):
        self._entidad.habilitar = 1
        try:
            self._repositorio.actualizar(self._entidad)
        except Exception as ex:
            raise(ex.args)


    def deshabilitar(self):
        self._entidad.habilitar = 0
        try:
            self._repositorio.actualizar(self._entidad)
        except Exception as ex:
            raise(ex.args)