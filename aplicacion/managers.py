
class ManagerCarrera(object):

    def __init__(self, repositorio, carrera):
        self._carrera = carrera
        self._repositorio = repositorio

    def guardar(self):
        try:
            if self._carrera == None:
                raise ('Nada para guadar')
            if self._carrera.id == None:
                self._repositorio.guardar(self._carrera)
            else:
                self._repositorio.actualizar(self._carrera)

        except Exception as ex:
            raise(ex.args)

    def obtener_por_id(self, id):
        try:
            carrera = self._repositorio.obtener_por_id(id)
            return carrera
        except Exception as ex:
            raise(ex)

    def habilitar(self):
        self._carrera.habilitar = 1
        try:
            self._repositorio.actualizar(self._carrera)
        except Exception as ex:
            raise(ex.args)

    def deshabilitar(self):
        self._carrera.habilitar = 0
        try:
            self._repositorio.actualizar(self._carrera)
        except Exception as ex:
            raise(ex.args)



