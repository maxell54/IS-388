class GeneradorPDF:
    def generador_reporte(self,datos):
        print("generador de reporte en formato PDF...")

class GeneradorReporteUNSCH:
    def __init__(self):
        self.generador = GeneradorPDF()

    def generar_reporte_aulas(self,datos_estudiantes):
        self.generador.generador_reporte(datos_estudiantes)