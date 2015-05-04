from acceso_datos.persistidor import *
from acceso_datos.repositorio import *
from aplicacion.managers import *
from modelo.entidades import *


print('Inicio')

DBEvaluacion = DBPersistidor('sqlite:///evaluaciones')

print(type(DBEvaluacion))
DBEvaluacion.inicializar_tablas()
DBEvaluacion.inicializar_mapeos()

carrera_repositorio = DBRepositorioCarrera(DBEvaluacion, Carrera)
"""
materia_repositorio = DBRepositorioMateria(DBEvaluacion, Materia)
print(type(carrera_repositorio))
print(type(materia_repositorio))

carrera = Carrera()
carrera.nombre = 'Licenciatura en Sistemas de Información'
carrera.institucion = 'UADER'
carrera.plan = '2014'
carrera_repositorio.guardar(carrera)


mi_carrera = carrera_repositorio.obtener_por_id(carrera.id)
print("Recupero:", mi_carrera)

materia = Materia()
materia.nombre = 'Métricas de Software'
materia.carrera = mi_carrera
materia_repositorio.guardar(materia)

mi_materia = materia_repositorio.obtener_por_id(1)
print("Recupero:", mi_materia)
print('fin')
"""


carrera = Carrera()
mananger_carrera = ManagerCarrera(carrera_repositorio, carrera)
carrera = mananger_carrera.obtener_por_id(4)
print(carrera.nombre)
print(carrera.institucion)
print(carrera.materias)

print('fin')