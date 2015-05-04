from sqlalchemy.orm import sessionmaker
from infraestructura.persistencia.repositorios.core import RepositorioDB


class DBRepositorioCarrera(RepositorioDB):

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


class DBRepositorioMateria(RepositorioDB):

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