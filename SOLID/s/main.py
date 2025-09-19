class Estudiante:
    def __init__(self, codigo, nombre, email, carrera):
        self.codigo = codigo
        self.nombre = nombre
        self.email = email
        self.carrera = carrera
        self.notas = []

    def agregar_nota(self, curso, nota, creditos):
        self.notas.append({
            'curso': curso,
            'nota': nota,
            'creditos': creditos,
        })

    def calcular_promedio_ponderado(self):
        if not self.notas:
            return 0

        suma_ponderado = sum(nota["nota"] * nota["creditos"] for nota in self.notas)
        total_creditos = sum(nota["creditos"] for nota in self.notas)

        return suma_ponderado / total_creditos if total_creditos > 0 else 0

    def generar_reporte_academico(self):
        reporte = f"=== REPORTE ACADEMICO UNSCH ===\n"
        reporte += f"Estudiante: {self.nombre} ({self.codigo})\n"
        reporte += f"Carrera: {self.carrera}\n"
        reporte += f"Email: {self.email}\n"
        reporte += f"HISTORIAL ACADEMICO:\n"

        for nota_info in self.notas:
            # Usamos comillas simples fuera para evitar conflicto
            reporte += f"- {nota_info['curso']}: {nota_info['nota']}\n"
            reporte += f"({nota_info['creditos']} créditos)\n"

        reporte += f"\nPromedio Ponderado: {self.calcular_promedio_ponderado():.2f}"
        return reporte

    def enviar_email_notificacion(self, mensaje):
        print(f"Enviando Email a {self.nombre}: {mensaje}")
        return True

    def guardar_en_base_datos(self):
        print(f"Guardando estudiante {self.nombre}: en base de datos...")
        return True


Estudiante1 = Estudiante(codigo="2700000", nombre="Carlos Lopez", email="carlos@gmail.com", carrera="Sistemas")

Estudiante1.agregar_nota(curso="Base de Datos", nota=19, creditos=5)

print(Estudiante1.generar_reporte_academico())

mensaje1 = Estudiante1.enviar_email_notificacion("Tu reporte esta listo")
guardar_bdatos1 = Estudiante1.guardar_en_base_datos()

#print(mensaje1)
#print(guardar_bdatos1)