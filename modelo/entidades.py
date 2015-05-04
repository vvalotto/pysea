"""
Definición de la entidad Carrera
"""

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