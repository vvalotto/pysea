from sqlalchemy import *

db = create_engine('sqlite:///evaluaciones')

db.echo = True

metadata = MetaData(db)


carrera = Table('td_carrera', metadata,
                Column('id', Integer, primary_key=True),
                Column('a_nombre', String(50)),
                Column('a_institucion', String(50)),
                Column('a_plan', String(10)),
                Column('a_habilitado', Integer))

materia = Table('td_materia', metadata,
                            Column('id', Integer, primary_key=True),
                            Column('id_carrera', Integer, ForeignKey('td_carrera.id')),
                            Column('a_nombre', String(50)),
                            Column('habilitado', Integer))

usuario = Table('td_usuario', metadata,
                             Column('id', Integer, primary_key=True),
                             Column('usuario', String(20)),
                             Column('contrasenia', String(20)),
                             Column('nombre', String(50)),
                             Column('apellido', String(50)),
                             Column('habilitado', Integer),
                             Column('id_rol', Integer, ForeignKey('td_rol.id')))

rol = Table('td_rol', metadata,
                            Column('id', Integer, primary_key=True),
                            Column('a_nombre', String(50)),
                            Column('descripcion', String(500)),
                            Column('habilitado', Integer))

docente = Table('td_docente', metadata,
                            Column('id_usuario', Integer, ForeignKey('td_usuario.id'), primary_key=True),
                            Column('id_materia', Integer, ForeignKey('td_materia.id'), primary_key=True),
                            Column('habilitado', Integer))

alumno = Table('td_alumno', metadata,
                            Column('id_usuario', Integer, ForeignKey('td_usuario.id'), primary_key=True),
                            Column('id_materia', Integer, ForeignKey('td_materia.id'), primary_key=True),
                            Column('habilitado', Integer))

metadata.create_all()