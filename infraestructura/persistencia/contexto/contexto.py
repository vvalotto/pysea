from  abc import ABCMeta, abstractmethod


class BaseContexto(metaclass=ABCMeta):
    """
    Clase abstract que define la interfaz de la persistencia de datos
    """
    @abstractmethod
    def __init__(self, recurso):
        """
        Se crea el contexto, donde el pasa el recurso fisico donde residen los datos
        junto con esto se crea el recurso fisico
        :param recurso: definicion del recurso fisico
        :return:
        """
        self._recurso = None
        if recurso is None or recurso == "":
            raise Exception("Nombre de recurso vacio")
        self._recurso = recurso
        return

    @property
    def recurso(self):
        return self._recurso