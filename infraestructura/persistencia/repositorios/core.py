"""
Definición del modelo físico en la base de datos
"""
from sqlalchemy.orm import sessionmaker
from dominio.repositorios.core import BaseRepositorio


class RepositorioDB(BaseRepositorio):
    """
    Definicion del Repositorio generico
    """

    def guardar(self, entidad):
        """
        Persiste la entidad senial
        :return:
        """
        try:
            Sesion = sessionmaker(bind=self._persistidor.recurso)
            sesion = Sesion()
            if entidad.id is None:
                sesion.add(entidad)
            sesion.flush()
            sesion.commit()
        except Exception as ex:
            raise ex
        return

    def obtener_por_id(self, id_entidad):
        """
        :return:
        """
        try:
            Sesion = sessionmaker(bind=self._persistidor.recurso)
            sesion = Sesion()
            print(self._entidad)
            entidad = sesion.query(self._entidad).get(id_entidad)
            print(type(entidad))
            sesion.flush()
            sesion.commit()
            return entidad
        except Exception:
            raise Exception

    def actualizar(self, entidad):
        pass