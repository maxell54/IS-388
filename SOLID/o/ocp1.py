class TipoEstudiante:
    def calcular_costo(self):
        pass

class Maestria(TipoEstudiante):
    def calcular_costo(self):
        return 2500

class Doctorado(TipoEstudiante):
    def calcular_costo(self):
        return 3500

class SecEspecialida(TipoEstudiante):
    def calcular_costo(self):
        return 4000

class CalculadorMatricula:
    def calcular_costo(self, tipo_estudiante: TipoEstudiante):
        return tipo_estudiante.calcular_costo()

'''
# Crear instancias
doctorado = Doctorado()
calculador = CalculadorMatricula()

# Usar método
r1 = calculador.calcular_costo(doctorado)

print(r1)  # Esto imprimirá 3500
'''

r1 = CalculadorMatricula().calcular_costo(Doctorado())

print(r1)