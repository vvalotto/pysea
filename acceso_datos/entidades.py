from sqlalchemy import *
from sqlalchemy.orm import *
from modelo.entidades import *

db = create_engine('sqlite:///evaluaciones')

db.echo = True

metadata = MetaData()

carrera = Table('td_carrera', metadata,
                Column('id', Integer, primary_key=True),
                Column('a_nombre', String(50)),
                Column('a_institucion', String(50)),
                Column('a_plan',String(10)),
                Column('a_habilitado', Integer))

mapper(Carrera, carrera, properties={
    'materias': relationship(Materia, backref='materia')
})

materia = Table('td_materia', metadata,
                Column('id', Integer, primary_key=True),
                Column('id_carrera', Integer, ForeignKey('td_carrera.id')),
                Column('a_nombre', String(50))
                )

mapper(Materia, materia)

Session = sessionmaker(bind=db)
db.echo = True
session = Session()

mi_carrera = Carrera()
mi_carrera.pinstitucion = 'FUINER'
mi_carrera.pnombre = 'Ingenieria de Sofware'
mi_carrera.pplan = '2013'
mi_carrera.habilitar()

session.add(mi_carrera)
session.flush()
session.commit()

mi_carrera.pnombre = 'Diseño'
session.flush()
session.commit()

