
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

rol = Rol()
rol_manager = ManagerEntidad(rol_repositorio, rol)
rol = rol_manager.obtener_por_id(1)

print(rol.nombre)
print(rol.descripcion)
for u in rol.usuarios:
    print('<Usuario: %s>' % u.usuario )


usu = Usuario()
manager_usuario = ManagerEntidad(usuario_repositorio, usu)
usu = manager_usuario.obtener_por_id(1)

print(usu.usuario)
for r in usu.roles:
    print('<Usuario: %s>' % r.nombre)


usuario = Usuario()
usuario.nombre = 'Nombre'
usuario.apellido = 'Apellido'
usuario.usuario = 'usuario'
usuario.contrasenia = '12345'
usuario_manager = ManagerEntidad(usuario_repositorio, usuario)
usuario_manager.guardar()

print('fin')