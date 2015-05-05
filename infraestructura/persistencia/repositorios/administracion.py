from sqlalchemy.orm import sessionmaker
from infraestructura.persistencia.repositorios.core import RepositorioDB
from dominio.entidades.administracion import *


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
            raise ex.args


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
            raise ex.args


class DBRepositorioRol(RepositorioDB):

    def actualizar(self, rol):
        try:
            Sesion = sessionmaker(bind=self._persistidor.recurso)
            sesion = Sesion()
            rol_ant = sesion.query(self._entidad).get(rol.id)
            print(rol_ant)
            rol_ant.nombre = rol.nombre
            rol_ant.descripcion = rol.descripcion
            print(rol_ant)
            sesion.commit()
        except Exception as ex:
            raise ex.args


class DBRepositorioUsuario(RepositorioDB):

    def actualizar(self, usuario):
        try:
            Sesion = sessionmaker(bind=self._persistidor.recurso)
            sesion = Sesion()
            usuario_ant = sesion.query(self._entidad).get(usuario.id)
            print(usuario_ant)
            usuario_ant.usuario = usuario.usuario
            usuario_ant.contrasenia = usuario.contrasenia
            usuario_ant.nombre = usuario.nombre
            usuario_ant.apellido = usuario.apellido
            print(usuario_ant)
            sesion.commit()
        except Exception as ex:
            raise ex.args

    def asignar_rol(self, usuario, rol):
        try:
            Sesion = sessionmaker(bind=self._persistidor.recurso)
            sesion = Sesion()

            sesion.commit()
        except Exception as ex:
            raise ex.args


