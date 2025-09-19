from abc import ABC, abstractmethod

class ServicioMatriculas(ABC):
    @abstractmethod
    def matriculasr_curso(self,estudiante, curso):
        pass
class ServicioCalificaciones(ABC):
    @abstractmethod
    def calificar(self,estudiante , curso, nota):
        pass
class ServicioHorarios(ABC):
    @abstractmethod
    def generar_horarios(self, semestre):
        pass
class ServicioPagos(ABC):
    @abstractmethod
    def procesar_pagos(self, estudiante, monto):
        pass

class GestorMatricula(ServicioMatriculas):
    def matriculasr_curso(self, estudiante, curso):
        return f"Matriculando {estudiante} en {curso}"

class GestorCalificacion(ServicioCalificaciones):
    def calificar(self,estudiante, curso, nota):
        return f"Calificando {estudiante} en {curso} {nota}"