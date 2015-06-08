
from infraestructura.persistencia.contexto.contexto_database import *
from infraestructura.persistencia.repositorios.administracion import *
from aplicacion.managers.core import *
from dominio.entidades.administracion import *


print('Inicio')

DBEvaluacion = ContextoDB('sqlite:///acceso_datos/evaluaciones')

print(type(DBEvaluacion))

DBEvaluacion.inicializar_tablas()
DBEvaluacion.inicializar_mapeos()

carrera_repositorio = DBRepositorioCarrera(DBEvaluacion, Carrera)
rol_repositorio = DBRepositorioRol(DBEvaluacion, Rol)
usuario_repositorio = DBRepositorioUsuario(DBEvaluacion, Usuario)

usuarios = usuario_repositorio.obtener_todos()

mi_usuario = usuario_repositorio.obtener_por_id(1)

for u in usuarios:
    print(u.roles)

roles = rol_repositorio.obtener_todos()

for r in roles:
    print(r.usuarios)

print(mi_usuario.nombre)
print(mi_usuario.roles[0].nombre)

print('fin')