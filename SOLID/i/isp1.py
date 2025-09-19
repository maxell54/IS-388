class Usuario:
   def __init__(self, codigo, nombre, email):
       self.codigo = codigo
       self.nombre = nombre
       self.email = email
   def acceder_sistema(self):
       return f"{self.nombre} ha accedido al sistema UNSCH"
class UsuarioConPrivilegios(Usuario):
   def modificar_notas(self, curso, nueva_nota):
       return f"Nota modificada en {curso}: {nueva_nota}"
class EstudianteUsuario(Usuario):
   def consultar_notas(self):
       return "Consultando notas del estudiante"
class ProfesorUsuario(UsuarioConPrivilegios):
   def asignar_nota(self, estudiante, curso, nota):
       return f"Nota asignada a {estudiante} en {curso}: {nota}"
class AdministradorUsuario(UsuarioConPrivilegios):
   def generar_reporte_general(self):
       return "Generando reporte administrativo"


administrador = AdministradorUsuario("ADM001", "pedro", "pedro@unsch.edu.pe")
profesor = ProfesorUsuario("P001", "Pelayo", "pelayo@unsch.edu.pe")
estudiante = EstudianteUsuario("2721001", "María García", "maria.garcia@unsch.edu.pe")
print(estudiante.modificar_notas('Cálculo I', 18.5))
print(profesor.modificar_notas('Cálculo I', 18.5))
print(profesor.asignar_nota('Ana López', 'Álgebra Linear', 17.0))
print(administrador.modificar_notas('Física II', 16.8))