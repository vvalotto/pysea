"""
Definición del Modelo de Domincio - Modulo de Administración de
Entidades Basicas
"""

class Rol(object):

    @property
    def nombre(self):
        return self.a_nombre

    @nombre.setter
    def nombre(self, valor):
        self.a_nombre = str(valor)

    @property
    def descripcion(self):
        return self.a_descripcion

    @descripcion.setter
    def descripcion(self, valor):
        self.a_descripcion = str(valor)

    @property
    def habilitado(self):
        return self.a_habilitado

    @habilitado.setter
    def habilitado(self, valor):
        self.a_habilitado = str(valor)

    def __init__(self):
        self.a_nombre = ""
        self.a_descripcion = ""
        self.a_habilitado = 0
        self.usuarios = []

    def __repr__(self):
        return '<Rol: %s>' % self.a_nombre

    def __str__(self):
        return '%s: %r' %(self.a_nombre, self.a_descripcion)


class Usuario(object):

    @property
    def usuario(self):
        return self.a_usuario

    @usuario.setter
    def usuario(self, valor):
        self.a_usuario = str(valor)

    @property
    def contrasenia(self):
        return self.a_contrasenia

    @contrasenia.setter
    def contrasenia(self, valor):
        self.a_contrasenia = str(valor)

    @property
    def nombre(self):
        return self.a_nombre

    @nombre.setter
    def nombre(self, valor):
        self.a_nombre = str(valor)

    @property
    def apellido(self):
        return self.a_apellido

    @apellido.setter
    def apellido(self, valor):
        self.a_apellido = str(valor)

    @property
    def habilitado(self):
        return self.a_habilitado

    @habilitado.setter
    def habilitado(self, valor):
        self.a_habilitado = str(valor)

    def __init__(self):
        self.a_usuario = ""
        self.a_contrasenia = ""
        self.a_nombre = ""
        self.a_apellido = ""
        self.a_habilitado = 0
        self.roles = []

    def __repr__(self):
        return '<Usuario: %s>' % self.a_nombre

    def __str__(self):
        return '%s: %r' %(self.a_nombre, self.a_descripcion + ' ' + self.a_apellido)


class Carrera(object):

    @property
    def nombre(self):
        return self.a_nombre

    @nombre.setter
    def nombre(self, valor):
        self.a_nombre = str(valor)

    @property
    def institucion(self):
        return self.a_institucion

    @institucion.setter
    def institucion(self, valor):
        self.a_institucion = str(valor)

    @property
    def plan(self):
        return self.a_plan

    @plan.setter
    def plan(self, valor):
        self.a_plan = str(valor)

    @property
    def habilitado(self):
        return self.a_habilitado

    @habilitado.setter
    def habilitado(self, valor):
        self.a_habilitado = str(valor)

    def __init__(self):
        self.a_nombre = ""
        self.a_institucion = ""
        self.a_plan = ""
        self.a_habilitado = 0
        self.materias = []

    def __repr__(self):
        return '<Carrera: %s - %s>' % (self.a_nombre, self.a_institucion)


class Materia(object):

    @property
    def nombre(self):
        return self.a_nombre

    @nombre.setter
    def nombre(self, valor):
        self.a_nombre = str(valor)

    @property
    def carrera(self):
        return self.a_carrera

    @carrera.setter
    def carrera(self, valor):
        self.a_carrera = valor.nombre
        self.id_carrera = valor.id

    @property
    def habilitado(self):
        return self.a_habilitado

    @habilitado.setter
    def habilitado(self, valor):
        self.a_habilitado = str(valor)

    def __init__(self):
        self.a_nombre = ""
        self.id_carrera = None
        self.a_carrera = None
        self.a_habilitado = 0

    def __repr__(self):
        return '<Materia: %s>' % self.a_nombre


class UsuarioRol(object):

    def __init__(self):
        self.id_usuario = 0
        self.id_rol = 0

