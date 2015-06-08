from sqlalchemy.orm import sessionmaker
from infraestructura.persistencia.repositorios.core import RepositorioDB
from dominio.entidades.administracion import *


class DBRepositorioCarrera(RepositorioDB):

    def actualizar(self, carrera):
        try:
            carrera_ant = self._persistidor.sesion.query(self._entidad).get(carrera.id)
            print(carrera_ant)
            carrera_ant.nombre = carrera.nombre
            carrera_ant.institucion = carrera.institucion
            carrera_ant.plan = carrera.plan
            carrera_ant.habilitado = carrera.habilitado
            print(carrera_ant)
            self._persistidor.sesion.commit()
        except Exception as ex:
            raise ex.args


class DBRepositorioMateria(RepositorioDB):

    def actualizar(self, materia):
        try:
            materia_ant = self._persistidor.sesion.query(self._entidad).get(materia.id)
            print(materia_ant)
            materia_ant.nombre = materia.nombre
            materia_ant.id_carrera = materia.id_carrera
            print(materia_ant)
            self._persistidor.sesion.commit()
        except Exception as ex:
            raise ex.args


class DBRepositorioRol(RepositorioDB):

    def actualizar(self, rol):
        try:
            rol_ant = self._persistidor.sesion.query(self._entidad).get(rol.id)
            print(rol_ant)
            rol_ant.nombre = rol.nombre
            rol_ant.descripcion = rol.descripcion
            print(rol_ant)
            self._persistidor.sesion.commit()
        except Exception as ex:
            raise ex.args


class DBRepositorioUsuario(RepositorioDB):

    def actualizar(self, usuario):
        try:
            usuario_ant = self._persistidor.sesion.query(self._entidad).get(usuario.id)
            print(usuario_ant)
            usuario_ant.usuario = usuario.usuario
            usuario_ant.contrasenia = usuario.contrasenia
            usuario_ant.nombre = usuario.nombre
            usuario_ant.apellido = usuario.apellido
            print(usuario_ant)
            self._persistidor.sesion.commit()
        except Exception as ex:
            raise ex.args

    def asignar_rol(self, usuario, rol):
        try:
            self._persistidor.sesion.commit()
        except Exception as ex:
            raise ex.args


class DBRepositorioDocente(RepositorioDB):

    def asignar_materia(self, docente, materia):
        pass

    def desasignar_materia(self, docente, materia):
        pass


class DBRepositorioAlumno(RepositorioDB):

    def asignar_materia(self, docente, materia):
        pass

    def actualizar(self, entidad):
        pass
