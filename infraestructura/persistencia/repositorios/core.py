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
            if entidad.id is None:
                self._persistidor.sesion.add(entidad)
            self._persistidor.sesion.flush()
            self._persistidor.sesion.commit()
        except Exception as ex:
            raise ex
        return

    def obtener_por_id(self, id_entidad):
        """
        :return:
        """
        try:
            print(self._entidad)
            entidad = self._persistidor.sesion.query(self._entidad).get(id_entidad)
            print(type(entidad))
            return entidad
        except Exception:
            raise Exception

    def actualizar(self, entidad):
        pass

    def obtener_todos(self):
        """
        Rescata todas las ocurrencias (filas) de la entidad
        :return:
        """
        try:
            lista_entidades = self._persistidor.sesion.query(self._entidad).all()
            return lista_entidades
        except Exception:
            raise Exception