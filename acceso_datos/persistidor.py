"""
Definición del mecanismo de persistencia (Tecnología para almacenar los datos)
"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import mapper

from dominio.entidades.administracion import *
from infraestructura.persistencia.repositorios.core import *


class Persistidor(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, recurso):
        """
        Se crea el persistor, donde el nombre es el recurso fisico donde residen los datos
        junto con esto se crea el recurso fisico con el nombre
        :param recurso:
        :return:
        """
        self._recurso = None
        if recurso is None or recurso == "":
            raise Exception("Nombre de recurso vacio")
        return

    @property
    def recurso(self):
        return self._recurso


class DBPersistidor(Persistidor):

    def __init__(self, recurso):
        super().__init__(recurso)
        self._recurso = create_engine('sqlite:///acceso_datos/evaluaciones')
        self._recurso.echo = False

    def inicializar_tablas(self):
        '''
        Define los objetos tabla
        :return:
        '''
        metadata = MetaData(self._recurso)
        self._db = Database(metadata)

    def inicializar_mapeos(self):
        mapper(Carrera, self._db.carrera, properties=dict(materias=relation(Materia)))
        mapper(Materia, self._db.materia)