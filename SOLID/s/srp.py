from symtable import Class


class Estudiante:
    """Responsabilidad única: Representar la entidad Estudiante"""

    def __init__(self, codigo, nombre, email, carrera):
        self.codigo = codigo
        self.nombre = nombre
        self.email = email
        self.carrera = carrera


class RegistroAcademico:
    """Responsabilidad única: Gestionar el historial académico"""

    def __init__(self):
        self.notas = []

    def agregar_nota(self, curso, nota, creditos):
        self.notas.append({
            'curso': curso,
            'nota': nota,
            'creditos': creditos
        })

    def obtener_notas(self):
        return self.notas.copy()


class CalculadoraPromedio:
    """Responsabilidad única: Realizar cálculos académicos"""

    @staticmethod
    def calcular_promedio_ponderado(notas):
        if not notas:
            return 0
        suma_ponderada = sum(nota['nota'] * nota['creditos'] for nota in notas)
        total_creditos = sum(nota['creditos'] for nota in notas)
        return suma_ponderada / total_creditos if total_creditos > 0 else 0


class GeneradorReportes:
    """Responsabilidad única: Generar reportes académicos"""

    def generar_reporte_estudiante(self, estudiante, registro_academico):
        promedio = CalculadoraPromedio.calcular_promedio_ponderado(
            registro_academico.obtener_notas()
        )

        reporte = f"=== REPORTE ACADÉMICO UNSCH ===\n"
        reporte += f"Estudiante: {estudiante.nombre} ({estudiante.codigo})\n"
        reporte += f"Carrera: {estudiante.carrera}\n"
        reporte += f"Email: {estudiante.email}\n\n"
        reporte += "HISTORIAL ACADÉMICO:\n"
        reporte += "HISTORIAL ACADÉMICO:\n"


        for nota_info in registro_academico.obtener_notas():
            reporte += f"- {nota_info['curso']}: {nota_info['nota']} "
            reporte += f"({nota_info['creditos']} créditos)\n"

        reporte += f"\nPromedio Ponderado: {promedio:.2f}"
        return reporte



class Servicio_Email:
    def enviar_email_notificacion(self, destinatario, mensaje):
        print(f"Enviando Email a {destinatario}: {mensaje}")
        return True

class Repositorio_Estudiante:
    def guardar_en_base_datos(self, estudiante):
        print(f"Guardando estudiante {estudiante.codigo}: en base de datos...")
        return True


# Crear estudiante
estudiante1 = Estudiante(codigo="2700000", nombre="Carlos Lopez", email="carlos@gmail.com", carrera="Sistemas")

# Crear registro académico y agregar notas
registro = RegistroAcademico()
registro.agregar_nota(curso="Base de Datos", nota=20, creditos=5)
registro.agregar_nota(curso="Matemáticas", nota=18, creditos=4)
registro.agregar_nota(curso="Programación", nota=19, creditos=3)

# Generar reporte
#generador = GeneradorReportes()
#reporte1 = generador.generar_reporte_estudiante(estudiante1, registro)



#print(reporte1)


email_service = Servicio_Email()
email_service.enviar_email_notificacion(estudiante1.email,"Tu reporte académico está listo.")

repositorio = Repositorio_Estudiante()
repositorio.guardar_en_base_datos(estudiante1)

