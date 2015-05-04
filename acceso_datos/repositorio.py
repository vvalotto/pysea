from sqlalchemy.orm import  sessionmaker

from dominio.repositorios.core import BaseRepositorio


class DBRepositorio(BaseRepositorio):
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
            if entidad.id == None:
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

class DBRepositorioCarrera(DBRepositorio):

    def actualizar(self, carrera):
        try:
            Sesion = sessionmaker(bind=self._persistidor.recurso)
            sesion = Sesion()
            carrera_ant = sesion.query(self._entidad).get(carrera.id)
            print(carrera_ant)
            carrera_ant.nombre = carrera.nombre
            carrera_ant.institucion = carrera.institucion
            carrera_ant.plan = carrera.plan
            carrera_ant.habilitado = carrera.habilitado
            print(carrera_ant)
            sesion.commit()
        except Exception as ex:
            raise(ex.args)


class DBRepositorioMateria(DBRepositorio):

    def actualizar(self, materia):
        try:
            Sesion = sessionmaker(bind=self._persistidor.recurso)
            sesion = Sesion()
            materia_ant = sesion.query(self._entidad).get(materia.id)
            print(materia_ant)
            materia_ant.nombre = materia.nombre
            materia_ant.id_carrera = materia.id_carrera
            print(materia_ant)
            sesion.commit()
        except Exception as ex:
            raise(ex.args)