class Usuario:
   def __init__(self, codigo, nombre, email):
       self.codigo = codigo
       self.nombre = nombre
       self.email = email

   def acceder_sistema(self):
       return f"{self.nombre} ha accedido al sistema UNSCH"
   def modificar_notas(self, curso, nueva_nota):
       return f"Nota modificada en {curso}: {nueva_nota}"

class EstudianteUsuario(Usuario):
   def modificar_notas(self, curso, nueva_nota):
       raise PermissionError("Los estudiantes no pueden modificar notas")

class ProfesorUsuario(Usuario):
   def modificar_notas(self, curso, nueva_nota):
       return f"Profesor modificó nota en {curso}: {nueva_nota}"

estudiante = EstudianteUsuario("2721001", "María García", "maria.garcia@unsch.edu.pe")
profesor = ProfesorUsuario("P001", "Pelayo", "pelayo@unsch.edu.pe")
usuario_base = Usuario("ADM001", "Admin", "admin@unsch.edu.pe")
resultado = usuario_base.modificar_notas("Química I", 17.0)
#resultado1 = estudiante.modificar_notas("Química I", 17.0)
print(resultado)