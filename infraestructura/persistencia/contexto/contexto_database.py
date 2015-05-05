"""
Definición del mecanismo de persistencia (Tecnología para almacenar los datos)
"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import mapper, relationship, relation

from dominio.entidades.administracion import *
from infraestructura.persistencia.modelo.database import *
from infraestructura.persistencia.contexto.contexto import *


class ContextoDB(BaseContexto):

    def __init__(self, recurso):
        super().__init__(recurso)
        self._recurso = create_engine(recurso)
        self._recurso.echo = False
        self._db = None

    def inicializar_tablas(self):
        """
        Define los objetos tabla
        :return:
        """
        metadata = MetaData(self._recurso)
        self._db = Database(metadata)

    def inicializar_mapeos(self):
        """
        Define el mapeo entre las entidades del dominio y las tablas para persistirlas
        :return:
        """
        mapper(Carrera, self._db.carrera, properties=dict(materias=relation(Materia)))
        mapper(Materia, self._db.materia)
        mapper(Rol, self._db.rol, properties={'usuarios':
                                                  relationship(Usuario, secondary=self._db.rol_usuario,
                                                               backref='roles')
                                              })
        mapper(Usuario, self._db.usuario)
        mapper(UsuarioRol, self._db.rol_usuario)