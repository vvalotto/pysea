from sqlalchemy import Table, Column, Integer, String, ForeignKey

class Database(object):

    def __init__(self, metadata):
        '''
        Define los objetos tabla
        :return:
        '''

        self.carrera = Table('td_carrera', metadata,
                            Column('id', Integer, primary_key=True),
                            Column('a_nombre', String(50)),
                            Column('a_institucion', String(50)),
                            Column('a_plan', String(10)),
                            Column('a_habilitado', Integer))

        self.materia = Table('td_materia', metadata,
                            Column('id', Integer, primary_key=True),
                            Column('id_carrera', Integer, ForeignKey('td_carrera.id')),
                            Column('a_nombre', String(50)),
                            Column('a_habilitado', Integer))

        self.usuario = Table('td_usuario', metadata,
                             Column('id', Integer, primary_key=True),
                             Column('a_usuario', String(20)),
                             Column('a_contrasenia', String(20)),
                             Column('a_nombre', String(50)),
                             Column('a_apellido', String(50)),
                             Column('a_habilitado', Integer))

        self.rol = Table('td_rol', metadata,
                            Column('id', Integer, primary_key=True),
                            Column('a_nombre', String(50)),
                            Column('a_descripcion', String(500)),
                            Column('a_habilitado', Integer))

        self.rol_usuario = Table('td_rol_usuario', metadata,
                            Column('id_rol', Integer, ForeignKey('td_rol.id'), primary_key=True),
                            Column('id_usuario', Integer, ForeignKey('td_usuario.id'), primary_key=True))

        self.docente = Table('td_docente', metadata,
                            Column('id_usuario', Integer, ForeignKey('td_usuario.id'), primary_key=True),
                            Column('id_materia', Integer, ForeignKey('td_materia.id'), primary_key=True),
                            Column('a_habilitado', Integer))

        self.alumno = Table('td_alumno', metadata,
                            Column('id_usuario', Integer, ForeignKey('td_usuario.id'), primary_key=True),
                            Column('id_materia', Integer, ForeignKey('td_materia.id'), primary_key=True),
                            Column('a_habilitado', Integer))
        return